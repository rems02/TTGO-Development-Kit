from machine import Pin, SPI
import st7789
from time import sleep
from math import ceil, cos, sin, pi, radians
# Load basic font from flash
import vga1_8x8, vga1_16x16, vga1_16x32, vga1_bold_16x16, vga1_bold_16x32
# Load several frozen fonts from flash
import gotheng
import greeks
import italicc
import italiccs
import meteo
import romanc
import romancs
import romand
import romanp
import romans
import romant
import scriptc
import scripts

# initialisation d'ecran TFT
tft = st7789.ST7789(
    SPI(2, baudrate=30000000, sck=Pin(18), mosi=Pin(19)),
    135,
    240,
    reset=Pin(23, Pin.OUT),
    cs=Pin(5, Pin.OUT),
    dc=Pin(16, Pin.OUT),
    backlight=Pin(4, Pin.OUT),
    rotation=3)


tft.init()

# fonction qui centre le texte sur X
def centre_x(font,txt,ajust = 0, rotation=3):
    tft.rotation(rotation)
    pos_x = int((tft.width()/2) - ((len(txt)/2) * int(font.WIDTH))) + ajust
    return(pos_x)
    
# fonction qui centre le texte sur Y    
def centre_y(font, ajust = 0, rotation=3):
    tft.rotation(rotation)
    pos_y = int(((tft.height())/2) - int(font.HEIGHT/2)) + ajust
    return(pos_y)
    
#fonction qui place le texte a gauche
def left(ajust = 0, rotation=3):
    tft.rotation(rotation)
    pos_x = 0 + ajust
    return(pos_x)
  
#fonction qui place le texte a droite
def right(txt,font, ajust = 0, rotation=3):
    tft.rotation(rotation)
    pos_x = int(tft.width() - (len(txt) * int(font.WIDTH))) - ajust
    return(pos_x)

#fonction qui place le texte en haut TOP
def top(ajust = 0, rotation=3):
    tft.rotation(rotation)
    pos_y = 0 + ajust
    return(pos_y)
 
#fonction qui place le texte en bas Bottom
def bottom(font, ajust = 0, rotation=3):
    tft.rotation(rotation)
    pos_y = int(tft.height()) - int(font.HEIGHT) - ajust
    return(pos_y)
    

#-----------------------------------------------------------------------

#fonction qui centre le message au milieu de l'ecran
def CentreTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3):
    tft.rotation(rotation)
    tft.text(font, txt, centre_x(font,txt,ajust_x,rotation), centre_y(font,ajust_y,rotation), ColorTxt, ColorFonTxt)    


#------------------------------------------------------------------------ 

#fonction qui affiche le message en haut a gauche de l'ecran
def LeftTopTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3):
    tft.rotation(rotation)
    tft.text(font, txt, left(ajust_x, rotation), top(ajust_y, rotation), ColorTxt, ColorFonTxt)


#------------------------------------------------------------------------ 

#fonction qui affiche le message en bas a gauche de l'ecran
def LeftBottomTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3):
    tft.rotation(rotation)
    tft.text(font, txt, left(ajust_x, rotation), bottom(font, ajust_y, rotation), ColorTxt, ColorFonTxt)


#------------------------------------------------------------------------ 

#fonction qui affiche le message en haut a droite de l'ecran
def RightTopTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3):
    tft.rotation(rotation)
    tft.text(font, txt, right(txt,font, ajust_x, rotation), top(ajust_y, rotation), ColorTxt, ColorFonTxt)


#------------------------------------------------------------------------ 

#fonction qui affiche le message en bas a droite de l'ecran
def RightBottomTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3):
    tft.rotation(rotation)
    tft.text(font, txt, right(txt,font, ajust_x, rotation), bottom(font, ajust_y, rotation), ColorTxt, ColorFonTxt)
    


#------------------------------------------------------------------------    
#fonction qui affiche des messages avec retour a la ligne
def message(txt, ColorTxt, ColorFonTxt, rotation=3):
    #tft.rotation(rotation)
    # determine le format de caracter en fonction de longueur de message.
    if 15 < len(txt) <= 60 and (rotation==1 or rotation==3):
      font = vga1_16x32
    elif 7 < len(txt) <= 56 and (rotation==2 or rotation==4):#
      font = vga1_16x32
      
    elif 60 < len(txt) <= 120 and (rotation==1 or rotation==3):
      font = vga1_16x16
    elif 56 < len(txt) <= 120 and (rotation==2 or rotation==4):#
      font = vga1_16x16
      
    elif len(txt) > 120: # and (rotation==1 or rotation==3):
      font = vga1_8x8
      
    elif len(txt) <= 15 and (rotation==1 or rotation==3):
      font = vga1_16x32
      tft.text(font, txt, centre_x(font,txt,0,rotation), centre_y(font,0,rotation), ColorTxt, ColorFonTxt)
    elif len(txt) <= 7 and (rotation==2 or rotation==4):
      font = vga1_16x32
      tft.text(font, txt, centre_x(font,txt,0,rotation), centre_y(font,0,rotation), ColorTxt, ColorFonTxt)
  
    if len(txt) > 15:
      tft.rotation(rotation)
      car = int((tft.width()/int(font.WIDTH)))
      i = 1
      j = 0
      t = car
      for r in range(ceil((len(txt)/car))):
        txt_form = txt[j:t]
        j = j + car
        i = i + 1
        t = car * i
        pos_y = r * int(font.HEIGHT)
        tft.text(font, txt_form, left(0,rotation), pos_y, ColorTxt, ColorFonTxt)
