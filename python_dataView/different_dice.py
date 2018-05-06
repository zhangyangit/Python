# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python dataView.--画廊
'''

from die import Die
import pygal

# 创建D6+D10
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling  D6+D10 50000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"
hist.add('D6+D10', frequencies)
hist.render_to_file('die_visual_D6_D10.svg')
