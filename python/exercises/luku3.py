import random

# 3. OHJELMOINNIN PERUSRAKENTEITA: Ohjelmointitehtävät jakso 2
def ex2_2():
    x = 1
    y = -1 
    z = 1
    if x > 0:
        if y > 0:
            print("x > 0 ja y > 0")

    elif z > 0:
        print("x < 0 ja z > 0")

# 3. OHJELMOINNIN PERUSRAKENTEITA: Ohjelmointitehtävät jakso 3

#ex.1
def ex3_1():
    a = 1
    b = 2   

    if a > b: 
        print('a on suurempi kuin b')
    if b > a:
        print('b on suurempi kuin a')
    if a==b:
        print('a on sama kuin b')


    for i in range(0, 100): # toistetaan 100 kertaa
        x = random.randint(1, 100)  # satunnaisluku x, väliltä 1-100

        # Toteuta tehtävänanto alle, 
        # sisennettynä tämän kommentin kanssa samalle tasalle:
        if x > 50:
            a+=1
        else:
            b+=1

#ex.2
def ex3_2():      
    for i in range(0, 100): # toistetaan 100 kertaa
        x = random.randint(1, 100)  # satunnaisluku x, väliltä 1-100

        # Toteuta tehtävänanto alle, 
        # sisennettynä tämän kommentin kanssa samalle tasalle:
        if x > 50:
            a+=1
        else:
            b+=1

#ex.3
def ex3_3():  
    asuste_kuuma = "olla alaston"
    asuste_kylma = "otta takkin"
    asuste_leuto = "vahan vaateet"
    paiva = 0
    lampotila = random.randint(-30, 30)
    # alustetaan paivan_aluste - muuttuja
    paivan_asuste = ""

    # toteuta if-elif-else lauseet
    if lampotila > 20:
        paivan_asuste = asuste_kuuma 
    elif lampotila < 0:
        paivan_asuste = asuste_kylma 
    else:
        paivan_asuste = asuste_leuto 

    # tulostetaan sääennuste ja suositeltu asuste
    # huomaa miten \ merkki jakaa print-komennon kahdelle riville
    print(paiva + 1, "päivä,", "lämpötila:", lampotila, \
        "C", "asusteeksi suositellaan", paivan_asuste)

#ex.4
def ex3_4():  
    a = 0  # kolmosia
    b = 0  # aidosti alle viitosia (<5)
    c = 0  # suurempia tai yhtä suuria kuin 3 (>=3)
    d = 0  # lukuja jotka EI ole 2 (!=2)

    # arvotaan sata satunnaislukua väliltä 1-10
    for i in range(0, 100):  # toistetaan 0:sta 100:an kierrosta
        x = random.randint(1, 10)  # satunnaisluku 1-10
        
        # TEHTÄVÄ
        # päivitä laskureita a-d tehtävänannon mukaisesti

        if x == 3:
            a+=1
        if x < 5:
            b+=1
        if x >=3:
            c+=1
        if x != 2:
            d += 1



    # tulostetaan lopputulokset
    print('kolmosia :', a)
    print('aidosti alle viitosia :', b)
    print('suurempia tai yhtä suuria kuin 3 :', c)
    print('lukuja jotka eivät ole 2 :', d)

#ex.5
def ex3_5(): 
# totuusarvot satunnaista valintaa varten
    valinta = [True, False]
    # käsitellään kymmenen olentoa
    for olento in range(0, 10):

        # arvotaan olennolle totuusarvot
        suomut = random.choice(valinta)
        jalat = random.choice(valinta)
        pyrsto = random.choice(valinta)
        print()
        print('----------------------------------------------------------------------')
        print('suomut:',suomut, end=" -")
        print('jalat:',jalat, end=" -")
        print('pyrsto:',pyrsto)
        print()
        # tulostellaan alkuhöpinät
        print('Kierros ', olento)
        print('Näemme kaukaa otuksen jolla', end = ' ')
        print('on suomut' if suomut else 'ei ole suomuja', end=', ')
        print('on jalat' if jalat else 'ei jalkoja', end=' ja jolla ')
        print('on pyrstö' if pyrsto else 'ei ole pyrstöä')
        print('ohjelmamme on sitä mieltä että kyseessä on :', end=' ')

        # TEHTÄVÄ
        # luokittele olento tehtävänannon mukaan
        # ja tee tulostus omalle rivilleen
        # Huom! sisennä vastauksesi tälle tasolle

        if (jalat and pyrsto) and (not suomut):
            print('lintu')
        elif (suomut and pyrsto) and (not jalat):
            print('kala')
        elif (jalat and suomut) and (not pyrsto):
            print('lisko')
        elif (jalat ) and ((not pyrsto) and (not suomut)):
            print('maaeläin')
        else:
            print('mytologinen eläin')
        
        print('----------------------------------------------------------------------')

