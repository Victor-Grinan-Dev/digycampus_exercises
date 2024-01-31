import pickle
import random
myset = {1, 2, 3}
mylist = [2, 3]
myset.add(3) 
# print(myset)
# print(len(myset))
myset2 = set(mylist)
def pickle_sample():
    print(myset)
    'pickle.dump(), pickle.load()'
    'numpy, pandas'

    # with open('test.pkl', 'wb') as file:
    #     pickle.dump({'name':'victor', 'age':40}, file)

    # with open('test.pkl', 'rb') as file:
    #     d = pickle.load(file)
    #     print(d)

    print(myset2.issubset(myset))
    print(myset.issuperset(myset2))

#ex.1
def ex_1():
    lisattavat = ["toinen", "testikierros", "lisää sekalaisia juttuja", 2353, True, "moi"]
    numerot = {i for i in range(1,11)}
    numerot.remove(6)
    numerot.update(lisattavat)
    print(numerot)

#ex.2
def ex_2():
    salibandy_osallistujat = set(("Simo", "Emmi", "Jari", "Pirkko", "Jenika","Samir","Tommi", "Aapo"))
    jaakiekko_osallistujat = set(("Emmi", "Sampo", "Heli", "Tiina", "Samir", "Silja", "Aapo"))
    koripallo_osallistujat = set(("Iina", "Tiina", "Samir", "Riikka", "Niina", "Tommi", "Aapo", "Pirkko"))
    joukko_1 = koripallo_osallistujat.intersection(salibandy_osallistujat)
    joukko_2 = salibandy_osallistujat.union(koripallo_osallistujat)
    joukko_3 = koripallo_osallistujat.difference(salibandy_osallistujat)
    joukko_4 = koripallo_osallistujat.symmetric_difference(salibandy_osallistujat)
    joukko_5 = koripallo_osallistujat.intersection(salibandy_osallistujat, jaakiekko_osallistujat)
    all_result = [
            joukko_1,
            joukko_2,
            joukko_3,
            joukko_4,
            joukko_5
        ]
    for i in all_result:
        print(i)

#ex3
def ex_3():
    englanti_suomi_sanakirja = {}
    englanti_suomi_sanakirja['apple' ]= 'omena'
    englanti_suomi_sanakirja['orange' ]= 'appelsiini'
    englanti_suomi_sanakirja['pear' ]= 'päärynä'

#ex.4
sanakirja_kalat = {'lohi' : 0, 'ahven' : 0}
kaikki_kalat = ['lohi', 'ahven', 'särki', 'hauki']
def laske_kalat(kala):
    if kala in sanakirja_kalat.keys():
        sanakirja_kalat[kala] = sanakirja_kalat[kala] + 1 

#ex.5
nimet = ['Marko', 'Marjatta', 'Mirja', 'Matti', 'Miso', 'Merja']
aloitus_id = 1
tunnukset = {}
for x in range(10):
    tunnukset[aloitus_id + x] = random.choice(nimet)
def ex_5():
    print(tunnukset[5])
    print(len(tunnukset))
    for key, value in tunnukset.items():
        print(key, value)
    print(tunnukset.get(15))
    print(tunnukset.pop(3))
    print(tunnukset.keys())
    print(tunnukset.values())
    print(tunnukset.items())

#ex.6
morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
}

def morseksi(teksti):
    global morse
    final_text = ''
    for i in teksti:
        if i == ' ':
            final_text += ' '
        elif i.lower() not in morse.keys():
            final_text += '?'
        else:
            final_text += morse[(i).lower()]
        final_text += ' '
    return final_text.strip()

#ex.7
def find_letter(morse_letter):
    global morse
    for key, value in morse.items():
        if morse_letter =='?':
            return '?'
        if morse_letter == value:
            return key


