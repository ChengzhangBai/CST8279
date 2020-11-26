from gfxhat import lcd, fonts
from PIL import Image, ImageFont, ImageDraw

f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

def displayObject(obj, x, y):
    lcd.clear()
    xp = x
    for y1 in obj:
        for x1 in y1:
            lenY = len(obj)
            lenX = len(y1)
            if x1 == 1:
                pixel = 1
            else:
                pixel = 0
            lcd.set_pixel(xp, y, pixel)
            xp += 1
        y += 1
        lcd.set_pixel(xp, y, pixel)
        xp = x
    lcd.show()
    
displayObject(f1, 16, 9)
