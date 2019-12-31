#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2019/12/6 17:35
# @File    : main.py
# @Software: PyCharm
"""
from class_object.class_inheritance.Student import Student
from class_object.class_inheritance.Teacher import Teacher

t = Teacher('Mrs. Shrividya', 40, 30000)

s = Student('Swaroop', 25, 75)

# 打印一行空白行

print()

members = [t, s]

for member in members:

    # 对全体师生工作

    member.tell()


points = [{'x': 2, 'y': 3},

            {'x': 4, 'y': 1}]

points.sort(key=lambda i: i['y'])

print(points)