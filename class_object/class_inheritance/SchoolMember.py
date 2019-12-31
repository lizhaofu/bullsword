#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2019/12/6 17:24
# @File    : SchoolMember.py
# @Software: PyCharm
"""


class SchoolMember:

    """代表任何学校里的成员。"""

    def __init__(self, name, age):

        self.name = name

        self.age = age

        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):

        """告诉我有关我的细节。"""

        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")