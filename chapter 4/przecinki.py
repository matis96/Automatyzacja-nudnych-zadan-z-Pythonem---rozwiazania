def text(workList):
    for i in range(len(workList)-2):
        print(workList[i], end=', ')
    print(workList[-2], end=' ')
    print('i ' + workList[-1])

spam = ['jabłka', 'banany', 'tofu', 'koty']
text(spam)
