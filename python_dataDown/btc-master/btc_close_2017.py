from __future__ import (absolute_import, division, print_function, unicode_literals)
from urllib.request import urlopen
import json
import requests
import pygal
import math
from itertools import groupby

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)
# 读取数据
req = response.read()
# 写入文件
with open('btc_close_2017_urlib.json', 'wb') as f:
    f.write(req)
# 加载json格式
file_urllib = json.loads(req)
print(file_urllib)


json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# 写入文件 属性“wb”会出现类型错误
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)
# 加载json格式
file_requests = req.json()

print(file_urllib == file_requests)

# 将数据加载到列表
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# 打印信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    print("{} is month {} week {} , {}, the close price is {} RMB".format(date, month, week, weekday, close))

# 创建列表，绘图
dates, months, weeks, weekdays, closes = [], [], [], [], []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', closes)
line_chart.render_to_file('收盘价折线图.svg')

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
closes_log = [math.log10(_) for _ in closes]
line_chart.add('收盘价', closes_log)
line_chart.render_to_file('收盘价对数变换折线图.svg')


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list)/len(y_list)])

    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], '收盘价月日均值', '月日均值')
line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week], closes[1:idx_week], '收盘价周日均值', '周日均值')
line_chart_week

idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int, closes[1:idx_week], '收盘价星期均值', '星期均值')
line_chart_weekday.x_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
line_chart_weekday.render_to_file('收盘价星期均值.svg')

with open('收盘价Dashboard.html','w', encoding='utf-8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><metacharset="utf-8"></head><body>\n')
    for svg in ['收盘价折线图.svg', '收盘价对数变换折线图.svg', '收盘价月日均值.svg', '收盘价周日均值.svg', '收盘价星期均值.svg']:
        html_file.write(' <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body></html>')