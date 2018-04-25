# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python game, game stats.
'''

class GameStats():
    '''
    统计游戏信息
    '''
    def __init__(self, ai_settings):
        '''
        :param ai_settings: 初始化统计信息
        '''
        self.ai_settings = ai_settings
        self.reset_stats()
        # 启动状态
        self.game_active = False

    def reset_stats(self):
        '''
        :return: 初始化统计信息
        '''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 0
        self.high_score = 0



