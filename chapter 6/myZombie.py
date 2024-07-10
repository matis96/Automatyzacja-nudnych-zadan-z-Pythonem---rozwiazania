import zombiedice, random

class MyZombie:
    def __init__(self, name):
        # Wszystkie zombie muszą mieć nazwę.
        self.name = name

    def turn(self, gameState):
        # gameState to słownik informacji o bieżącym stanie gry.
        # Możesz się zdecydować na jego zignorowanie w kodzie.

        diceRollResults = zombiedice.roll() # first roll
        # Funkcja roll() zwraca słownik, którego klucze 'brains', 'shotgun' i 'footsteps'
        # wskazują liczbę wyrzuconych ikon przedstawionych przez te klucze.
        # Klucz 'rolls' to lista krotek (kolor, ikona) zawierających
        # dokładne informacje o wyniku rzutu.
        # Przykładowa wartość zwrotna roll():
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # TEN KOD ZOMBIE ZASTĄP WŁASNYM:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()  # Ponowny rzut.
            else:
                break

class MyZombie1:
    def __init__(self, name):
        # Wszystkie zombie muszą mieć nazwę.
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        decyzja = random.randint(0, 1)
        if decyzja:
            while diceRollResults is not None:
                diceRollResults = zombiedice.roll()


class MyZombie2:
    def __init__(self, name):
        # Wszystkie zombie muszą mieć nazwę.
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        guns = 0
        while diceRollResults is not None:
            guns += diceRollResults['shotgun']
            if guns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MyZombie3:
    def __init__(self, name):
        # Wszystkie zombie muszą mieć nazwę.
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        # TEN KOD ZOMBIE ZASTĄP WŁASNYM:
        decyzja = random.randint(0,3)
        guns = 0
        for x in range(decyzja):
            guns += diceRollResults['shotgun']
            if guns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
class MyZombie4:
    def __init__(self, name):
        # Wszystkie zombie muszą mieć nazwę.
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        # TEN KOD ZOMBIE ZASTĄP WŁASNYM:
        guns = 0
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            guns += diceRollResults['shotgun']
            if brains >= guns:
                diceRollResults = zombiedice.roll()
            else:
                break
zombies = (
    #zombiedice.examples.RandomCoinFlipZombie(name='Wybrany losowo'),
    #zombiedice.examples.RollsUntilInTheLeadZombie(name='Aż do prowadzenia'),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Zatrzymanie przy 2 postrzeleniach', minShotguns=2),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Zatrzymanie przy postrzeleniu', minShotguns=1),
    MyZombie(name='Mój Bot Zombie'),
    MyZombie1(name = 'Decyzja po pierwszym rzucie'),
    MyZombie2(name = 'Do dwóch broni'),
    MyZombie3(name = '1-4, do 2 broni'),
    MyZombie4(name = 'więcej mózgów niż broni'),
    # W tym miejscu dodaj zombie innych graczy.
)

# Usuń komentarz z jednego z tych wierszy, aby uruchomić
# wersję tekstową lub graficzną w przeglądarce WWW.
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
