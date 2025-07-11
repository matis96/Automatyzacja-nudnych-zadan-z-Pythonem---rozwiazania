#! python3
# Import modułów i umieszczenie komentarzy opisujących przeznaczenie tego programu
import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Sprawdzenie, czy rozszerzenie pliku nie jest .png lub .jpg
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            numNonPhotoFiles += 1
            continue    # Przejscie do kolejnego pliku

        # Otworzenie pliku obrazu za pomocą modułu pillow.
        try:
            im = Image.open(os.path.join(foldername, filename))
            width, height = im.size
            # Sprawdzenie, czy szerokość i wysokość są większe niż 500.
            if width > 500 and height > 500:
                # Obraz jest wystarczająco duży, aby go uznać za zdjęcie.
                numPhotoFiles += 1
            else:
                # Obraz jest zbyt mały, aby go uznać za zdjęcie.
                numNonPhotoFiles += 1
        except:
            continue


        # Jeżeli więcej niż połowa plików to były zdjęcia, wówczas
        # należy wyświetlić bezwzględną ścieżkę dostępu tego katalogu
        if numPhotoFiles > numNonPhotoFiles:
            print(foldername)
