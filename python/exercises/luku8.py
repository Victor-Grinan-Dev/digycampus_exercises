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

# print(poista_sulut(teksti2))

"""
# In English
# TASK
# Write 3 functions:

# Function word_lengths() that processes the given text (string) and examines its words.
# The function should return a list containing the occurrences of words of different lengths.
# The first element of the list (index 0) is the number of words with 0 characters (always 0),
# the second element (index 1) is the number of words with 1 character, and so on.
# The returned list has a length of the longest word + 1 (if the longest word is 6 characters, the list has 7 elements).
# Example: word_lengths("Matilla on kana.") returns [0, 0, 1, 0, 1, 0, 0, 1].

# Function longest_word() that processes the given text (string) and finds its longest word.
# If there are multiple words of the same length, return the first one.
# Return the word converted to lowercase.
# Example: longest_word("Matilla on kana.") returns "matilla".

# Function shortest_word() that processes the given text (string) and finds its shortest word.
# If there are multiple words of the same length, return the first one.
# Return the word converted to lowercase.
# Ignore words with fewer than 2 characters.
# Example: shortest_word("Matilla on kana.") returns "on".

# General Notes:
# The concept of a "word" in this task is loosely defined.
# A word is considered any string surrounded by spaces, from which trailing periods and commas have been removed.
# Remove trailing periods and commas from the end of words before examining their length.
# You can use the split() method to separate words based on spaces.
# For more information, refer to: https://www.w3schools.com/python/ref_string_split.asp

def word_lengths(text):
    words = [word.strip('.,') for word in text.split()]
    lengths = [0] * (max(len(word) for word in words) + 1)
    
    for word in words:
        lengths[len(word)] += 1
    
    return lengths

def longest_word(text):
    words = [word.strip('.,') for word in text.split()]
    longest = max(words, key=len)
    return longest.lower()

def shortest_word(text):
    words = [word.strip('.,') for word in text.split() if len(word) >= 2]
    shortest = min(words, key=len)
    return shortest.lower()

# Testing with the provided example
text_example = "Matilla on kana."
print(word_lengths(text_example))
print(longest_word(text_example))
print(shortest_word(text_example))

"""
#ex.8
teksti = "Butterflies Are Free is a play by Leonard Gershe. \
Loosely based on the life of attorney Harold Krents, the plot \
revolves around a blind man living in downtown Manhattan whose \
controlling mother disapproves of his relationship with a free-spirited \
hippie. The title was inspired by a passage in Charles Dickens' \
Bleak House: \"I only ask to be free. The butterflies are free. \
Mankind will surely not deny to Harold Skimpole what it concedes to the \
butterflies.\" After 12 previews, the Broadway production, directed by \
Milton Katselas, opened on October 21, 1969 at the Booth Theatre, where it \
ran for 1,128 performances. The original cast consisted of Keir Dullea, \
Blythe Danner, Eileen Heckart, and Paul Michael Glaser. Replacements during \
the run included Gloria Swanson, Pamela Bellwood, Kipp Osborne and \
David Huffman. Stephen Schwartz composed the title song. Gershe, Katselas, \
Heckart, and Glaser were reunited for the 1972 screen adaptation (set in San \
Francisco) with Edward Albert and Goldie Hawn. Heckart won an Academy Award \
for best supporting actress for her role in the film."

teksti2 = "Parasite is a 2019 South Korean black comedy thriller film directed \
by Bong Joon-ho, who also co-wrote the screenplay with Han Jin-won. It stars \
Song Kang-ho, Lee Sun-kyun, Cho Yeo-jeong, Choi Woo-shik, Park So-dam, and \
Jang Hye-jin and follows the members of a poor family who scheme to become \
employed by a wealthy family by infiltrating their household and posing as \
unrelated, highly qualified individuals. The film premiered at the 2019 \
Cannes Film Festival on 21 May 2019, where it became the first South \
Korean film to win the Palme d'Or and the first film to win with a unanimous \
vote since Blue Is the Warmest Colour at the 2013 Festival. It was then released in \
South Korea by CJ Entertainment on 30 May 2019. The film received critical acclaim \
and has featured in listings of the best films of the 2010s. It has grossed over $207 \
million worldwide on a production budget of about $11 million, \
becoming one of South Korea's highest-grossing films."

def pisin_sana(merkkijono):
    longest = ''
    merkkijono = merkkijono.replace('.', ' ')
    string_list = merkkijono.split(' ')
    for el in string_list:
        if el.isalpha and len(el) > len(longest):
            longest = el
    return longest.lower()

def lyhyin_sana(merkkijono):
    shortest = ''
    merkkijono = merkkijono.replace('.', ' ')
    string_list = merkkijono.split(' ')
    for el in string_list:
        if not shortest and len(el) > 2:
            shortest = el
        elif len(el) > 1 and len(el) < len(shortest):
            shortest = el
    return shortest.lower()

def sanamaarat(merkkijono):

    result = []
    list_length = len(pisin_sana(merkkijono))
    merkkijono = merkkijono.replace('.', ' ')
    merkkijono = merkkijono.replace(',', ' ')
    # merkkijono = merkkijono.replace('"', ' ')
    # merkkijono = merkkijono.replace('"', ' ')
    string_list = merkkijono.split(' ')

    while list_length >= 0:
        result.append(0)
        list_length -= 1
    
    for el in string_list:      
        if len(el) > 0 and el.isalnum():
            index = len(el)
            result[index] += 1
            if len(el) == 1:
                print(el)

    return result

print(sanamaarat(teksti))
