import cv2
import time
from time import sleep
import datetime
import os
from gpiozero import LED
import schedule
from DataUpload import *
from ImageUpload import *
import subprocess

def Iter():
    led = LED(21)
    led.on()
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 2048)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 2048)
    now = time.localtime()
    Date = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    filename = "%04d-%02d-%02d_%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)
    print('Taking picture at  ', filename)
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    if ret:
        name = '/home/test/Desktop/pictures/' + filename + '-01.png'
        USB = '/home/test/usb/pictures/' + filename + '-01.png'

        cv2.imwrite(name, frame)
        cv2.imwrite(USB, frame)

    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    if ret:
        name = '/home/test/Desktop/pictures/' + filename + '-02.png'
        USB = '/home/test/usb/pictures/' + filename + '-02.png'

        cv2.imwrite(name, frame)
        cv2.imwrite(USB, frame)

    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    if ret:
        name = '/home/test/Desktop/pictures/' + filename + '-03.png'
        USB = '/home/test/usb/pictures/' + filename + '-03.png'

        cv2.imwrite(name, frame)
        cv2.imwrite(USB, frame)

    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()

    if ret:
        name = '/home/test/Desktop/pictures/' + filename + '-04.png'
        USB = '/home/test/usb/pictures/' + filename + '-04.png'

        cv2.imwrite(name, frame)
        cv2.imwrite(USB, frame)
        
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    ret, frame = camera.read()
    
    if ret:
        name = '/home/test/Desktop/pictures/' + filename + '-05.png'
        USB = '/home/test/usb/pictures/' + filename + '-05.png'
        cv2.imwrite(name, frame)
        cv2.imwrite(USB, frame)       
    
    nameIdx = 'filename'
    SensorUpload(1, Date, 10, 5, 'N', 15, 10)
    for i in range(1, 6):
        sleep(1)
        nameIdx = (str(filename)+'-0'+ str(i)+'.png')
        ImageUpload(1, Date, nameIdx)
        sleep(1)
    camera.release()
    led.off()
    led2 = LED(12)
    print('motor on')
    led2.on()
    sleep(5)
    led.off()

print('Activated')
Iter()
print('Done')