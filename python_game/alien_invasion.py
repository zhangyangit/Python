# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python game.
'''

import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from scoreboard import Scoreboard
from button import Button
from game_stats import GameStats
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏，并创建screen对象
    pygame.init()
    # 初始化游戏设置
    ai_settings = Settings()
    # 创建 surface 对象
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 设置 窗口标题
    pygame.display.set_caption("Alien Invasion")
    # 创建按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个存储统计信息的实例
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    # 创建一个子弹数组
    bullets = Group()
    # 创建与个外星人组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # begin the loop of the game
    while True:
        # 响应按键和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 更新飞船位置
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()