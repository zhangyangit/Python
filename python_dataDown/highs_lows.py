# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python dataView.--datadownload
'''

import csv
from matplotlib import pyplot as plt
from datetime import datetime

#filename = 'sitka_weather_07-2014.csv'
#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    # 分析文件头
    header_row = next(reader)

    # 打印文件头及其位置 enumerate : 获取元素索引及其值
    for index, colum_header in enumerate(header_row):
        print(index, colum_header)

    dates, highs, lows = [], [], []
    for row in reader:
        # 将日期转化为指定格式
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # 绘制 图像
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='red', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # 设置格式
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=24)
    plt.tick_params(axis='b oth', which='major', labelsize=16)
    plt.show()


