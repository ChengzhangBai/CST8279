#Generate the character image from binary code

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


def hex2bin(hexValue):
    hexValueList = list(hexValue[2:])#ignore the first two letters 0x
    binValueList = []
    for i in hexValueList:
        binValue = bin(int(i, 16))[2:].zfill(4) #delete the first two letters 0b
        binValueList.append(binValue)
    binValue = ''.join(binValueList)
    return binValue


def printChar():
    chars = generateDictionary() #put the dictionary to the variable chars
    for key in chars.keys():
            binValue = chars[key]
            list = []
            for i in range(0, 8):
                for j in range(0, 8):
                    list.append(int(binValue[i * 8 + j])) #change the binary value from str to list
            chunks = [list[x:x + 8] for x in range(0, len(list),8)]  # Split the 64 digits in the list into 8*8 chunks, thanks to: https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
            charImg = str(chunks).replace('],','\n').replace('[[',' ').replace('[','').replace(']','').replace(',','').replace('0',' ').replace('1','∙')

            f = open('characterImage.txt', 'a', encoding='utf-8')
            f.write(key + '\n' +charImg + '\n\n')
    f.close()
    print('Character-image match pair file generated. Please open characterImage.txt for detail.')


printChar()
