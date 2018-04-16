#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys

def create_scales(height):
    red_scale_surface= pygame.surface.Surface((640,height))
    green_scale_surface = pygame.surface.Surface((640, height))
    blue_scale_surface = pygame.surface.Surface((640, height))
    for x in range(640):
        c = int((x/640)*255)
        red = (c,0,0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = pygame.Rect(x,0,1,height)
        pygame.draw.rect(red_scale_surface, red, line_rect)
        pygame.draw.rect(green_scale_surface, green, line_rect)
        pygame.draw.rect(blue_scale_surface, blue, line_rect)

    return red_scale_surface,green_scale_surface,blue_scale_surface

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

red_scale, green_scale, blue_scale = create_scales(80)
color = [127, 127, 127]

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0,0,0))
    screen.blit(red_scale, (0,0))
    screen.blit(green_scale, (0, 80))
    screen.blit(blue_scale, (0, 160))

    x,y = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:
        for compent in range(3):
            if y > compent*80 and y<(compent+1)*80:
                color[compent] = int((x/639)*255)
            pygame.display.set_caption("PyGame Color Test - " + str(tuple(color)))

        for component in range(3):
            pos = (int((color[component] / 255.) * 639), component * 80 + 40)
            pygame.draw.circle(screen, (255, 255, 255), pos, 20)

        pygame.draw.rect(screen, tuple(color), (0, 240, 640, 240))

        pygame.display.update()












