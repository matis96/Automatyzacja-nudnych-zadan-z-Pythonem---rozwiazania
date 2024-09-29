import random
guess = ''
while guess not in ('orzel', 'reszka'):
    print('Odgadnij wynik rzutu monetą! Wpisz orzel lub reszka:')
    guess = input()
toss = random.randint(0, 1) #0 oznacza reszke, natomiast 1 to orzel.
if toss == 0:
    toss = 'reszka'
else:
    toss = 'orzel'
if toss == guess:
    print('Odgadles!')
else:
    print('Nie udalo sie! Sprobuj ponownie!')
    guess = input()
    if toss == guess:
        print('Odgadles!')
    else:
        print('Nie udalo sie! Naprawde kiepsko Ci dzis idzie.')
