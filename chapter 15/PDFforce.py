import PyPDF2
f = open("dictionary.txt", 'r')
pdfReader = PyPDF2.PdfReader(open('encrypted.pdf', 'rb'))
for x in f:
    print('Przetwarzane haslo to: ' + x[:-1])
    if pdfReader.decrypt(x[:-1]):
        print('Haslo to: ' + x[:-1])
        break
    if pdfReader.decrypt(x[:-1].lower()):
        print('Haslo to: ' + x[:-1].lower())
        break
