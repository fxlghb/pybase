#!/usr/bin/env python
# -*- coding: utf-8 -*-
#test surface module
from random import randint
import pygame

def rangePosColor():
    rangeColor = (randint(0,255),randint(0,255),randint(0,255))

    for x in range(100):
        randPos = (randint(0,639), randint(0,479))
        screen.set_at(randPos, rangeColor)


pygame.init()
screen = pygame.display.set_mode((640,480))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    rangePosColor()
    pygame.display.update()