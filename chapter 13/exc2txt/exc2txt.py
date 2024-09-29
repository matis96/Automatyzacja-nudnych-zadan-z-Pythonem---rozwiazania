import openpyxl

wb = openpyxl.load_workbook('txt2exc_result.xlsx')
ws = wb.active

colMax = ws.max_column
for col in range(0, colMax):
    f = open('file'+str(col+1)+'.txt', 'w')
    for cellObj in list(ws.columns)[col]:
        if cellObj.value != None:
            f.write(str(cellObj.value))
    f.close()
