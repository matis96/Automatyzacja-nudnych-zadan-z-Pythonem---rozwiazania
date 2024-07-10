def collatz(number):
    number = int(number)
    if number % 2 == 0:
        k = number // 2
        print(k)
        return k
    else:
        k = 3 * number + 1
        print(k)
        return k


print("Podaj liczbę:")
x = input()
try:
    wynik = collatz(x)
    while wynik != 1:
        wynik = collatz(wynik)

except ValueError:
    print("Proszę wpisać liczbę całkowitą")
