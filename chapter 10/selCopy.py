import os, shutil
from pathlib import Path

print('Program nie kopiuje plikow o tych samych nazwach\n' +
      'Program tworzy katalog w ' + str(Path.home()))

fileExt = input('Podaj rozszerzenie plikow: ')
tarDir = input('Podaj nazwe docelowa katalogu: ')

cwd = Path.cwd()
os.mkdir(Path.home() / tarDir)
td = Path(Path.home()/ tarDir)      #path of target directory
str_len = len(str(Path.cwd()))

for folderName, subfolders, filenames in os.walk(cwd):
    flag = False
    currentPath = Path(folderName)
    for file in currentPath.glob(f'*.{fileExt}'):       #check if Path contains extension
        flag = True
    if flag:
        print('Aktualny folder: .\\' + cwd.name + str(currentPath)[str_len:])   #pokazuje przegladany folder
        path = str(td) + '\\' + cwd.name + str(currentPath)[str_len:]
        os.makedirs(path)
        for file in currentPath.glob(f'*.{fileExt}'):
            print(file.name)
            shutil.copy(file, Path(path) / file.name)

k = input('Nacisnij cos by zakonczyc ')
