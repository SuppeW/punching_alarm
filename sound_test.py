import pygame
import random

sounds = ["chickencoop.mp3","where is my team.mp3","whaaat.mp3","goingtobed.mp3"]
soundslen = len(sounds)
from random import randint
randnum = randint(0,soundslen-1)

print(randnum)

pygame.mixer.init()
pygame.mixer.music.load(sounds[randnum])
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
