# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python dataView.--折线图
'''

import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth=5)
# 图标标题，增加标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
# 可图标记
plt.tick_params(axis='both', labelsize=14)
plt.show()

