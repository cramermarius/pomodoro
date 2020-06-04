import time
import os
import sys

workTime = 25 # 25min
breakTime = 5 # 5min
breakTimeLong = 15 # 15min
pomoCycle = 4 # 2 hours total
breakCycle = 4 # do breakTimeLong after 4 cycles
cycleCount = 0
soundFile = "/home/mcramer/repos/pomodoro/ding.wav"
playSoundCmd = "aplay -q"

def save(output):
    f = open("/home/mcramer/repos/pomodoro/pomotimer", "w")
    f.write(output)
    f.close()

def timer(length):
    for remainTime in range(length, 0, -1):
        output = phaseType + str(remainTime)
        save(output)
        time.sleep(60)
    os.system(playSoundCmd + " " + soundFile)

os.system(playSoundCmd + " " + soundFile)
while cycleCount < pomoCycle:
    phaseType = "W"
    timer(workTime)
    cycleCount += 1

    if cycleCount % breakCycle == 0:
        phaseType = "B"
        timer(breakTimeLong)
    else:
        phaseType = "B"
        timer(breakTime)

save(" ")
