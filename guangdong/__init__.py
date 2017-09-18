import csv
import re
import matplotlib.pyplot as plt
from huapingtu import huabingtu


'''
print('等级景区预览')
print('test')
print('统计各等级景区数量')
'''
path = './input/等级景区.csv'
data = []
map = {}

with open(path,'r', encoding='GBK') as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        data.append(line)

del data[0]

for list in data:
    # print(list[1], '->', list[4])
    dengji = list[4]
    # 先把整个字符串的规则抽象出来，让后括号选取想要的部分
    m = re.match('.*?(A.*A)', dengji)
    if m is not None:
        # print(m.group())
        # print(m.group(1))
        dengji_new = m.group(1)
        list[4] = dengji_new

    print(list[1], '->', list[4])
    if list[4] in map:
        map[list[4]] = map[list[4]] + 1

    else:
        map[list[4]] = 1


huabingtu(map)
