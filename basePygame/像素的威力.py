#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640,480),0,24)
all_colors = pygame.Surface((4096,4096),depth=24)

for r in    range(256):
    print(r+1, 'out of 256')
    x = r&0xf*256
    y = (r>>4)*256
    for g in range(256):
        for b in range(256):
            all_colors.set_at((x+g, y+b),(r,g,b))

pygame.image.save(all_colors, 'allcolor.bmp')



