# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python password
'''

import re


# 特征
NUMBER = re.compile(r'[0-9]')
LOWER_CASE = re.compile(r'[a-z]')
UPPER_CASE = re.compile(r'[A-Z]')
OTHERS = re.compile(r'[^0-9A-Za-z]')


class Strength(object):
    '''密码的属性：
    1.有效性
    2.强度
    3.提示信息
    '''

    def __init__(self, vaild, strength, message):
        self.valid = vaild
        self.strength = strength
        self.message = message

    def __repr__(self):
        return self.strength

    def __str__(self):
        return self.message

    def __bool__(self):
        return self.valid


class Password(object):
    '''密码强度判断：
    1.长度
    2.复杂度
    # 3. 常用列表
    '''

    # 强度标志
    TERRIBLE = 0
    SIMAPLE = 1
    MEDIUM = 2
    STRONG = 3

    # staticmethod 这个方式是从实例调用还是从类调用，它都用第一个参数把类传递过来.
    # 判断是否为随便在键盘上打的
    @staticmethod
    def is_regular(input):
        regular = ''.join(['qwertyuiop', 'asdfghjkl', 'zxcvbnm'])
        return input in regular or input[::-1] in regular

    # 判断是否为等间距的打的
    @staticmethod
    def is_by_step(input):
        delta = ord(input[1]) - ord(input[0])
        for i in range(2, len(input)):
            if ord(input[i]) - ord(input[i-1]) != delta:
                return False
        return True

    def __call__(self, input, min_length=6, min_type=3, level=STRONG):
        if len(input) < min_length:
            return Strength(False, "terrible", "密码太弱，不合格")
        if self.is_regular(input) or self.is_by_step(input):
            return Strength(False, "simple", "密码有规则，不合格")

        type = 0
        if NUMBER.search(input):
            type += 1
        if LOWER_CASE.search(input):
            type += 1
        if UPPER_CASE.search(input):
            type += 1
        if OTHERS.search(input):
            type += 1

        if type < 2:
            return Strength(False, "simple", "密码复杂度小于3，不合格")

        return Strength(True, "strong", "密码强度足，合格")

password = Password()
