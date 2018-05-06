# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python dataView.--画廊
'''

from die import Die
import pygal
# pyagl 2.4
die_1 = Die()
die_2 = Die()
# 掷几次，存储在列表
results = []
for roll_num in range(1000):
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

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Results"
hist.y_title = "Frequency of Result"
hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual.svg')