def morsesta(m):
    global morse
    final_text_list = []
    final_text = ''
        
    m_list = m.split('   ')
    for section in m_list:
        word = ''
        letters_list = section.split(' ')
        for letter in letters_list:
            word += find_letter(letter)
        final_text_list.append(word)

    final_text = ' '.join(final_text_list)
    return final_text.strip()

# print(morsesta( ". -. - ?   .--- --- ...   ... . .- ... ... .-   --- -.   . .-. .. -.- --- .. ... -- . .-. -.- -.- . .--- ? ?"))

#ex.8
T = "The Wright brothers – Orville (August 19, 1871 – January 30, 1948) and Wilbur \
(April 16, 1867 – May 30, 1912) – were two American aviation pioneers generally credited \
with inventing, building, and flying the world's first successful motor-operated airplane. \
They made the first controlled, sustained flight of a powered, heavier-than-air aircraft with \
the Wright Flyer on December 17, 1903, 4 mi (6 km) south of Kitty Hawk, North Carolina. In 1904–05, \
the brothers developed their flying machine to make longer-running and more aerodynamic flights with \
the Wright Flyer II, followed by the first truly practical fixed-wing aircraft, the Wright Flyer III. \
The Wright brothers were also the first to invent aircraft controls that made fixed-wing powered flight possible. \
The brothers' breakthrough was their creation of a three-axis control system, which enabled the pilot to steer the \
aircraft effectively and to maintain its equilibrium. This method remains standard on fixed-wing aircraft of \
all kinds. From the beginning of their aeronautical work, the Wright brothers focused on developing a reliable \
method of pilot control as the key to solving \"the flying problem\". This approach differed significantly from \
other experimenters of the time who put more emphasis on developing powerful engines. Using a \
small home-built wind tunnel, the Wrights also collected more accurate data than any before, enabling them \
to design more efficient wings and propellers. Their first U.S. patent did not claim invention of a \
flying machine, but a system of aerodynamic control that manipulated a flying machine's surfaces. \
The brothers gained the mechanical skills essential to their success by working for years in their Dayton, \
Ohio-based shop with printing presses, bicycles, motors, and other machinery. Their work with bicycles, \
in particular, influenced their belief that an unstable vehicle such as a flying machine could be controlled \
and balanced with practice. From 1900 until their first powered flights in late 1903, they conducted extensive glider \
tests that also developed their skills as pilots. Their shop employee Charlie Taylor became an \
important part of the team, building their first airplane engine in close collaboration with the brothers."

T1 = 'Testataan kirjoittamaasi funktiota. Toistetaan muutaman kerran pari sanaa. Sipuli Sipuli Sipuli omena omena apina apina apina apina apina'


def steralize(text:str):
    clean_text = ''
    for char in text:
        if char.isalpha() or char == ' ':
            clean_text += char
    return clean_text.lower().split(' ')

def created_keys(text_list:list):
    return set(text_list)

def create_dict_count(text_list:list):
    word_count = {}
    for key in created_keys(text_list):
        word_count[key] = 0
    return word_count

def populate_count_dict(merkkijono_list:list, dictionary:dict):
    for element in merkkijono_list:
        dictionary[element] = dictionary[element] + 1
    return dictionary

def create_analysoi_dic(count_dict:dict):
    final_dict = {}
    for key, value in count_dict.items():
        if value == 1 or key == '':
            pass
        elif value in final_dict:
            final_dict[value].append(key)
        else:
            final_dict[value] = [key]      
    return final_dict

def analysoi(merkkijono:str):
    merkkijono_list = steralize(merkkijono)
    empty_dict = create_dict_count(merkkijono_list)
    populated_dict = populate_count_dict(merkkijono_list, empty_dict)
    analysoi_dict = create_analysoi_dic(populated_dict)
    sorted_dict = dict(sorted(analysoi_dict.items()))
    
    for key, value in sorted_dict.items():
        print(key, value,sep=' : ')




# analysoi(T)
print(analysoi(T))