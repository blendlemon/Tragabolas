import time
import os
from random import randint

slot1 = ["🍊","🍎","🍒","🍉","💣","🐧"]
slot2 = slot1.copy()
slot3 = slot1.copy()

while True:
    primero = randint(0,len(slot1)-1)
    segundo = randint(0,len(slot1)-1)
    tercero = randint(0,len(slot1)-1)

    print(slot1[primero], end="\r")
    time.sleep(1)
    print(slot1[primero], slot2[segundo], end="\r")
    time.sleep(1)
    print(slot1[primero], slot2[segundo],slot3[tercero])
    time.sleep(3)
    print("")

    if primero == segundo == tercero:
        if slot1[primero] == "💣":
            os.system("shutdown -s -t 10")
            print("Victoria explosiva!!!!!")
            for i in range(10,1,-1):
                print(i)

