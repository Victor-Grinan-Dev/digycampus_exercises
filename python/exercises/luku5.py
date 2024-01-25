#ex.1
import math
import statistics


rahamaara = 10.123123123
def muotoile_euroiksi(amount):
    euros = format(amount, '.2f')
    euros += '€'
    return euros

# print(muotoile_euroiksi(rahamaara))


#ex.2
def summa(a, b, c, d, e):
    return a + b + c + d + e
    
def suurin(a, b, c):
    suurin = a
    if b > suurin:
        suurin = b
    if c > suurin:
        suurin = c
    return suurin

def etaisyys(a, b):
    alempi = a
    suurin = b
    if b < alempi:
        alempi = b
        suurin = a
    return suurin - alempi

#ex.3

VAKIO_KIIHTYVYYS = 9.81
kappaleen_nopeus = 0
kuljettu_matka = 0
aika = 6
#176.58 

def matka(t):
    global kuljettu_matka 
    kuljettu_matka = (kuljettu_matka + (kappaleen_nopeus * t)) + ( 1/2 *( VAKIO_KIIHTYVYYS * (t * t)))

# matka(aika)
# print('Kappale on kulkenut nyt yhteensä:',kuljettu_matka,'metriä.')
kappaleen_nopeus = 15 
kuljettu_matka = 2
#268.58000000000004 

# matka(aika) 
# print('Kappale on kulkenut nyt yhteensä:',kuljettu_matka,'metriä.')


#ex.4
def summa_ja_keskiarvo(a, b):
    summa = a+b
    keskiarvo = statistics.mean([a,b])
    return summa, keskiarvo


def potenssit(a):
    return tuple([a**i for i in range(1, 6)])

# a,b = summa_ja_keskiarvo(5,10)
# print(a, b)
# print(potenssit(24.656))

#ex.5
def floor_rect_area(x,y):
    return math.floor(x*y)

def ceil_rect_area(x,y):
    return math.ceil(x*y)

#ex.6