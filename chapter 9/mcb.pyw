#! python3
# mcb.pyw - Zapisuje i wczytuje do schowka fragmenty tekstu.
# Użycie: py.exe mcb.pyw save <słowo-kluczowe> — Zapis schowka wraz ze słowem kluczowym.
#         py.exe mcb.pyw <słowo-kluczowe> — Wczytanie słowa kluczowego do schowka.
#         py.exe mcb.pyw list — Wczytanie wszystkich słów kluczowych do schowka.
#         py.exe mcb.pyw delete <słowo-kluczowe> - usunięcie słowa kluczowego z bazy
#         py.exe mcb.pyw delete - Usunięcie wszystkich słów kluczowych

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')


if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':           # Zapis zawartości schowka.
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    if sys.argv[1].lower() == 'delete':         # Usunięcie słowa kluczowego
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
 i wczytanie treści.
    if sys.argv[1].lower() == 'list':           # Wyświetlenie listy słów kluczowych
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower() == 'delete':         # Usunięcie wszystkich słów kluczowych
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:               # Skopiowanie treści
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
