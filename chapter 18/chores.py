import random
import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('#mail', '#password ')    #Fill your password and mail here
chores = ['pozmywac naczynia', 'posprzatac lazienke', 'odkurzyc dom', 'wyprowadzic psa']
mails = ['#address1', '#address1',
         '#address1', '#address1']  

for x in range(len(chores)):
    randomChore = random.choice(chores)
    chores.remove(randomChore)
    smtpObj.sendmail('#MailRecipient', mails[x],
                     'Subject: zadanie na dzis\n{randomChore}')
