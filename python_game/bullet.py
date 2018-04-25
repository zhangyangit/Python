# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python game, bullet.
'''

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''
    对飞船发射的子弹的管理类
    '''
    def __init__(self, ai_settings, screen, ship):
        '''
        :param ai_settings: s设置项
        :param screen: 窗口对象
        :param ship: 飞船对象
        '''
        super(Bullet, self).__init__()
        self.screen = screen
        # 在(0,0) 创建子弹矩形，然后设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # 存储小数表示的子弹位置
        self.y = float(self.rect.y)
        # 其他设置
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''
        :return: 向上移动子弹
        '''
        # 更新子弹位置，小数值
        self.y -= self.speed_factor
        # 更新子弹位置
        self.rect.y = self.y

    def draw_bullet(self):
        '''
        :return: 在屏幕绘制子弹
        '''
        pygame.draw.rect(self.screen, self.color, self.rect)
