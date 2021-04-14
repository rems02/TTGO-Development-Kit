# TTGO ST7789 Driver for MicroPython #
This driver is based on [russhughes](https://github.com/russhughes/st7789_mpy) and [devbis](https://github.com/devbis/st7789_mpy) st7789_mpy driver. I modified the original driver for one of my projects to add:

- Text processing on the screen (display left, right, center up, down ...)
- Display of figures (square, rectangle, pentagon, circle, ellipse ... - filled and empty)
- on-screen **MENU** management
- **FTP** file transfer ([robert-hh](https://github.com/robert-hh/FTP-Server-for-ESP8266-ESP32-and-PYBD))


---


## WordProcessing.py ##
#### How to use the functions ####


start by importing the file

```import WordProcessing as wp```

Centers the text in the middle of the screen:

```CentreTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3)```

Displays the text at the top left of the screen:

```LeftTopTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3)```

Displays the text at the bottom left of the screen

```LeftBottomTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3)```

Display the text at the top right of the screen:

```RightTopTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3)```

Display the message at the bottom right of the screen:

```RightBottomTxt(font, txt, ColorTxt, ColorFonTxt, ajust_x=0, ajust_y=0, rotation=3)```

Displays newline messages:

```message(txt, ColorTxt, ColorFonTxt, rotation=3)```

**font** your font

**txt:** your text

**ColorTxt:** your text color

**ColorFonTxt:** your backgroud text color

**ajust_x (optional):** X-axis adjustment of x pixel

**ajust_y (optional):** Y-axis adjustment of y pixel

**rotation (optional):** screen position