#ex.6
min_lampotila = 15
max_lampotila = 25
def ex3_6(): 
    print('min lämpötila:', format(min_lampotila, '.2f') + 'C')
    print('max lämpötila:', format(max_lampotila, '.2f') + 'C')

    for x in range(0, 50): # 50 toistoa

        # arvotaan lämpötila väliltä -40 <-> +40
        lampotila = (random.random() * 2 - 1) * 40

        # TEHTÄVÄ
        # Toteuta tehtävänannon mukainen välimatkavertailu alle
        if min_lampotila < lampotila < max_lampotila:
            print('sopiva lämpötila: {} C'.format(format(lampotila, '.2f')))

#ex.7
def ex3_7(): 
    # lista korttien arvontaa varten
    kortit = ["ässä", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jätkä", "kuningatar", "kuningas"]

    for x in range(20): # 20 toistoa
        A = random.choice(kortit) # arvotaan kortti A
        B = random.choice(kortit) 

        # ei sallita ässä-ässä erikoistilannetta 
        while A == 'ässä' and B == 'ässä':
            B = random.choice(kortit)

        print('Kortit: A-', A, ' B-', B, sep='')

        # TEHTÄVÄ ALKAA TÄSTÄ
        voi_jakaa = False
        if A == B:
            voi_jakaa = True
        if A == "ässä":
            A = 11
        if A == "jätkä" or A == "kuningatar" or A == "kuningas":
            A = 10
        
        if B == "ässä":
            B = 11
        if B == "jätkä" or B == "kuningatar" or B == "kuningas":
            B = 10
        
        C = A + B
        print("{} + {} = {}".format(A,B,C))
        
        if C == 21:
            print('BLACKJACK')
        elif C < 17:
            print('nosto kannattaa')
        else:
            print('kannattaa pysyä')
        if voi_jakaa:
            print('käden voi jakaa!')

#ex.8
def ex3_8():
    vuosi = 2020
    kuukausi = -2
    is_leap = False
    päivien_lkm = 30
    Kuukaudet = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu"]
    kuukauden_nimi=""
    if 1 <= kuukausi <= 12:
        kuukauden_nimi = Kuukaudet[kuukausi-1]
        if kuukausi <= 7 and kuukausi % 2 != 0 or kuukausi >=   8 and kuukausi % 2 == 0:
           päivien_lkm = 31  
        elif kuukausi == 2:
            if vuosi % 4 == 0:
                is_leap = True
            if vuosi % 100 == 0:
                is_leap = False
                if vuosi % 400 == 0:
                    is_leap = True
            if is_leap:
                päivien_lkm = 29
            else:
                päivien_lkm = 28
        print(f'{kuukausi}/{vuosi} {kuukauden_nimi} päiviä: {päivien_lkm}')
    else:
        päivien_lkm = 0
        print(f'{kuukausi}/{vuosi} Kuukausi ei ole väliltä 1-12 päiviä: {päivien_lkm}')
#ex.9
# Round the x and y coordinates to two decimal places using this function
def ex3_9():

    kvadrantti=''
    x=-0.89
    y=12.456789
    _x = round(x,2)
    _y = round(y,2)
    print(_x, _y, sep=',', end=' ')

    if _x > 0 and _y > 0:
        kvadrantti='I'
    elif _x < 0 and _y > 0:
        kvadrantti='II'
    elif _x < 0 and _y < 0:
        kvadrantti='III'
    else:
        kvadrantti='IV'

    print(f'kvadrantti = {kvadrantti}')

ex3_9()