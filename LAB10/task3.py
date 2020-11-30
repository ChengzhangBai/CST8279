#Author: Chengzhang Bai @AC
#Date: Nov. 29, 2020
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
        char = line1[1]# line1[1]: char in font3.txt, e.g. A
        value = hex2bin(line1[0])# line1[0]: hex value of char in font3.txt, e.g. 0x3C00000000000000
        # split the 64-digit binary list into 8*8 form
        list = []
        for i in range(0, 8):
            for j in range(0, 8):
                list.append(int(value[i * 8 + j]))  # change the binary value from str to list
        chunks = [list[x:x + 8] for x in range(0, len(list), 8)]  # Split the 64 digits in the list into 8*8 chunks, thanks to: https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
        #print(chunks)
        charList.append((char,chunks))

    charDict = dict(charList)#convert list to dict
    # print(charDict)
    return charDict



def hex2bin(hexValue): #convert hex value to binary value, format of hexValue: 0x3C00000000000000
    hexValueList = list(hexValue[2:]) # delete 0x
    binValueList = [] #change hexvalue to list in order to loop
    for i in hexValueList:
        binValue = bin(int(i, 16))[2:].zfill(4)  #delete the leading 0b, then fill each binary value with 0 if it is less than 4 digits
        binValueList.append(binValue)
    binValue = ''.join(binValueList)
    #print(hexValue,binValue)
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
            print(binValue)
            n = 1
            break
    if n == 0:
        msg = "The key you input isn't recorded in the dictionary."
        print(msg)


bitmapInHat()


