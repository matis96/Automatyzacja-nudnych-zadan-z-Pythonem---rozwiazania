import openpyxl

f1 = open("plikA.txt", 'r')
f2 = open("plikB.txt", 'r')
f3 = open("plikC.txt", 'r')
files = [f1, f2, f3]

wb = openpyxl.Workbook()
ws = wb.active

j = 0
for file in files:
    j+=1
    i = 1
    for line in file.readlines():
        ws.cell(row = i, column = j).value = line
        i+=1

wb.save('txt2exc_result.xlsx')
