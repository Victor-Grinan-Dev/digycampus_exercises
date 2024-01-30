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

# for i in range(len(files)):
    # print('tarkistetaan '  + files[i] + ' - ' + tarkista(files[i]))
    # print()

#ex.5
text = "Kallen Rautakanget Oy, on suomessa 1810 perustettu yritys, jonka merkittävimpiä tuotteita ovat erilaiset rautakanget. Vuonna 1920 yrityksen johtoon astui Kalle Kankinen, perheyrityksen nuorimmainen, joka uudisti merkittävästi yrityksen ulkoasua ja markkinointia. Kallen Rautakanget Oy:n uudeksi maskotiksi tulikin Paavo Pesukarhu, joka rautakanki kädessä tutkiskelee roskakoreja"
def korjaa_teksti(teksti):
    step1 = teksti.replace('Kaken Kanki Oy', 'Kallen Rautakanget Oy')
    step2 = step1.replace('ryövää', 'tutkiskelee')
    step3 = step2.replace('hämärähommat', 'remontit')
    print(step3)

# korjaa_teksti(text)
    
#ex.6
text = 'yksinkertainen testi. toimiikohan funktiosi'
def isot_alkukirjaimet(merkkijono):
    final_merkkijono_lista = []
    merkkijono_lista = merkkijono.split('. ')

    for sentence in range(len(merkkijono_lista)):
        clean_sentence = merkkijono_lista[sentence].strip()
        final_merkkijono_lista.append(clean_sentence[0].upper() + clean_sentence[1:])

    final_text = '. '.join(final_merkkijono_lista)
    return final_text

# print(isot_alkukirjaimet(text))
"""
# Write a function 'remove_parentheses' that processes the given text (string) and removes everything inside parentheses or [square brackets]. The function also ensures that removing parentheses does not result in double spaces.

# Example:
# "Hello [there]" -> "Hello" and NOT "Hello  "

def remove_parentheses(text):
    result = ""
    stack = []  # Use a stack to keep track of open parentheses
    
    for char in text:
        if char == '(' or char == '[':
            stack.append(char)  # Push open parentheses onto the stack
        elif char == ')' and stack and stack[-1] == '(':
            stack.pop()  # Pop matching open parenthesis from the stack
        elif char == ']' and stack and stack[-1] == '[':
            stack.pop()  # Pop matching open square bracket from the stack
        elif not stack:
            result += char  # Add non-parenthesis characters to the result
    
    return result

# Example usage:
text_to_process = "Hello [there] (and) goodbye"
result_text = remove_parentheses(text_to_process)
print(result_text)


"""
	
teksti = "Stephen Fain \"Steve\" Earle (s. 17. tammikuuta 1955 Fort Monroe, Hampton, Virginia) on \
yhdysvaltalainen muusikko, lauluntekijä ja tuottaja. Nashvillessä 1970-luvun puolivälissä Earle sai \
opetusta laulujen tekemiseen Townes Van Zandtiltä ja Guy Clarkilta. Earle on ollut yhteiskunnallisesti \
aktiivinen. Teini-iässä hän vastusti Vietnamin sotaa. Hän on lauluissaan ottanut kantaa sosiaaliseen ja \
taloudelliseen eriarvoisuuteen. Hän on vastustanut kuolemanrangaistusta ja maamiinoja. Yhdysvaltain \
presidentinvaaleissa vuonna 2016 hän kannatti Bernie Sandersia. 1990-luvun puolivälissä \
Earle pääsi eroon pitkään kestäneestä huumeriippuvuudesta.[1][2]"
teksti2 = "Testataan vielä sisäkkäisten sulkujen (eli tällaisten (sulkujen) ja [hakasulkujen][[hei] ja moi]) toimintaa."
def poista_sulut(merkkijono):
    result = ""
    stack = "" 
    count_1 = 0
    count_2 = 0
    
    for char in merkkijono:
        if char == '(':
             stack += char
             count_1 += 1
        elif char == '[':
            stack += char
            count_2 += 1
        elif char == ')' and stack and stack[0] == '(':
            count_1 -= 1
            if count_1 == 0:
                stack = ''
        elif char == ']' and stack and stack[0] == '[':
            count_2 -= 1
            if count_2 == 0:
                stack = ''
        elif not stack:
            result += char 

    result = result.replace('  ', ' ')

    return result

print(poista_sulut(teksti2))