import WordProcessing as wp
from time import sleep
import sys
import urequests
from machine import Pin


button0 = Pin(0, Pin.IN)
button35 = Pin(35, Pin.IN)

compteur_menu0 = 0
compteur_menu35 = 0


# Menu a afficher
menu1 = "* Horloge/Tmp"
menu2 = "* Ex fonts"
menu3 = "* Ex toaster"
menu4 = "* FTP Start"
menu5 = "* test.py"

# fonction qui construit le menu
def menu(): 
    wp.tft.rect(0, 0, 240, 135, wp.st7789.BLUE)
    wp.tft.fill_rect(0, 0, 240, 23, wp.st7789.BLUE)
    #wp.tft.hline(0, 23, 240, wp.st7789.GREEN)
    wp.tft.text(wp.vga1_16x16, "* Menu *", wp.centre_x(wp.vga1_bold_16x16,"* Menu *"), 5,wp.st7789.GREEN, wp.st7789.BLUE) # Titre
    wp.LeftTopTxt(wp.vga1_16x16, menu1, wp.st7789.GREEN, wp.st7789.BLACK,5,5+26,3) # Menu 1
    wp.LeftTopTxt(wp.vga1_16x16, menu2, wp.st7789.GREEN, wp.st7789.BLACK,5,5+47,3) # Menu 2
    wp.LeftTopTxt(wp.vga1_16x16, menu3, wp.st7789.GREEN, wp.st7789.BLACK,5,5+68,3) # Menu 3
    wp.LeftTopTxt(wp.vga1_16x16, menu4, wp.st7789.GREEN, wp.st7789.BLACK,5,5+89,3) # Menu 4
    wp.LeftTopTxt(wp.vga1_16x16, menu5, wp.st7789.GREEN, wp.st7789.BLACK,5,5+110,3) # Menu 5
   
 
wp.tft.on()
wp.tft.init()
menu()

while True:
 
    #si click sur button0 surbrilance menu suivant 
    #si click sur button35 validation de choix
    #1 - menu 1 -> Horloge / Temperature
    #2 - menu 2
    #3 - menu 3    ...
  
  if button0.value() == 0:
    wp.tft.on()
    compteur_menu0 = compteur_menu0 + 1
    sleep(0.1)
    if compteur_menu0 == 6:
      compteur_menu0 = 0
      
    if compteur_menu0 == 1:
      menu()
      wp.LeftTopTxt(wp.vga1_16x16, menu1, wp.st7789.BLACK, wp.st7789.GREEN,5,5+26,3)
    elif compteur_menu0 == 2:
      menu()
      wp.LeftTopTxt(wp.vga1_16x16, menu2, wp.st7789.BLACK, wp.st7789.GREEN,5,5+47,3)
    elif compteur_menu0 == 3:
      menu()
      wp.LeftTopTxt(wp.vga1_16x16, menu3, wp.st7789.BLACK, wp.st7789.GREEN,5,5+68,3)
    elif compteur_menu0 == 4:
      menu()
      wp.LeftTopTxt(wp.vga1_16x16, menu4, wp.st7789.BLACK, wp.st7789.GREEN,5,5+89,3)
    elif compteur_menu0 == 5:
      menu()
      wp.LeftTopTxt(wp.vga1_16x16, menu5, wp.st7789.BLACK, wp.st7789.GREEN,5,5+110,3)   


  if button35.value() == 0:
    if compteur_menu0 == 1:
      exec(open("./horloge.py").read()) 
    if compteur_menu0 == 2:
      exec(open("./fonts.py").read()) 
    if compteur_menu0 == 3:
      exec(open("./toasters.py").read()) 
    if compteur_menu0 == 4:
      import ftp
    if compteur_menu0 == 5:
      #wp.tft.off()
      exec(open("./test.py").read()) 
  sleep(0.1)














