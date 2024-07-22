from collections import defaultdict

path = ('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx')

import pandas as pd
df = pd.read_excel(path) # skiprows=2，不需要跳过任何行，第一行就是表头

dic = dict()
prices = defaultdict(list)

keys = ['脑电图仪', '脑电采集','脑电采集设备', '脑电采集系统', '视频', '移动', '便携式', '数字', '导', '通道', '动态']
for key in keys:
    dic[key] = 0
print(dic)

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



print(dic)
print(prices)

import matplotlib.pyplot as plt

# 数据
brain_wave_data = [50.0, 49.9, 39.0, 123.0, 188.0, 29.9, 184.6, 14.15, 188.0, 29.9, 79.5, 8.95, 45.76, 27.96, 62.8, 49.0, 49.0, 49.0, 38.0, 49.0, 18.0, 54.0, 30.0, 177.5, 38.4, 32.0, 38.6, 128.0, 33.8, 8.0, 40.0, 150.0, 38.97, 63.8, 37.0, 22.8]
video_data = [49.9, 39.0, 44.8, 29.9, 29.9, 33.95, 45.76, 27.96, 62.8, 44.7, 49.0, 110.0, 17.92, 65.0, 43.9, 18.0, 54.0, 42.0, 49.5, 29.8, 38.6, 63.8, 44.0, 60.0]

# 截取较长的列表以匹配较短的列表
min_length = min(len(brain_wave_data), len(video_data))
brain_wave_data = brain_wave_data[:min_length]
video_data = video_data[:min_length]

# 创建一个图形
fig, ax = plt.subplots(figsize=(10, 8))

# 脑电图仪数据的散点图

ax.scatter(len(dic['脑电图仪']), dic['脑电图仪'], color='blue', label='脑电图仪')

# 视频数据的散点图
# ax.scatter(range(50), dic['脑电采集设备'], color='green', label='视频')

# 设置标题和标签
ax.set_title('Scatter Plot of Brain Wave Data and Video Data')
ax.set_xlabel('Index')
ax.set_ylabel('Value')

# 添加网格和图例
ax.grid(True)
ax.legend()

# 显示图形
plt.show()


# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# # 生成词云图
# words = WordCloud(font_path='msyh.ttc', background_color='white').generate_from_frequencies(dic)
# # 展示词云图
# plt.imshow(words, interpolation='bilinear')
# plt.axis('off')
# plt.show()