# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python dataView.--散点图
'''

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# 图标标题，增加标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
# 可图标记
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')