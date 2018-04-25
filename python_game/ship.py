# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python game, ship.
'''

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        '''
        :param screen: 初始化飞船，并设置初始化位置
        '''
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 飞船属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''
        :return: 根据移动标志调整飞船的位置
        ：更新： 根据飞船的center值，而不是rect
        '''
        # 限定边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def center_ship(self):
        '''
        :return: 飞船居中
        '''
        self.center = self.screen_rect.centerx

    def blitme(self):
        '''
        :param self:指定位置绘制飞船
        :return:
        '''
        self.screen.blit(self.image, self.rect)
