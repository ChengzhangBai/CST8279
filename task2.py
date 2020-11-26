# Write a python program that prompts the user for the name of .csv file
# then reads and displays each line of the file as a Python list.
# Test your program on the 2 csv files that you generated in Task 1.
fileName = input('Please input "boy" or "girl" to open a file: ')
if fileName == "" or fileName not in('boy','girl'):
    fileName = 'boy'
try:
    fileName = '2000_'+ fileName.capitalize() + 'sNames.csv'
    names = open(fileName,'r')
    nameList = []
    for name in names:
        nameList.append(name.replace('\n',''))
        print(nameList)
        nameList=[]
    names.close()
except FileNotFoundError:
    print("File not found, please generate a csv file first.")
