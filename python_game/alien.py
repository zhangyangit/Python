# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python game, alien.
'''

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''
    表示外星人单体
    '''
    def __init__(self, ai_settings, screen):
        '''
        :param ai_settings: 设置，初始化外星人的位置
        :param screen:
        '''
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载外星人图像
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # 设置外星人出现的坐标
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储
        self.x = float(self.rect.x)

    def blitme(self):
        '''
        :param self:指定位置创建Alien
        :return:
        '''
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''
        :return:边缘检测
        '''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        '''
        :return: 移动外星人
        '''
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x