#------------------------------------------------------------------------ 


#----------------Figures-----------------

# dessine un cerle vide
def draw_circle(x0, y0, r, color):
        """Draw a circle.
        Args:
            x0 (int): X coordinate of center point.
            y0 (int): Y coordinate of center point.
            r (int): Radius.
            color (int): RGB565 color value.
        """
        f = 1 - r
        dx = 1
        dy = -r - r
        x = 0
        y = r
        tft.pixel(x0, y0 + r, color)
        tft.pixel(x0, y0 - r, color)
        tft.pixel(x0 + r, y0, color)
        tft.pixel(x0 - r, y0, color)
        while x < y:
            if f >= 0:
                y -= 1
                dy += 2
                f += dy
            x += 1
            dx += 2
            f += dx
            tft.pixel(x0 + x, y0 + y, color)
            tft.pixel(x0 - x, y0 + y, color)
            tft.pixel(x0 + x, y0 - y, color)
            tft.pixel(x0 - x, y0 - y, color)
            tft.pixel(x0 + y, y0 + x, color)
            tft.pixel(x0 - y, y0 + x, color)
            tft.pixel(x0 + y, y0 - x, color)
            tft.pixel(x0 - y, y0 - x, color)


# dessine une ellipse
def draw_ellipse(x0, y0, a, b, color):
        """Draw an ellipse.
        Args:
            x0, y0 (int): Coordinates of center point.
            a (int): Semi axis horizontal.
            b (int): Semi axis vertical.
            color (int): RGB565 color value.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the axes are integer rounded
            up to complete on a full pixel.  Therefore the major and
            minor axes are increased by 1.
        """
        a2 = a * a
        b2 = b * b
        twoa2 = a2 + a2
        twob2 = b2 + b2
        x = 0
        y = b
        px = 0
        py = twoa2 * y
        # Plot initial points
        tft.pixel(x0 + x, y0 + y, color)
        tft.pixel(x0 - x, y0 + y, color)
        tft.pixel(x0 + x, y0 - y, color)
        tft.pixel(x0 - x, y0 - y, color)
        # Region 1
        p = round(b2 - (a2 * b) + (0.25 * a2))
        while px < py:
            x += 1
            px += twob2
            if p < 0:
                p += b2 + px
            else:
                y -= 1
                py -= twoa2
                p += b2 + px - py
            tft.pixel(x0 + x, y0 + y, color)
            tft.pixel(x0 - x, y0 + y, color)
            tft.pixel(x0 + x, y0 - y, color)
            tft.pixel(x0 - x, y0 - y, color)
        # Region 2
        p = round(b2 * (x + 0.5) * (x + 0.5) +
                  a2 * (y - 1) * (y - 1) - a2 * b2)
        while y > 0:
            y -= 1
            py -= twoa2
            if p > 0:
                p += a2 - py
            else:
                x += 1
                px += twob2
                p += a2 - py + px
            tft.pixel(x0 + x, y0 + y, color)
            tft.pixel(x0 - x, y0 + y, color)
            tft.pixel(x0 + x, y0 - y, color)
            tft.pixel(x0 - x, y0 - y, color)


# dessine un cercle plain
def fill_circle(x0, y0, r, color):
        """Draw a filled circle.
        Args:
            x0 (int): X coordinate of center point.
            y0 (int): Y coordinate of center point.
            r (int): Radius.
            color (int): RGB565 color value.
        """
        f = 1 - r
        dx = 1
        dy = -r - r
        x = 0
        y = r
        tft.vline(x0, y0 - r, 2 * r + 1, color)
        while x < y:
            if f >= 0:
                y -= 1
                dy += 2
                f += dy
            x += 1
            dx += 2
            f += dx
            tft.vline(x0 + x, y0 - y, 2 * y + 1, color)
            tft.vline(x0 - x, y0 - y, 2 * y + 1, color)
            tft.vline(x0 - y, y0 - x, 2 * x + 1, color)
            tft.vline(x0 + y, y0 - x, 2 * x + 1, color)

