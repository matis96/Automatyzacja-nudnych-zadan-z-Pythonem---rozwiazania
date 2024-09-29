import sys, openpyxl
N = int(sys.argv[1])
M = int(sys.argv[2])
source_name = sys.argv[3]

source_wb = openpyxl.load_workbook(source_name)
source_ws = source_wb.active
dest_wb = openpyxl.Workbook()
dest_ws = dest_wb.active

for rowCellObj in source_ws:
    for cellObj in rowCellObj:
        if cellObj.row<N:
            dest_ws.cell(row = cellObj.row, column = cellObj.column).value = cellObj.value
        else:
            dest_ws.cell(row = cellObj.row+M, column = cellObj.column).value = cellObj.value

dest_wb.save(source_name)

