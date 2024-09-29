import ezsheets

ss = ezsheets.Spreadsheet('')   # Fill with spreadsheet id 
sheet = ss[0]
mails = sheet.getColumn(3)
i = 1
while mails[i] != '':
    print(mails[i])
    i+=1
