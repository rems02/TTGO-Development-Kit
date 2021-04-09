#
# Recupere les informations mete sur le site OpenWeatherMap
# Recuperee l'heure et l'offset UTC sur le site Worldtimeapi.org
#

import network
import time
import machine
import json
import urequests
from machine import RTC
import WordProcessing as wp

button0 = Pin(0, Pin.IN)
wp.tft.init()

adresse_openweathermap = "https://api.openweathermap.org/data/2.5/weather?q=Septvaux&appid="
cle_api_openweathermap = "cb89e856f5811eb874c293b13c736b3b"
url_openweathermap = adresse_openweathermap + cle_api_openweathermap
url_worldtimeapi = "http://worldtimeapi.org/api/timezone/Europe/Paris"
requete_web_delai = 60000  # effectue une requete toutes les 60s
liste_jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
liste_mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin",
              "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]

def convert_epoch_time(temps):
    # Epoch time Linux demarre le 1 janvier 1970
    # Epoch time ESP32 demarre le 1 janvier 2000
    # donc il faut soustraire le temps de 946,684,800 secondes (30 ans)
    temps -= 946684800
    (u_annee, u_mois, u_jour, u_heure, u_minute, u_seconde, u_jour_semaine, u_jour_annee) = time.localtime(temps)
    return u_annee, u_mois, u_jour, u_heure, u_minute, u_seconde, u_jour_semaine

def traite_date_heure():
    global heure_offset, operation_offset, annee, mois, date, heure, minute, seconde, jour, rtc
    reponse = urequests.get(url_worldtimeapi)  # effectue la requete Web
    if reponse.status_code == 200:  # requete ok
        data = json.loads(reponse.text)  # transforme les donn閼煎崘s JSON en objet Python
        temps_unix = int(data.get("unixtime"))
        annee, mois, date, heure, minute, seconde, jour = convert_epoch_time(temps_unix)
        heure_offset = data.get("utc_offset")  # on recupere l'offset 
        operation_offset = heure_offset[0]  # recupere l'op閼煎嵐ateur + ou -
        heure_offset = int(heure_offset[2:3]) # recupere uniquement les heures
        if operation_offset == "+":
            heure += heure_offset
        if operation_offset == "-":
            heure -= heure_offset
        rtc.datetime((annee, mois, date, 0, heure, minute, seconde, 0))  # MAJ horloge interne
        mois = liste_mois[int(mois) - 1]
        jour = liste_jours[jour]
        
def traite_openweathermap():
    global temperature, pression, humidite, lever_soleil, coucher_soleil, vent_vitesse, vent_orientation
    reponse = urequests.get(url_openweathermap)  # effectue la requete Web
    if reponse.status_code == 200:  # requete ok
        data = json.loads(reponse.text)  # transforme les donnees JSON en objet Python
        temperature = data.get("main").get("temp")
        pression = data.get("main").get("pressure")
        humidite = data.get("main").get("humidity")
        annee_s, mois_s, date_s, heure_s, minute_s, seconde_s, jour_s = convert_epoch_time(data.get("sys").get("sunrise"))
        if operation_offset == "+":
            heure_s += heure_offset
        if operation_offset == "-":
            heure_s -= heure_offset
        lever_soleil = "{0:02}:{1:02}:{2:02}".format(heure_s, minute_s, seconde_s)
        annee_s, mois_s, date_s, heure_s, minute_s, seconde_s, jour_s = convert_epoch_time(data.get("sys").get("sunset"))
        if operation_offset == "+":
            heure_s += heure_offset
        if operation_offset == "-":
            heure_s -= heure_offset
        coucher_soleil = "{0:02}:{1:02}:{2:02}".format(heure_s, minute_s, seconde_s)
        vent_vitesse = data.get("wind").get("speed")  # vitesse du vent en m/s
        vent_vitesse *= 3.6  # conversion du vent en Km/h
        vent_orientation = data.get("wind").get("deg")  # origine du vent 
rtc = RTC()  # horloge temps reel interne
compteur = time.ticks_ms() - requete_web_delai  # initialise le compteur

wp.tft.rect(0, 0, 240, 135, wp.st7789.GREEN)
wp.tft.hline(0, 18, 240, wp.st7789.GREEN)
wp.tft.hline(0, 36, 240, wp.st7789.GREEN)
wp.tft.hline(0, 99, 240, wp.st7789.GREEN)
wp.tft.hline(0, 117, 240, wp.st7789.GREEN)
wp.CentreTxt(wp.vga1_16x32, "Loading", wp.st7789.RED, wp.st7789.BLACK)

while True:
    if time.ticks_ms() - compteur >= requete_web_delai: # test si 60s sont passees
        traite_date_heure()
        traite_openweathermap()
        time_str = "{:02}:{:02}".format(rtc.datetime()[4], rtc.datetime()[5])
        date_str = (jour) + " " + str(date) + " " + (mois) + " " + str(annee)
        print((jour) + " " + str(date) + " " + (mois) + " " + str(annee))
        print(time_str)
        print("Temperature : " + str(round(temperature-273.15,2)) + "C, Pression : " + str(pression) + " hPa, Taux d'humidite : " + str(humidite) + "%")    
        print("Lever Soleil : " + (lever_soleil) + ", Coucher Soleil : " + (coucher_soleil))
        vit_vent = "Vent: " + str(round(vent_vitesse,1)) + " Km/h" 
        dir_vent = "Dir: " + str(vent_orientation)
        lev_sol = "Lever Soleil : " + (lever_soleil)
        cou_sol = "Coucher Soleil : " + (coucher_soleil)
        print("Vitesse du vent : " + str(vent_vitesse) + " Km/h, Orientation : " + str(vent_orientation))
        
        wp.LeftTopTxt(wp.vga1_8x8, date_str, wp.st7789.GREEN, wp.st7789.BLACK,5,5,3)
        wp.LeftTopTxt(wp.vga1_8x8, lev_sol, wp.st7789.GREEN, wp.st7789.BLACK,5,23,3)
        wp.RightTopTxt(wp.vga1_8x8, str(round((temperature-273.15),2))+ "C", wp.st7789.GREEN, wp.st7789.BLACK,5,5,3)
        wp.CentreTxt(wp.vga1_16x32, "       ", wp.st7789.GREEN, wp.st7789.BLACK)
        wp.CentreTxt(wp.vga1_16x32, time_str, wp.st7789.GREEN, wp.st7789.BLACK)
        wp.LeftBottomTxt(wp.vga1_8x8, cou_sol, wp.st7789.GREEN, wp.st7789.BLACK,5,23,3)
        wp.LeftBottomTxt(wp.vga1_8x8, vit_vent, wp.st7789.GREEN, wp.st7789.BLACK,5,5,3)
        wp.RightBottomTxt(wp.vga1_8x8, dir_vent, wp.st7789.GREEN, wp.st7789.BLACK,5,5,3)
        
        compteur = time.ticks_ms()  # maj du compteur
        
    if button0.value() == 0:
      exec(open("./main.py").read()) # click button0 renvoi au menu general




