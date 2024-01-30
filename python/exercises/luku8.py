#ex1
import random


def ex_1():
    teksti = 'Hello World!'
    kirjaimet:str

    a = 'Hello'
    b = ' '
    c = 'World!'
    yhdiste = a + b + c
    print(yhdiste)

    for i in range(len(teksti) ):
        print(teksti[i])

    for i in range(len(teksti)):
        if teksti[i] != ' ':
            kirjaimet+=teksti[i]

#ex2
def tarkista_merkkijono(x:str):
    result = []
    special_char = True
    # Does the string contain only letters or numbers?
    result.append(x.isalnum())
    result.append(x.isalpha())
    result.append(x.isnumeric())
    result.append(x.islower())
    for i in range(len(x)):
        if not x.strip():
            break
        elif x[i].isalpha or x[i].isnumeric:
            special_char = False
            break
    result.append(special_char)
    result.append(x.isupper())
    return result

#ex3
"""
# In English
A string can be sliced much like a list. The indices within the list now refer to the characters in the string.

For example:

word = 'Orange'
word[0]      # refers to the letter 'O'
word[0:3]    # refers to a slice of the word, from the beginning up to the third index, the first 3 letters 'Ora'
word[1:]     # refers to a slice of the word, from index 1 (the letter 'p') to the end, the string 'range'

TASK

Create a function create_usernames(students) that:

Iterates through the two-dimensional list students created by the given code and passed as an argument, which contains student information as lists. For example, students[0] is [name, surname, id].
Generates usernames from student information so that the student's username consists of:
- The first three letters of the student's surname in lowercase
- The first letter of the student's name in uppercase
- The first two letters of the student's id
For example, from the list element ['Matti', 'Smith', '123456'], the username 'smiM12' is created.

Adds the created username to the list and finally returns the list.

Tips!
Remember that you can iterate through a two-dimensional list, for example, one element (inner list) at a time, and refer to the information with indices as follows:

student_data = [['Matti', 'Smith', '123456'], ['Mervi', 'Jones', '123457']]

for student in student_data:
    # student receives three-element lists as values
    # for example, in the first iteration:
    # ['Matti', 'Smith', '123456']

You can convert a string to lowercase using the string.lower() function and to uppercase using the string.upper() function, used as follows:

name = 'Matti'
name_lowercase = name.lower()  # 'matti'
"""

etunimet = ("Antti", "Anna", "Sanna", "Simo", "Santeri","Saku","Teuvo","Taru","Eetu","Emilia")
sukunimet = ("Kivinen","Mäkinen","Jokinen","Beck","Päivärinne","Teuvonen")
opiskelijat = []

def luo_tunnukset(opiskelijat):
    final_list = []
    for opiskelija in opiskelijat:
        final_list.append(opiskelija[1][:3].lower() + opiskelija[0][0].upper() + opiskelija[2][:2])
    return final_list

for x in range(10):
    nimi = random.choice(etunimet)
    snimi = random.choice(sukunimet)
    num = str(random.randint(100000, 300000))
    opiskelijat.append([nimi,snimi,num])

# print(luo_tunnukset(opiskelijat))

#ex.4
"""
Create a function that checks whether the imaginary string passed to it is a valid file name, meaning it contains both the file name (prefix) and the file extension (global constant FILE_EXTENSIONS, which is a list of strings).

Create a 'check' function that checks the given string and prints:

'CORRECT' : if the string ends with one of the file extensions given in the task.
'WRONG' : if the string does not end with any of the specified file extensions OR if the string STARTS with any of the specified file extensions.
"""
files = ['aamupala',
'aurinko.doc',
'paivakirja.jpg',
'koirienkanssarannalla',
'koirienkanssarannalla.txt',
'koirienkanssarannalla.jpg',
'tiliote2019.png',
'.jpg',
'koirienkanssarannalla.png',
'aamupala.doc',
'.jpgAurinko',
'Aurinko.jpg',
'.jpg',
'.jpg.jpg']

TIEDOSTOPAATTEET = ['.txt', '.jpg', '.png', '.html', '.doc']

def tarkista(merkkijonoja):
    if len(merkkijonoja.split('.')) > 2 or len(merkkijonoja.split('.')) <= 1 or merkkijonoja.startswith('.'):
        return 'VÄÄRIN'
    else:
        return 'OIKEIN'

for i in range(len(files)):
    print('tarkistetaan '  + files[i] + ' - ' + tarkista(files[i]))
    print()

