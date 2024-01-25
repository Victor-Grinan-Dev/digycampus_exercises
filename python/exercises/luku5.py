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
def toisto_tulostus(teksti, n):
    for i in range(n):
        print(teksti)
        
def suurin_neljasta(a, b, c, d):
    return max(a, b, c, d)
    
def pienenna(luku, raja, askel):
    while luku > raja:
        luku -= askel
    return luku

#ex.7
def semi_major_axis(a, b):
    return (b+a)/2
    
def standard_grav_parameter(x):
    global G
    return G*x

def orbital_period(m, rmin, rmax):
   return (2 * math.pi) * (math.sqrt(pow(semi_major_axis(rmin, rmax),3)/standard_grav_parameter(m)))

# print(semi_major_axis(15,2))
# print(semi_major_axis(69816900000,46001200000), 'm')

#ex.8
def piirra( side_y:int, side_x:int, hollow:bool):
    if not hollow:
        for _ in range(side_x):
            for _ in range(side_y):
                print('O', end='')
            print()
    else:
        for x in range(side_x):
            for y in range(side_y):
                if y == 0 or x == 0 or y ==side_y-1 or x==side_x-1:
                    print('O', end='')
                else:
                    print('   ', end='')#In the exercise you need 3 spaces, in console only 1
            print()

leveys = 5
korkeus = 10
ontto = True

print('Arvot:')
print('leveys:',leveys)
print('korkeus:',korkeus)
print('Ontto:',ontto)

piirra(leveys,korkeus,ontto)

leveys = 4
korkeus = 4
ontto = True

print('Arvot:')
print('leveys:',leveys)
print('korkeus:',korkeus)
print('Ontto:',ontto)

piirra(leveys,korkeus,ontto)