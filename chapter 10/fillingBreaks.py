from pathlib import Path
import shutil, os
prefix = input('Podaj prefix pliku: ')
ext = input('Podaj rozszerzenie pliku: ')
p = Path.cwd()
i = 0
for file in p.glob(f'{prefix}*.{ext}'):
    i += 1
    newFile = f'{prefix}' + str(i) + f'.{ext}'
    newPath = os.path.join(p, newFile)
    shutil.move(file, newFile)
