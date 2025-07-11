#Auto unsubscriber

import imapclient
import datetime
import pyzmail
import webbrowser
import bs4

today = datetime.date.today()
week_ago = today - datetime.timedelta(days=7)
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('#Mail', '#password ')
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search([u'SINCE', week_ago])
rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
# print(UIDs)
messages = []
for x in UIDs:
    message = pyzmail.PyzMessage.factory(rawMessages[x][b'BODY[]'])
    messages.append(message)

raw_links = []
for message in messages:
    soup = bs4.BeautifulSoup(message.html_part.get_payload().
                             decode(message.html_part.charset), 'html.parser')
    link = soup.find_all("a", string="unsubscribe")
    if link:
        raw_links.append(link)

for link in raw_links:
    soup = bs4.BeautifulSoup(str(link), 'html.parser')
    page = soup.a['href']
    webbrowser.open(page)


