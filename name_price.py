path = ('C:\\Users\\Lenovo\\Downloads\\医院原始招标信息.xlsx')

import pandas as pd
from pymysql import NULL

df = pd.read_excel(path) # skiprows=2，不需要跳过任何行，第一行就是表头
from collections import defaultdict
dic = defaultdict(list)

# Out:defaultdict(<class 'list'>, {'a': [1, 2, 3]})

for index, row in df.iterrows():

    hospital = row[0]
    dic[index].append(hospital)

    date = row[1]
    formatted_date = date.strftime("%Y-%m")
    dic[index].append(formatted_date)

    device_name = str(row[2])
    dic[index].append(device_name)

    if pd.isna(row[3]) is False:
        manufacture = str(row[3])
    else:
        manufacture = '空'
    dic[index].append(manufacture)

    if pd.isna(row[4]) is False:
        price = row[4]
    else:
        price = 0
    dic[index].append(price)

    if pd.isna(row[5]) is False:
        channel_count = int(row[5])
    else:
        channel_count = 0
    dic[index].append(channel_count)



print(dic[0])
for key in dic:
    print(dic[key])