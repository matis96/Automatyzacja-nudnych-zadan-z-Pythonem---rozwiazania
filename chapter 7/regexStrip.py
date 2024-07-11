import re

def regex_strip(text, chars2remove=''):
    if chars2remove=='':
        pattern = re.compile(r'^\s+|\s+$')
    else:
        chars2remove = re.escape(chars2remove)
        pattern = re.compile(f'^[{chars2remove}]+|[{chars2remove}]+$')

    return re.sub(pattern, '', text)

spam ='     Witaj, świecie      '
spam = regex_strip(spam)
print(spam)

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam = regex_strip(spam, 'ampS')
print(spam)
