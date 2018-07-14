# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- Machine Learning
'''
import numpy as np
import matplotlib.pyplot as plt
# 读取输入数据
## 定义存储输入数据数组
x, y = [], []
## 遍历数据集，获取样本
for sample in open('../_Data/prices.txt', 'r'):
## ',’分隔数据
    _x, _y = sample.split(',')
    x.append(float(_x))
    y.append(float(_y))
# 转化数据
## 转化成 Numpy 数组
x, y = np.array(x), np.array(y)
## 标准化
x = (x - x.mean()) / x.std()
# 输出图像
plt.figure()
plt.scatter(x, y, c='g', s=6)
plt.show()

# 在(-2, 4) 空间上画100个点做基础
x0 = np.linspace(-2, 4, 100)
# 利用Numpy 定义训练并返回多项式回归模型
# deg 参数代表 n ,及多项式次数
# 返回模型是能够根据输入，预测输出y
def get_model(deg):
    return lambda input_x=x0: np.polyval(np.polyfit(x, y, deg), input_x)

# 根据参数n, 输入x,y 返回对应的损失
def get_cost(deg, input_x, input_y):
    return 0.5 * ((get_model(deg)(input_x) - input_y) ** 2).sum()

# 定义测试参数集 并根据它进行试验
test_set = (1, 4, 10)
for d in test_set:
    print(get_cost(d, x, y))

# 画出图形
plt.scatter(x, y, c='g', s=20)
for d in test_set:
    plt.plot(x0, get_model(d)(), label="degree = {}".format(d))

plt.xlim(-2, 4)
plt.ylim(1e5, 8e5)
plt.legend()
plt.show()