# Write a python program that:
# 1 asks the user for a record number between 1 and 24, other values must be ignored
# and the user prompted again. Character q quits the program.

while True:
    try:
        recNum = input('Please input a number between 1 and 24, enter q to quit the program: ')
        if recNum == 'q':
            quit()
        if int(recNum) <1 or int(recNum) > 24:
            print('Number out of range. ')
            continue
        break

    except ValueError:
        print('Invalid input, please input an integer number between 1 and 24.')
        continue
# 2 writes and executes a SQLite3 query to extract the Link field associated with the record.
# (research and use the sqlite3 module)

import sqlite3
import base64
conn = sqlite3.connect('week11.db')
c = conn.cursor()

c.execute("SELECT link FROM Lab10 WHERE ID=" + recNum)
link = c.fetchone()

# 3 decodes the base64 encoded value of the URL. (research and use the base64 module)

decodeLink = base64.b64decode(str(link))
#print(decodeLink)
# 4 opens a web browser with the decoded URL. (research and use the webbrowser module)
import webbrowser
webbrowser.open_new_tab(decodeLink)
# 5 for that specific record, asks the user for name of the city and the country and updates
# the record. (research and use the sqlite3 module).
cityName = input('Please input the city name: ').strip(' ')
countryName = input('Please input the country name: ').strip(' ')
if cityName != '' and countryName != '':
    sql = 'UPDATE Lab10 SET City ="%s", Country ="%s" WHERE ID = %s'%(cityName,countryName,recNum)
    c.execute(sql)
    conn.commit()
    print('Tha city name and country name of ID %s have been upated.'%recNum)
else:
    print('Please input city name and country name!')

conn.close()
