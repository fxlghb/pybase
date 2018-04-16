#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame

def ModuleinitScreen(title, resolution=(0,0), flags=0, depth=0):
    #pygame 初始化
    pygame.init()
    # 创建一个窗口
    screen = pygame.display.set_mode(resolution, flags, depth)
    # 设置窗口坐标
    pygame.display.set_caption(title)


def moduleOpeEvnet():
    event = pygame.event.wait()
    #pygame.event.get()
    #pygame.event.poll()

def moduleUserEvent():
    CATONKEYBOARD = pygame.USEREVENT + 1
    my_event = pygame.event.Event(CATONKEYBOARD, message="Bad cat!")
    pygame.event.post(my_event)

def moduleTest():
    ScreenSize = (640, 480)
    #pygame 初始化
    pygame.init()
    # 创建一个窗口
    screen = pygame.display.set_mode(ScreenSize)
    # 设置窗口坐标
    pygame.display.set_caption('pygame')

    font = pygame.font.SysFont('arial', 16)
    fontHight = font.get_linesize()
    eventText = []

    while True:
        event = pygame.event.wait()
        #获得事件的名称
        eventText.append(str(event))
        if(event == pygame.QUIT):
            exit()
        screen.fill((255,255,255))

        y = ScreenSize[1] - fontHight
        for text in reversed(eventText):
            screen.blit(font.render(text, True, (0,0,0)),(0,y))
            y-=fontHight
        pygame.display.update()




moduleTest()