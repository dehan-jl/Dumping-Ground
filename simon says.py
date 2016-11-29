import winsound
import random
import time

###
# time in ms
shortmin = 200
shortmax = 800
longmin = 1400
longmax = 2000
# freq in Hz
lowmin = 200
lowmax = 400
highmin = 1200
highmax = 2000
###

###
# types shortlow - shorthigh - longlow - longhigh
# types     0    -     1     -    2    -    4
###
types = ["shortlow", "shorthigh", "longlow", "longmax"]
def beep(type):
    if type == types[0]: #shortlow
        dur = random.randrand()
    elif type == types[1]: #shorthigh
        dur =
    elif type == types[2]: #longlow
        dur
    elif type == types{3}: #longmax
        dur
    time.sleep(random.randrange(200, 1000, 50)/1000)  # randrange gives ms, then convert to seconds for time.sleep


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
    beep(types[1])

time.sleep(0.4)
ans = int(input("How many beeps did you hear: "))

if ans == ran:
    print("Horay!")
else:
    print("Nope")