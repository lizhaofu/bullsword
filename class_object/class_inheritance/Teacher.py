#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2019/12/6 17:27
# @File    : Teacher.py
# @Software: PyCharm
"""
from class_object.class_inheritance.SchoolMember import SchoolMember


class Teacher(SchoolMember):

        """代表一位老师。"""

        def __init__(self, name, age, salary):

            SchoolMember.__init__(self, name, age)

            self.salary = salary

            print('(Initialized Teacher: {})'.format(self.name))

        def tell(self):

            SchoolMember.tell(self)

            print('Salary: "{:d}"'.format(self.salary))