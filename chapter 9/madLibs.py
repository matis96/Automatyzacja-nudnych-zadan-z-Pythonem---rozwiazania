import re

fp = open('test_madLibs.txt')
text = fp.read()
fp.close()

szuk = re.compile(r'PRZYMIOTNIK|RZECZOWNIK|PRZYSLOWEK|CZASOWNIK')
x=szuk.search(text)
while x:
    word = input(f'Podaj {x.group().lower()}: ')
    text = szuk.sub(word, text, 1)
    x=szuk.search(text)
print(text)

new = open('madLibs_result.txt', 'w')
new.write(text)
new.close()
