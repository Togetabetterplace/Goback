# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 冒泡排序。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
# for i in range(1, n):
#     data[i] = int(input())
# import requests
# import json
import numpy as np


def bubble_Sort(a, data):
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
    for i in range(0, n):
        print(data[i])


n = int(input())
data = [int(n) for n in input().split()]
bubble_Sort(n, data)

# Edmonds_Karp。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
# from collections import deque


def bfs(S_point, T_point, graph, parent):
    visited = [False] * len(graph)
    queue = []

    queue.append(S_point)
    visited[S_point] = True

    while queue:
        u = queue.pop(0)

        for index, value in enumerate(graph[u]):  # 一个访问数组下标，一个访问下标表示的内容
            if not visited[index] and value > 0:  # 如果没访问过且边的 容量！= 0
                queue.append(index)
                visited[index] = True
                parent[index] = u

    return visited[T_point]


def Edmonds_Karp(S_point, sink, graph):  # 求最大流的fork-fulkerson算法
    parent = [-1] * len(graph)  # 构建长度列表的方法
    max_flow = 0

    while bfs(S_point, sink, graph, parent):
        path_flow = float('inf')
        s = sink

        while s != S_point:
            path_flow = min(
                path_flow,
                graph[parent[s]][s])  # graph[parent[s]][s]：从s的父母到s所经过的弧的流量
            s = parent[s]  # 向上进行traverse整个路径，并更新最大流。

        max_flow += path_flow

        v = sink
        while v != S_point:
            u = parent[v]
            graph[u][v] -= path_flow  # 正向边减少流量
            graph[v][u] += path_flow  # 反向边增加流量
            v = parent[v]

    return max_flow


n = int(input("请输入节点数："))
m = int(input("请输入边数："))

graph = [[0] * n for i in range(n)]  # 二维数组邻接表建图

for i in range(m):  # 默认是0~m
    u, v, w = map(int, input("请输入边的起点、终点和权重：").split())  # (数据类型，输入。分割）
    graph[u][v] += w  # 正向边流量增加，反向边初始流量就是0

S_point = int(input("请输入源点索引："))
T_point = int(input("请输入汇点索引："))

print("最大流为：", Edmonds_Karp(S_point, T_point, graph))

# 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

# 杨辉三角
max_size = 10000
a = [[0] * max_size for i in range(max_size)]
while True:
    n = int(input())
    for i in range(n):
        a[i][0] = 1
    for i in range(1, n):
        for j in range(i + 1):
            a[i][j] = a[i - 1][j] + a[i - 1][j - 1]
    for i in range(n):
        for j in range(i + 1):
            print(a[i][j], end=" ")
        print(" ")
    print(" ")
# 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

# 爬虫复习

# if __name__ == "__main__":
#     headers = {
#         'User-Agent':
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#         'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
#     }
#     url = 'https://cn.bing.com/search?'
#     # 处理url所携带的参数：封装到字典
#     kw = input('enter keywords: ')
#     param = {'q': kw}
#     # 对指定的url发起的请求的url是携带参数的，且在请求过程中处理了参数
#     response = requests.get(url=url, params=param)
#     page_text = response.text
#     filename = kw + '.html'
#     with open(filename, 'w', encoding='utf-8') as fp:
#         fp.write(page_text)
#     print(filename, "Successfully saved!")
# if __name__ == "__main__":
#     while True:
#         post_url = 'https://fanyi.baidu.com/sug'  # 指定url
#         headers = {  # 请求头UA伪装
#             'User-Agent':
#             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#             'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
#         }
#         key_word = input('enter words that you want to translate： ')
#         if key_word == "EXIT":
#             break
#         data = {
#             'kw': key_word  # 输入的要翻译的关键字
#         }
#         response = requests.post(url=post_url, data=data,
#                                  headers=headers)  # 发送请求
#         dic_obj = response.json()  # 获取相应数据
#         fileName = key_word + '.json'
#         fp = open(fileName, 'w', encoding='utf-8')
#         json.dump(dic_obj, fp=fp, ensure_ascii=False)
#         print(".............................................................")
#         for i in range(len(dic_obj["data"])):
#             print(dic_obj['data'][i]['v'])
#         print(".............................................................")
#         print("translation ended!")

# # # 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
# # # 机器学习入门
# # import tensorflow as tf
# # import numpy as np
# # from tensorflow import keras
# # import os

# # model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# # model.compile(optimizer='sgd', loss='mean_squared_error')
# # xs = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=int)
# # ys = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024], dtype=int)
# # model.fit(xs, ys, epochs=10000)
# # print(model.predict([11]))
# # print(pow(2, 11))

# # 下载数据集
# zip_path = tf.keras.utils.get_file(
#     origin=
#     'https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
#     fname='jena_climate_2009_2016.csv.zip',
#     extract=True)
# csv_path, _ = os.path.splitext(zip_path)
# a = input()
# w = a.split()  # a.split()是临时将字符串或列表按照空格进行合并，而如果不存放到另一个列表内，则split没意义
# print(w[0])
# print(w[1])  # 使用a[i]则会出现3," ",4,使用w[i]则出现3，4
# print(w[2])  # 使用split输出时，输入不需要打空格，自动生成空格
# # import requests
# # import re

# # ns = int(input('input n: ')) ks = int(input('input k: ')) url = 'https://www.hackmath.net/en/calculator/n-choose-k'
# # data = {'kw_n': ns, 'kw_k': ks} headers = { 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;
# # x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 ''Safari/537.36 Edg/110.0.1587.63'} response =
# # requests.get(headers=headers, data=data, url=url) dic = response.text  # print(dic) print(re.findall(r'^is\s[
# # 0-9]*',dic)) filenames = 'n_choose_k' + '.html' with open(filenames, 'w', encoding='utf-8') as fp: fp.write(dic)
# # print(filenames, "Successfully saved!")

# print(re.search('W.*?$', 'hello Word'))
# search = re.search('^is\s[0-9]*', 'is 123 kkk')
# print(search)
# str1 = '1a2s3asdfa'
# mathch1 = re.search("^[0-9]", str1)
# print(mathch1)

# a = [1, 2, 3, 4, 5, 6]
# b = ['a', 'b', 'c', 'd', 'e', 'f']
# c = [2, 4, 6, 8, 10, 12]
# for i, j, k in zip(a, b, c):
#     print(i, j, k)

# 求LCS

n = int(input('input len: '))
a = np.zeros(n)
b = np.zeros(n)
res = 0
for i in range(0, n):
    a[i] = int(input())
for i in range(0, n):
    for j in range(0, i):
        if a[i] > a[j]:
            b[i] = max(b[i], b[j] + 1)
            res = max(b[i], res)
print('LCS: ', res)
