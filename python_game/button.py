# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python game, Button.
'''
import pygame.font


class Button():
    def __init__(self, ai_settings, screen, msg):
        '''
        :param ai_settings:
        :param screen:
        :param msg: 初始化按键属性
        '''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置按钮尺寸
        self.width, self.height = 200, 50
        self.button_color = (0, 250, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 创建按钮 rect 对象
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 按钮创建
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''
        :param msg:
        :return: 将msg渲染
        '''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制按钮
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)