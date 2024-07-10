# Write your code here :-)
import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Kod tworzący listę 100 wartości 'orzel' lub 'reszka'
    wynik = []
    for i in range(100):
        wynik.append(random.randint(0, 1))
    #Kod sprawdzający, czy lista zawiera serię szećiu wartości 'orzeł' lub 'reszka'
    k = 2
    for i in range(100):
        if k == wynik[i]:
            numOfReps += 1
        else:
            numOfReps = 1
        k = wynik[i]
        if numOfReps == 6:
            numOfReps = 0
            numberOfStreaks += 1
    print('Prawdopodobieństwo wystąpienia serii: %s%%' % (numberOfStreaks / 100))
    numberOfStreaks = 0
