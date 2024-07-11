import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    answers = 0
    print(prompt, end = ' ')
    start = time.time()
    for answers in range(3):
        x = input()
        if int(x) == num1*num2:
            print('Dobrze!')
            koniec = time.time()
            time.sleep(1)
            break
    if answers == 2:
        print('Zbyt wiele prób!')
        continue
    if koniec - start > 8:
        print('Czas minął!')
        continue
    correctAnswers += 1
print('Wynik: %s / %s' % (correctAnswers, numberOfQuestions))

