import winsound
import random
import time

highmin = 1200
highmax = 2000
lowmin = 200
lowmax = 400

def beep():
    freq = random.randint(440, 1440)
    dur = random.randint(300, 1000)
    winsound.Beep(freq,dur)
    time.sleep(random.randrange(0.2, 1, 0.05))


def prepare():
    print("Listen for number of beeps")
    time.sleep(1)
    print("Ready?")
    time.sleep(1)
    print("Set.")
    time.sleep(1)
    print("GO!!!")

ran = random.randint(3,8)
prepare()

for i in range(ran):
    beep()

time.sleep(0.4)
ans = int(input("How many beeps did you hear: "))

if ans == ran:
    print("Horay!")
else:
    print("Nope")