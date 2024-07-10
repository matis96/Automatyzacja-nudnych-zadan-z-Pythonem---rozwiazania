import re
text = ''''''       #tutaj wklej tekst z datamia

date_matches = []       #poprawne daty
month31 = ['01', '03', '05', '07', '08', '10', '12']    #miesiace po 31 dni
day = []
month = []
year = []
regData = re.compile(r'''(            # DD/MM/YYYY
    ([0][1-9]|[12][0-9]|3[01])\/      # 01-31
    (0[1-9]|1[0-2])\/                 # 01-12
    ([1|2][0-9]{3})                   # 1000-2999
    )''', re.VERBOSE)                  #regex daty 

#sprawdzanie poprawności dat
for groups in regData.findall(text):
    if int(groups[1]) <=  28:           #mniej niz 28 zawsze poprawne
        date_matches.append(groups[0])
        day.append(groups[1])
        month.append(groups[2])
        year.append(groups[3])
    elif groups[1] == '29':             #jezeli 29 to tylko luty byc moze zly
        if groups[2] != '02':
           date_matches.append(groups[0])
           day.append(groups[1])
           month.append(groups[2])
           year.append(groups[3])
        else:
            if int(groups[3])%4 == 0:       #rok przestepny
                if int(groups[3])%100!=0:
                    date_matches.append(groups[0])
                    day.append(groups[1])
                    month.append(groups[2])
                    year.append(groups[3])
                else:
                    if int(groups[3])%400 != 0:
                        continue
                    else:
                        date_matches.append(groups[0])
                        day.append(groups[1])
                        month.append(groups[2])
                        year.append(groups[3])
    elif groups[1] == '30' and groups[2] != '02':       #wykluczenie lutego
        date_matches.append(groups[0])
        day.append(groups[1])
        month.append(groups[2])
        year.append(groups[3])
    elif groups[1] == '31' and groups[2] in month31:    #miesiace, ktore maja 31 dni
        date_matches.append(groups[0])
        day.append(groups[1])
        month.append(groups[2])
        year.append(groups[3])
    else:
        continue


print(date_matches)



