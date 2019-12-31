#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2019/12/6 17:15
# @File    : main.py
# @Software: PyCharm
"""
from class_object.variable.Robot import Robot

droid1 = Robot("R2-D2")

droid1.say_hi()

Robot.how_many()

droid2 = Robot("C-3PO")

droid2.say_hi()

Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")

droid1.die()

droid2.die()

Robot.how_many()