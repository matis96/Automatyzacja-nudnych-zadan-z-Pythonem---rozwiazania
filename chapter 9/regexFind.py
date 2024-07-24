import re
from pathlib import Path

p = Path.cwd()
pattern = input('Podaj wyrazenie regularne do wyszukania: ')
regexToFind = re.compile(pattern)

list1 = list(p.glob('*.txt'))
for i in range(len(list1)):
    fp = open(list1[i])
    text = fp.readlines()
    for j in range(len(text)):
        match = regexToFind.search(text[j])
        if match:
            print(text[j])
    fp.close()
