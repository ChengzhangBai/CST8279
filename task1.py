from gfxhat import backlight, lcd, fonts
from PIL import Image, ImageFont, ImageDraw
from click import getchar 

def clearScreen(lcd):
    lcd.clear()
    lcd.show()
def displayText(text,lcd,x,y):
    lcd.clear()
    backlight.set_all(120,120,120)
    backlight.show()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
            lcd.show() 

def etchSketch(x,y):
    while True:
        key = getchar()
        lcd.set_pixel(x,y,1)
        lcd.show()
        if key == 's':
            clearScreen(lcd)
            x = 0
            y = 0
        elif key == '\x1b[A':
            y -= 1
            if y == 0:
                y = 63
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == '\x1b[B':
            y += 1
            if y == 63:
                y = 0 
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == '\x1b[C':
            x += 1
            if x == 127:
                x = 0 
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == '\x1b[D':
            x -= 1
            if x == 0:
                x = 127 
            lcd.set_pixel(x,y,1)
            lcd.show()
        elif key == 'q':
            lcd.clear()
            lcd.show()
            backlight.set_all(0,0,0)
            backlight.show()
            exit()

clearScreen(lcd)           
displayText('Lab9',lcd,0,0)
etchSketch(0,0)
c = getchar()
clearScreen(lcd)
