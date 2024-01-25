#ex.1
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