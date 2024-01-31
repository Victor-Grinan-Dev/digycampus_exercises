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

print(morseksi("Morse code"))