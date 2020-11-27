#Write a function generateDictionary that reads the file font3.txt
# and generate a dictionary where the key is the character
# ane the value is the 8*8 bit list representation of the character.

import click
# from gfxhat import backlight, lcd, fonts
from PIL import Image, ImageFont, ImageDraw


def generateDictionary():
    f = open('font3.txt','r')
    charList = []
    while True:
        line1 = f.readline()
        if line1 == "":#end of file
            break
        else:
            line1 = line1.replace("\n","").split(",")#delete the end of line symbol, and split the two items into list
        char = line1[1]#char
        value = line1[0]#hex value
        charList.append((char,value))
    charDict = dict(charList)#convert list to dict
    return charDict

chars = generateDictionary() #put the dictionary to the variable chars


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


# Write a program that reads a character from the user and displays the associate character
# on the gfxHat at the coordinates of your choice.
# Characters not present in the dictionary are ignored and a message is displayed on the computer screen.

print('Please press a key: ')
c = click.getchar()
print(c)
n = 0
for key in chars.keys():
    if key == c:
        clearScreen(lcd)
        displayText(chars[key], lcd, 2, 10)
        n = 1
if n == 0:
    msg = "The key you input isn't recorded in the dictionary."
    clearScreen(lcd)
    displayText(msg, lcd, 2, 10)





