#1. Missing names will be set to "MISSING DATA"
#2. Missing number will be set to "N/A"
#3. Duplicated entries will only be wrote to the csv file once
def getNumber(x): #get numbers in a string
    return filter(str.isdigit, str(x))
def getStr(x): #get alphabets in a string
    return filter(str.isalpha, str(x))

def txt2csv(file):
    fileName = '2000_' + file.capitalize() + 'sNames'
    f1 = open(fileName + '.txt',"r")
    lines_exist = set()  # the set is used to check if an entry is duplicate
    f2 = open(fileName + '.csv',"w") # overwrite data if file already exists
    f2.write('First name,Count\n')
    duplicate_num = 0 #number of duplicated entries
    while True:
        data = f1.readline()
        if data == "": #end of file
            break
        if data.find(',') == -1: # if comma not found
            number = list(getNumber(data)) #change the filtered item to a list
            name = list(getStr(data))
            if len(name) == 0:#if no alphabets contained in a string
                name = 'MISSING DATA' # empty item will not be deleted but commented, the value can be changed
            if len(number) == 0:
                number = 'N/A'
            data = ''.join(name) + ',' + ''.join(number) + '\n'
        if data not in lines_exist: #the duplicated entries will not be added
            f2.write(data)
            lines_exist.add(data)
        else:
            duplicate_num += 1
            print('"%s" skipped as it already exists.'%data.replace("\n",""))

    print('The data for %ss have been wrote into a csv file named %s.csv.' % (file,fileName))
    print('Number of total duplicated entries is: %d'%duplicate_num)
    f1.close()
    f2.close()

file = input('Please input the file name you want to process:\n\
enter "boy" for 2000_BoysNames.txt, "girl" for 2000_GirlsNames.txt,\n\
default or wrong input will be set to boy: ')
if file == "" or file not in('boy','girl'):
    file = 'boy'
txt2csv(file)