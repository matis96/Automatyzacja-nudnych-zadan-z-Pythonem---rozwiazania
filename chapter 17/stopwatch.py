#! python3
# stopwatch.py - A simple stopwatch program.

import time
import pyperclip
# import subprocess
# Display the program's instructions.
print('Press enter to begin. Afterwards, press ENTER to "click" the stopwatch.'
      ' Press Ctrl-C to quit.')
input()  # press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

f = open('laps.txt', 'w')
# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        str1 = 'Lap # ' + str(lapNum) + ':'
        str2 = str(totalTime).rjust(8) + ' ('
        str3 = str(lapTime).rjust(5)+')'
        strFinal = str1 + str2 + str3
        print(strFinal, end='')
        f.write(strFinal + '\n')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    f.close()
    laps = open('laps.txt', 'r')
    file_content = laps.read()
    pyperclip.copy(file_content)
    laps.close()
    print('\nDone.')

