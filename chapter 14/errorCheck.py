# solution to the excercise S
import ezsheets

ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')
rows = 15000
for i in range(2, rows+1):
    if (int(ss[0].getRow(i)[0])*int(ss[0].getRow(i)[1]) != int(ss[0].getRow(i)[2])):
        break
print(i)
