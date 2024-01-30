
text = "Hello World!"
text2 = 'hELLO wORLD!'
text3 = 'Griñán' 
text4 = 'hello\tworld' 
text5 = 'hello {}{}' 
text6 = '{greeting} {subject}'
text7 = 'hello123'
text8 = 'hello 123'
text9 = 'hello123!'
chiness_text = '诶必西'

#1: capitalize()
print(text.capitalize())

#2: casefold()
### to compare string without caring of uppercases or lowercases
print(text.casefold() == text2.casefold())

#3: center()
#places the string in the center of those many characters surrounded by specified char
print(text.center(20, '*'))

#4: count()
print(text.count('l'))

#5: encode()
print(text3.encode(encoding='UTF-8', errors='strict'))

#6: endswith()
print(text.endswith('d!'))
print(text.endswith(('!', '?')))#checks either or

#7: expandtabs()
print(text4.expandtabs(10))

#8: find()
print(text.find('w'))
print(text.find('World'))

#9: format()
print(text5.format('World','!'))
print(text6.format(greeting='Hello', subject='World!'))

#10: format_map()
coords = {'greeting':'Hello', 'subject': 'World!'}
print(text6.format_map(coords))

#11: index()
print(text.index('or'))

#12: isalnum()
print(text.isalnum())
print(text7.isalnum())
print(text8.isalnum())
print(text9.isalnum())

#13: isalpha()
print(text.isalpha())
print(text3.isalpha())

#14: isascii()
print(text.isascii())
print(text2.isascii())
print(text3.isascii())


#15: isdecimal() 
#if a string is decimal then is digit and numeric
print('123'.isdecimal())
print('abc'.isdecimal())
print('①②③④'.isdecimal())
print('⒈⒉⒊'.isdecimal())
print('㊀㊁㊂'.isdecimal())

#16: isdigit()
# if a string is digit then is also numeric
print('123'.isdigit())
print('abc'.isdigit())
print('①②③④'.isdigit())
print('⒈⒉⒊'.isdigit())
print('㊀㊁㊂'.isdigit())

#17: isnumeric()
print('123'.isnumeric())
print('abc'.isnumeric())
print('①②③④'.isnumeric())
print('⒈⒉⒊'.isnumeric())
print('㊀㊁㊂'.isnumeric())

#18: isidentifier() if you can name a variable 
print('hello-world'.isidentifier())
print('hello_world'.isidentifier())

#19: islower()
print(text.islower)

#20: isprintable() true if no scape characters
print('hello\nworld'.isprintable())

#21: isspace() 
print(' '.isspace())

#22: istitle() chec first letter of each word be capital
print(text.istitle())

#23: isupper()
print(text.isupper())

#24: join()
print('-'.join(['1', 'abc', text]))

#25: ljust()
print(text.ljust(20, '_'))

#26: lower()
print(text.lower())

#27: lstrip()
print(text.lstrip('Hello '))

'👋''🌎'

#28 & 29: maketrans() & translate()
table = text.maketrans('H', '👋')
print(text.translate(table))
table = text.maketrans({'H':'👋', 'W':'🌎'})
print(text.translate(table))

#30: partition() #splits the string in 3 parts by the targeted string portion
print(text.partition('lo'))

#31: removeprefix()
print('Wazzap!'.removeprefix('Waz'))

#32: removesuffix()
print('Wazzap!'.removesuffix('zap!'))

#33: replace()
print(text.replace('Hello', 'Greetings'))

#34: rfind() opposit to find()
print(text.rfind('l'))

#35: rindex() opposit to index()
print(text.rindex('l'))

#36: rjust() opposit to ljust()
print(text.rjust(20, '_'))

#37: rpartition() opposit to partition()
print(text.rpartition('l'))

#38: rsplit() & 39: split()
print(text.rsplit('l'))
print(text.split('l'))
print(text.rsplit('l', maxsplit=1))
print(text.split('l', maxsplit=1))

#40: rstrip()
print('Hello world Hello'.rstrip('Hello'))

#41: splitlines()
print('Hello world\nHello\nPeople'.splitlines(keepends=True))
print('Hello world\nHello\nPeople'.splitlines(keepends=False))

#42: startwith()
print(text.startswith('H'))

#43: strip()
print(text.strip('Hell'))
print(text.strip('ld!'))
print('  Hello World! \n'.strip())

#44: swapcase()
print(text.swapcase())
print(text2.swapcase())

#45: title()
print(text2.title())

#46: upper()
print(text.upper())

#47: zfill() (zero fill)
print(text.zfill(20))