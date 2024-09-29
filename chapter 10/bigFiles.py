import os
from pathlib import Path

cwd = Path.cwd()

for folderName, subfolders, filenames in os.walk(cwd):
    for filename in filenames:
        size = os.path.getsize(Path(folderName) / filename)
        if size > 100E6:
            print(Path(folderName) / filename)
            print(str(size) + ' bytes')

input('Nacisnij cos by zakonczyc: ')
