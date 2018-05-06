# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python dataView.--Little APP
'''
# 图像处理
from PIL import Image
# 命令行处理
import argparse


# 命令行处理参数
# 1.构建 ArgumentParser对象
parser = argparse.ArgumentParser()
# 2.添加参数
parser.add_argument('file')                            # 输入文件
parser.add_argument('-o', '--output')                  # 输出文件
parser.add_argument('--width', type=int, default=80)   # 输出字符宽度
parser.add_argument('--height', type=int, default=80)  # 输出字符高度
# 3.解析参数
args = parser.parse_args()

# 创建Image 对象
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 构建字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")


# 将256 灰度映射到对应的字符
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gary = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gary/unit)]

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)
    # 输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
