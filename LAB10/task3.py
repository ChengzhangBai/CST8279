#Author: Chengzhang Bai @AC
#Date: Nov. 27, 2020
import click

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

        value = hex2bin(line1[0])
        charList.append((char,value))
    charDict = dict(charList)#convert list to dict
    return charDict

# def hex2bin(hexValue): #convert hex value to binary form
#     binValue = bin(int(hexValue, 16))[2:].zfill(8)
#     diff = 64 - len(binValue)
#     if diff > 0:
#         binValue = binValue + diff * "0"  # if less than 64, then add 0 at the end to 64
#     return binValue


def hex2bin(hexValue):
    hexValueList = list(hexValue[2:])
    # binValue = bin(int(hexValue, 16))[2:].zfill(8)
    binValueList = []
    for i in hexValueList:
        binValue = bin(int(i, 16))[2:].zfill(4)
        binValueList.append(binValue)

    binValue = ''.join(binValueList)
    return binValue


def bitmapInHat():
    chars = generateDictionary() #put the dictionary to the variable chars
    print('Please press a key: ')
    c = click.getchar()
    print(c)
    n = 0
    for key in chars.keys():
        if key == c:
            binValue = chars[key]
            list = []
            for i in range(0, 8):
                for j in range(0, 8):
                    list.append(int(binValue[i * 8 + j])) #change the binary value from str to list
            chunks = [list[x:x + 8] for x in range(0, len(list),8)]  # Split the 64 digits in the list into 8*8 chunks, thanks to: https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
            print(chunks)
            n = 1
            break
    if n == 0:
        msg = "The key you input isn't recorded in the dictionary."
        print(msg)


bitmapInHat()
