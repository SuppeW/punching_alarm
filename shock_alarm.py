import pygame
import time
import random
import RPi.GPIO as GPIO

shock_pin = 17
sounds = ["chickencoop.mp3","where is my team.mp3","whaaat.mp3", "goindgtobed.mp3"]
soundslen = len(sounds)
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setup(shock_pin, GPIO.IN)

pygame.mixer.init()
def callback(shock_pin):
        if GPIO.input(shock_pin):
            print ("alarm time")
            pygame.mixer.music.load(sounds[randint(0,soundslen)])
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue


        else:
            print ("alarm time")

GPIO.add_event_detect(shock_pin, GPIO.BOTH, bouncetime=5000)
GPIO.add_event_callback(shock_pin, callback)

while True:
    time.sleep(5000)
