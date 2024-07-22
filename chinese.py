from collections import defaultdict

import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud

path = ('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx')

import pandas as pd
df = pd.read_excel(path) # skiprows=2，不需要跳过任何行，第一行就是表头

dic = dict()
prices = defaultdict(list)

keys = ['脑电图仪', '脑电采集','脑电采集设备', '脑电采集系统', '视频', '移动', '便携式', '数字', '导', '通道', '动态']

r = ''
for index, row in df.iterrows():
    r = r + ',' + str(row[2].strip())


for key in keys:
    jieba.add_word(key)

stops = ['和', '术', '仪']
for stop in stops:
    jieba.del_word(stop)


result = jieba.lcut(r,cut_all=False)#全模式
sentence=" ".join(result)
words = WordCloud(font_path='msyh.ttc', background_color='white').generate(sentence)


print(result)

plt.imshow(words) # 传入wordcloud对象
plt.axis('off') # 关闭坐标轴
plt.show() # 将图片展示出来