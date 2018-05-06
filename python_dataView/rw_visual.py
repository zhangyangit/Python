# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python dataView.--随机漫步
'''
import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    # 创建RandomWalk 实例
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 设置 窗口尺寸
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,cmap=plt.cm.Blues, edgecolors='none', s=1)
    # 突出起点终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break