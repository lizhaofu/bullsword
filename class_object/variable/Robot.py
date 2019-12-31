#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2019/12/6 17:12
# @File    : Robot.py
# @Software: PyCharm
"""


class Robot:

    """表示有一个带有名字的机器人。"""

    # 一个类变量，用来计数机器人的数量

    population = 0

    def __init__(self, name):

        """初始化数据"""

        self.name = name

        print("(Initializing {})".format(self.name))

        # 当有人被创建时，机器人

        # 将会增加人口数量

        Robot.population += 1

    def die(self):

        """我挂了。"""

        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:

            print("{} was the last one.".format(self.name))

        else:

            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):

        """来自机器人的诚挚问候

        没问题，你做得到。"""

        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):

        """打印出当前的人口数量"""

        print("We have {:d} robots.".format(cls.population))