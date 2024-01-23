import math

#ex.1
print("hei maailma")
print(100)

#ex.2
a = 5
b = 10
c = 15
d = 20
e = 2 + a
f = (c + d)/2
g = 100
h = g / d

#ex.3

print(a+c)
print(b-c)
print(d*b)
print(d/a)
print(a%c)
print((a+b+c+d)/4)
print(c**d)

#ex.4
print((a-b)**2)
print((a+b-c)*d)
print(a+b*(c/d))

#ex.5
x = (a**2) * ((c-b)**a)
print(x)
x = (a + 2)/(b * c)
print(x)
x = ((a + b) * c)/ (b-c)
print(x)

#ex.6
teksti_1 = "Hello"
teksti_2 = "World"
teksti_3 = "3"
parametri_1 = "\n:)\n"

print("{}".format(teksti_1), end=", " )
print("{}".format(teksti_2), end="\n\n")
print("{}{}".format(teksti_3, parametri_1), end="")

#ex.7
a = "a"
b = "b"
c = "c"
d = "d"

sep_1 = "-"
sep_2 = "..."

print("1","2","3","4","5","6","7","8","9","10", sep=", ")
print("1","2","3","4","5","6","7","8","9","10", sep=sep_1)
print("{}".format(a),"{}".format(b),"{}".format(c),"{}".format(d), sep=sep_2)


#ex.8

nimi : str= "qwe"
sukunimi : str= "rty"
kaupunki : str= "asd"
postinro : int= 100
katuosoite : str= "dsa"
puhelin : str= "123456"
tunnus : int= 200

"""
a) nimi sukunimi

("Erkki Esimerkki")

b) katuosoite,postinro kaupunki 

("Jokivarsi 2,70200 Kuopio")

c) puhelin+tunnus

("012-345678+240")
"""

print("{} ".format(nimi) + "{}".format(sukunimi ))
print("{},".format(katuosoite) + "{} ".format(postinro) + "{}".format(kaupunki  ))
print("{}".format(puhelin ) + "+{}".format(tunnus))

#ex.9

print("Brian O'Malley alustaa kirjassaan: \"Suurin inspiraatio tekstille syntyi keväällä 1985, tavatessani Ed Mulliganin.\"")
print("Koodinvaihtomerkkejä ovat esimerkiksi \\t ja \\n")

#ex.10

b = 123.123123123123

print(format(b, ".2f"))
print(format(b, ".4f"))
print(format(b, ".0f"))

#ex.11
a = 23.45345
b = 2345.435345 
c = 76000000
d = -213423 
e = 567567.789789

"""
Variable a rounded to 3 decimal places
Variable b without the decimal part
Variable c (an integer) with commas for thousands
Variable d formatted as a percentage with two decimal places
Variable e formatted as a percentage without the decimal part, reserving 5 characters for the variable.
"""
print(format(a, ".3f"))
print(format(b, ".0f"))
print(format(c, "3,d"))
print(format(d, ".2%"))
print((format(e, "5.0%")))

#ex.12

#Calculate the distance of the trip in kilometers and print the following output #(excluding quotation marks):
#"Matka: 200.4 mailia 322.6 km"
#Calculate fuel consumption in gallons and liters, and print as follows:
#"Kulutus: 6.7 gallonaa 25.4 litraa"
#Calculate the cost of consumed fuel in dollars and euros, and print:
#"Kustannus: 26.7 dollaria 24.0 euroa"

matka_maileja: int = 1000
maileja_per_gallona: int = 100
polttoaine_dollari_per_gallona: int = 5

km_per_maili: int = 1609
litraa_per_gallona: int = 3785
euroa_per_dollari: int = 0.92

print("Matka: {} mailia {} km" .format(format(matka_maileja, ".1f"), format(matka_maileja * km_per_maili, ".1f")))

print("Kulutus: {} gallonaa {} litraa" .format(format(matka_maileja / maileja_per_gallona, ".1f"), format((matka_maileja / maileja_per_gallona) * litraa_per_gallona, ".1f")))

print("Kustannus: {} dollaria {} euroa" .format(format((matka_maileja / maileja_per_gallona) * polttoaine_dollari_per_gallona, ".1f"), format(((matka_maileja / maileja_per_gallona) * polttoaine_dollari_per_gallona) * euroa_per_dollari, ".1f")))

#ex.13

paivia = 700

# Laske vuodet, viikot ja päivät
vuodet = paivia // 365
jaakaus = paivia % 365
viikot = jaakaus // 7
paivat = jaakaus % 7

# Tulosta tulokset

#ex.14

leveys:int = 7.5
pituus:int = 16
syvyys:int = 3

hinta_per_m2:int = 19
saastot_per_kk:int = 225

"""Print the resulting area on its own line rounded to two decimal places, and add the label "m2" separated by a space at the end. For example, "522.52 m2" """

"""Then calculate the amount of money spent on tiling and print it on its own line, rounded to two decimal places, and add the label "eur" separated by a space at the end. For example, "252.25 eur"."""

"""Finally, calculate how many months Sampo has to save to accumulate the required money for tiling. Round up the months to the nearest whole number (see tips) and print it on its own line. Add the label "months" separated by a space at the end, for example, "25 months"."""

import math
area = (leveys * pituus) + ((leveys * syvyys) *2) + ((pituus * syvyys) * 2)
full_price = area * hinta_per_m2
print("{} m2".format(format(area, '.2f')))
print("{} eur".format(format(area * hinta_per_m2, '.2f')))
print("{} kk".format(math.ceil(full_price / saastot_per_kk)))
