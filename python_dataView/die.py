# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python dataView.--画廊
'''

from random import randint

class Die():
    '''骰子类'''
    def __init__(self, num_sides=6):
        '''骰子 6 面'''
        self.num_sides = num_sides

    def roll(self):
        '''返回 1-6 之间的随机数'''
        return randint(1, self.num_sides)