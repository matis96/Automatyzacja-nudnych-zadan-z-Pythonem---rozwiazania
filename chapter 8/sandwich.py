import pyinputplus as pyip

def Menu():
    print('Oto nasz cennik.')
    print('Chleb pszenny - 10 zł\nChleb biały - 8 zł\nChleb na zakwasie - 12 zł')
    print('/*********************/')
    print('kurczak - 10 zł\nindyk - 8 zł\nszynka - 12 zł\ntofu - 11 zł')
    print('/*********************/')
    print('ser cheddar - 6 zł\nser szwajcarki - 8 zł\nmozzarella - 7 zł')
    print('/*********************/')
    print('majonez - 2 zł, musztarda - 2 zł, sałata - 3 zł, pomidor - 4 zł')
    print('/*********************/')
def kanapka(chleb, bialko, ser = 'nie'):
    suma = 0
    if chleb == 'pszenny':
        suma += 10
    elif chleb == 'bialy':
        suma += 8
    else:
        suma += 12
    if bialko == 'kurczak':
        suma += 10
    elif bialko == 'indyk':
        suma += 8
    elif bialko == 'szynka':
        suma += 12
    else:
        suma +=11
    if ser == 'cheddar':
        suma += 6
    elif ser == 'szwajcarski':
        suma += 8
    elif ser == 'mozzarella':
        suma += 7
    else:
        return suma
    return suma

Menu()
chleb = pyip.inputMenu(['pszenny', 'bialy', 'na zakwasie'],
                        prompt = 'Prosze wybrac rodzaj chleba: \n', numbered = True)
bialko = pyip.inputMenu(['kurczak', 'indyk', 'szynka', 'tofu'],
                        prompt = 'Prosze wybrac dodatek #1: \n', numbered = True)
ser = pyip.inputYesNo(prompt = 'Czy dodac ser?\n',
                        yesVal = 'tak', noVal = 'nie')
if ser == 'tak':
    dodSer = pyip.inputMenu(['cheddar', 'szwajcarski', 'mozzarella'],
                        prompt = 'Jaki dodatkowy ser? \n', numbered = True)
    cena = kanapka(chleb, bialko, dodSer)
else:
    cena = kanapka(chleb, bialko)
maj = pyip.inputYesNo(prompt = 'Czy dodac majonez?\n',
                        yesVal = 'tak', noVal = 'nie')
if maj == 'tak':
    cena += 2
musz = pyip.inputYesNo(prompt = 'Czy dodac musztardę?\n',
                        yesVal = 'tak', noVal = 'nie')
if musz == 'tak':
    cena += 2
salata = pyip.inputYesNo(prompt = 'Czy dodac sałatę?\n',
                        yesVal = 'tak', noVal = 'nie')
if salata == 'tak':
    cena += 3
pomidor = pyip.inputYesNo(prompt = 'Czy dodac pomidor?\n',
                        yesVal = 'tak', noVal = 'nie')
if pomidor == 'tak':
    cena += 4
zamowienie = pyip.inputInt(prompt = 'Ile takich kanapek? \n', min = 1)
cena *= zamowienie

print('Gotowe! Prosze oto twoje kanapki. Do zapłaty: %s' %cena)
