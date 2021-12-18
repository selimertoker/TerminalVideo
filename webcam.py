
from os import system, name
from PIL import Image
import cv2
import time
import os
def clearScreen():

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def printascii(pxl):
    clearScreen()
    char=""
    frame=""
    for y in range(480):
        if not y%8==0: continue
        for x in range(640):
            if not x%4==0: continue
            bright=pxl[y,639-x,0]*4
            if bright<=0:
                char=" "
            elif bright<=50:
                char="."
            elif bright<=100:
                char="'"
            elif bright<=150:
                char="^"
            elif bright<=200:
                char='"'
            elif bright<=250:
                char=":"
            elif bright<=300:
                char="<"
            elif bright<=350:
                char="+"
            elif bright<=400:
                char="t"
            elif bright<=450:
                char="n"
            elif bright<=500:
                char="X"
            elif bright<=550:
                char="C"
            elif bright<=600:
                char="m"
            elif bright<=650:
                char="o"
            elif bright<=700:
                char="$"
            elif bright<=750:
                char="@"
            frame=frame+char
        frame=frame+"\n"
    print(frame)
vid = cv2.VideoCapture(0)

while True:
    time.sleep(0.1)
    frame = vid.read()[1]
    printascii(frame)

vid.release()
cv2.destroyAllWindows()

