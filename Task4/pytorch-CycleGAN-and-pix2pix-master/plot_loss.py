import re

import matplotlib.pyplot as plt
import numpy as np

def plot(dir):
    loss_log_path="checkpoints/"+dir+"/loss_log.txt"
    content=""
    with open(loss_log_path, "r", encoding="utf-8") as file:
        content = file.read()
    pattern = r"(.*?("
    result = re.findall(pattern, content)
    print(result)

    y = [1, 2, 3, 4]  # 4组数据
    y1 = [e + 1 for e in y]
    y2 = [e + 2 for e in y]
    y3 = [e + 3 for e in y]
    plt.plot(y, "b.-")  # 没有x参数
    plt.plot(y1, "ro--")  # r：红色，o：圆圈，--：短线连接起来
    plt.plot(y2, "kx-.")  # k：黑色，x：x字符，-.：点和线
    plt.plot(y3, "c*:")  # c：蓝绿色，*：*字符，:：点组成的线
    plt.savefig("demo3.png")

if __name__ == '__main__':
    loss_log_path="checkpoints/"+"shuimo_cyclegan"+"/loss_log.txt"
    content=""
    with open(loss_log_path, "r", encoding="utf-8") as file:
        content = file.read()
    matches = re.findall(r'(?<=G_A: )(.*?)(?= )', content)
    matches= list(map(float, matches))
    arr = np.arange(1, len(matches)+1)

    plt.plot(arr,matches,'b.')
    plt.grid(True)
    plt.show()
    print(matches)