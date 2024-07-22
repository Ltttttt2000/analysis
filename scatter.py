#-*- coding: utf-8 -*-

from collections import defaultdict

path = ('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx')

import pandas as pd
df = pd.read_excel(path) # skiprows=2，不需要跳过任何行，第一行就是表头

dic = dict()
prices = defaultdict(list)
mans = defaultdict(list)

keys = ['脑电图仪', '脑电采集','脑电采集设备', '脑电采集系统', '视频', '移动', '便携式', '数字', '导', '通道', '动态']
for key in keys:
    dic[key] = 0


for index, row in df.iterrows():
    hospital = row[0]
    date = row[1]
    formatted_date = date.strftime("%Y-%m")

    if pd.isna(row[3]) is False:
        manufacture = str(row[3])
    else:
        manufacture = '空'

    if pd.isna(row[4]) is False:
        price = row[4]
    else:
        price = 0

    name = str(row[2])

    for word in keys:
        if word in name:
            dic[word] += 1
            if price != 0:
                prices[word].append(price)
            if manufacture != '空':
                mans[word].append(manufacture)

'''词频图（自己选的几个词）'''
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# # 生成词云图
# words = WordCloud(font_path='msyh.ttc', background_color='white').generate_from_frequencies(dic)
# # 展示词云图
# plt.imshow(words, interpolation='bilinear')
# plt.axis('off')
# plt.show()



print(prices['脑电图仪'])
print(prices)


'''设备金额和关键词的关系图'''
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号


y = []
for key in keys:
    y.append(prices[key])

print(len(y))
for xe, ye in zip(keys, y):
    print(xe,ye)
    plt.scatter([xe] * len(ye), ye)

# plt.xticks([1, 2])
# plt.axes().set_xticklabels(['cat1', 'cat2'])

plt.title('设备关键词和金额的关系')
plt.xlabel('关键词')
plt.ylabel('金额')
plt.show()
# plt.savefig('t.png')
