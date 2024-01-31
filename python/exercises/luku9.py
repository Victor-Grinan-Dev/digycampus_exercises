import pickle
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