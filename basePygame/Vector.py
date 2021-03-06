#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    #向量大小
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    #单位向量
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x/=magnitude
        self.y/=magnitude
    #向量加减法
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y+other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)
    @classmethod
    def from_points(cls, P1, P2):
        return cls(P2[0]-P1[0], P2[1]-P1[1])

A = (10.0, 20.0)
B = (20.0, 30.0)
AB = Vector2.from_points(A,B)
print(AB)