# dessine elipse plaine
def fill_ellipse(x0, y0, a, b, color):
        """Draw a filled ellipse.
        Args:
            x0, y0 (int): Coordinates of center point.
            a (int): Semi axis horizontal.
            b (int): Semi axis vertical.
            color (int): RGB565 color value.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the axes are integer rounded
            up to complete on a full pixel.  Therefore the major and
            minor axes are increased by 1.
        """
        a2 = a * a
        b2 = b * b
        twoa2 = a2 + a2
        twob2 = b2 + b2
        x = 0
        y = b
        px = 0
        py = twoa2 * y
        # Plot initial points
        tft.line(x0, y0 - y, x0, y0 + y, color)
        # Region 1
        p = round(b2 - (a2 * b) + (0.25 * a2))
        while px < py:
            x += 1
            px += twob2
            if p < 0:
                p += b2 + px
            else:
                y -= 1
                py -= twoa2
                p += b2 + px - py
            tft.line(x0 + x, y0 - y, x0 + x, y0 + y, color)
            tft.line(x0 - x, y0 - y, x0 - x, y0 + y, color)
        # Region 2
        p = round(b2 * (x + 0.5) * (x + 0.5) +
                  a2 * (y - 1) * (y - 1) - a2 * b2)
        while y > 0:
            y -= 1
            py -= twoa2
            if p > 0:
                p += a2 - py
            else:
                x += 1
                px += twob2
                p += a2 - py + px
            tft.line(x0 + x, y0 - y, x0 + x, y0 + y, color)
            tft.line(x0 - x, y0 - y, x0 - x, y0 + y, color)
 
#dessine plusieurs lignes
def draw_lines(coords, color):
        """Draw multiple lines.
        Args:
            coords ([[int, int],...]): Line coordinate X, Y pairs
            color (int): RGB565 color value.
        """
        # Starting point
        x1, y1 = coords[0]
        # Iterate through coordinates
        for i in range(1, len(coords)):
            x2, y2 = coords[i]
            tft.line(x1, y1, x2, y2, color)
            x1, y1 = x2, y2


  
# dessine un polygone regulier
def draw_polygon(sides, x0, y0, r, color, rotate=0):
        """Draw an n-sided regular polygon.
        Args:
            sides (int): Number of polygon sides.
            x0, y0 (int): Coordinates of center point.
            r (int): Radius.
            color (int): RGB565 color value.
            rotate (Optional float): Rotation in degrees relative to origin.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the radius is integer rounded
            up to complete on a full pixel.  Therefore diameter = 2 x r + 1.
        """
        coords = []
        theta = radians(rotate)
        n = sides + 1
        for s in range(n):
            t = 2.0 * pi * s / sides + theta
            coords.append([int(r * cos(t) + x0), int(r * sin(t) + y0)])
        # Cast to python float first to fix rounding errors
        draw_lines(coords, color=color)
        


# dessine un polygonne regulier plain
def fill_polygon(self, sides, x0, y0, r, color, rotate=0):
        """Draw a filled n-sided regular polygon.
        Args:
            sides (int): Number of polygon sides.
            x0, y0 (int): Coordinates of center point.
            r (int): Radius.
            color (int): RGB565 color value.
            rotate (Optional float): Rotation in degrees relative to origin.
        Note:
            The center point is the center of the x0,y0 pixel.
            Since pixels are not divisible, the radius is integer rounded
            up to complete on a full pixel.  Therefore diameter = 2 x r + 1.
        """
        # Determine side coordinates
        coords = []
        theta = radians(rotate)
        n = sides + 1
        for s in range(n):
            t = 2.0 * pi * s / sides + theta
            coords.append([int(r * cos(t) + x0), int(r * sin(t) + y0)])
        # Starting point
        x1, y1 = coords[0]
        # Minimum Maximum X dict
        xdict = {y1: [x1, x1]}
        # Iterate through coordinates
        for row in coords[1:]:
            x2, y2 = row
            xprev, yprev = x2, y2
            # Calculate perimeter
            # Check for horizontal side
            if y1 == y2:
                if x1 > x2:
                    x1, x2 = x2, x1
                if y1 in xdict:
                    xdict[y1] = [min(x1, xdict[y1][0]), max(x2, xdict[y1][1])]
                else:
                    xdict[y1] = [x1, x2]
                x1, y1 = xprev, yprev
                continue
            # Non horizontal side
            # Changes in x, y
            dx = x2 - x1
            dy = y2 - y1
            # Determine how steep the line is
            is_steep = abs(dy) > abs(dx)
            # Rotate line
            if is_steep:
                x1, y1 = y1, x1
                x2, y2 = y2, x2
            # Swap start and end points if necessary
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            # Recalculate differentials
            dx = x2 - x1
            dy = y2 - y1
            # Calculate error
            error = dx >> 1
            ystep = 1 if y1 < y2 else -1
            y = y1
            # Calcualte minimum and maximum x values
            for x in range(x1, x2 + 1):
                if is_steep:
                    if x in xdict:
                        xdict[x] = [min(y, xdict[x][0]), max(y, xdict[x][1])]
                    else:
                        xdict[x] = [y, y]
                else:
                    if y in xdict:
                        xdict[y] = [min(x, xdict[y][0]), max(x, xdict[y][1])]
                    else:
                        xdict[y] = [x, x]
                error -= abs(dy)
                if error < 0:
                    y += ystep
                    error += dx
            x1, y1 = xprev, yprev
        # Fill polygon
        for y, x in xdict.items():
            tft.line(x[0], y, x[1] - x[0] + 2, color)
