#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

import pygame
import sys

File_backGround = 'image/sushiplate.jpg'
File_mouse = 'image/fugu.png'

def eventPost():
    CATONKEYBOARD = pygame.USEREVENT + 1
    my_event = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
    pygame.event.post(my_event)

def eventManage(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x -= 50
        elif event.key == pygame.K_RIGHT:
            x += 50
        elif event.key == pygame.K_UP:
            y -= 30
        elif event.key == pygame.K_DOWN:
            y += 30
            FullScreen = not FullScreen
            if FullScreen:
                screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((640, 480), 0, 32)

    elif event.type == pygame.MOUSEMOTION:
        x, y = pygame.mouse.get_pos()


pygame.init()

#创建一个窗口
screen = pygame.display.set_mode((640,480),0,32)
#设置窗口坐标
pygame.display.set_caption("会动的鱼")

#加载并转换图片
background = pygame.image.load(File_backGround)
mouse_cursor = pygame.image.load(File_mouse)

srcx,srcy = randint(0,639.),randint(0,469.)

color = pygame.time.Clock()
speed = 250.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #画背景
    screen.fill((0,0,0))


    time_passed = color.tick()
    time_passed_seconds = time_passed / 1000.0

    distance_moved = time_passed_seconds * speed
    srcx += distance_moved
    srcy += distance_moved
    if srcx>=639. or srcy>=469.:
        srcx, srcy = randint(0,639),randint(0,439)
    screen.blit(mouse_cursor, (srcx-mouse_cursor.get_width()/2, srcy-mouse_cursor.get_height()/2))

    pygame.display.update()