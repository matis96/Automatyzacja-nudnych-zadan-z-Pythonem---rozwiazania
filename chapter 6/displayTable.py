# Write your code here :-)
tableData = [['jabłka', 'pomarańcze', 'wiśnie', 'banany'],
             ['Alicja', 'Bartek', 'Celina', 'Dawid'],
             ['psy', 'koty', 'łosie', 'gęsi']]

def printTable(table):
    Row = len(table[0])  #Liczba rzędów
    Col = len(table)     #Liczba kolumn
    colWidths = [0] * Col    #szerokość kolumn
    for x in range(Col):
        max = len(table[x][0])
        for y in range(1, Row):
            if max < len(table[x][y]):
                max = len(table[x][y])
        colWidths[x] = max
    for x in range(Row):
        for y in range(Col):
            print(table[y][x].rjust(colWidths[y]), end=' ')
        print()

printTable(tableData)
