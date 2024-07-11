import re

def passEvaluation(password):
    haslo = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}')
    if haslo.search(password):
        print('Silne haslo')
    else:
        print('Słabe hasło. Hasło powinno zawierać min 8 znaków, małą oraz dużą literę i min. jedną cyfrę')

passEvaluation('')      #check password
