# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# 0到1标准正态分布
arr1 = np.random.randn(3, 3)
# 0到1均匀分布
arr2 = np.random.rand(3, 3)
# 均匀分布的随机数（浮点数），前两个参数表示随机数的范围，第三个表示生成随机数的个数
arr3 = np.random.uniform(0, 10, 2)
# 均匀分布的随机数（整数），前两个参数表示随机数的范围，第三个表示生成随机数的个数
arr4 = np.random.randint(0, 10, 3)
print(f'arr1 : {arr1}\narr2 : {arr2}\narr3 : {arr3}\narr4 : {arr4}')
# out :
# arr1 : [[-0.31637952 -0.08258995  1.43866984]
#  [-0.11216775  0.43881134  0.11745847]
#  [-1.1770306  -0.97657465  2.2368878 ]]
# arr2 : [[0.16350611 0.4467384  0.9465067 ]
#  [0.1882318  0.40261184 0.93577701]
#  [0.56243911 0.69179631 0.83407725]]
# arr3 : [4.41402883 6.03259052]
# arr4 : [9 7 7]
# 未初始化的数组
arr1 = np.empty((2, 3))
# 数组元素以 0 来填充
arr2 = np.zeros((2, 3))
# 数组元素以 1 来填充
arr3 = np.ones((2, 3))
# 数组以指定的数来进行填充，这里举例3
arr4 = np.full((2, 3), 3)
# 生成单位，对角线上元素为 1，其他为0
arr5 = np.eye(2)
# 二维矩阵输出矩阵对角线的元素，一维矩阵形成一个以一维数组为对角线元素的矩阵
arr6 = np.diag(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
arr7 = np.arange(1, 100, 2)

arr8 = np.eye(10)
arr9 = np.zeros((5, 5, 5))  # 可扩展到n维
print(arr7)
print(arr8)
print(arr9)
print(arr8[5][5])
for i in range(0, 5, 3):
    for j in range(0, 5, 3):
        arr8[i][j] += 100
for i in range(4, 6):
    for j in range(4, 6):
        arr8[i][j] += 102
for i in range(6, 10, 2):  # 遍历时，第三个输入的数为步长
    for j in range(6, 10, 2):
        arr8[i][j] += 108
print(arr8)

# 数据处理
df = pd.read_csv(r'C:\Users\21550\Desktop\py_project\learning\data_APMCM.csv', encoding = 'gbk')
print(df.head(10))  # 查看前几行
print(df.describe((0, 1)))  # 查看摘要
# df['AverageTemperature'].hist(bins = 1000) # 不知道为什么这个用不了

# x = np.random.randint(0, 100, 100)  # 生成【0-100】之间的100个数据,即 数据集
x = df['AverageTemperature']
bins = np.arange(-100, 100, 0.1)  # 设置连续的边界值，即直方图的分布区间[0,10],[10,20]...
# 直方图会进行统计各个区间的数值
plt.hist(x, bins, color = 'purple', alpha = 0.5)  # alpha设置透明度，0为完全透明

plt.xlabel('temperature')
plt.ylabel('num_T')
plt.xlim(-50, 50)  # 设置x轴分布范围
plt.show()

print('=====================================================')
print(df.apply(lambda y: sum(x.isnull()), axis = 0))

df.fillna(df.median(), inplace = True)
# # data为缺失的数据集
# imp = IterativeImputer(max_iter = 10, random_state = 0)
# imp.fit(df)
# print(np.round(imp.transform(df)))
print(df.apply(lambda y: sum(x.isnull()), axis = 0))


# 对数组进行高级索引
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)