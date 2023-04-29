list_three = [[0 for i in range(3)] for j in range(3)]
print(list_three)
list_three[1][1] = 3
print(list_three)

import numpy as np
# 创建一维数组
nd_one = np.array([1, 2, 3])
# 创建二维数组
nd_two = np.array([[1, 2, 3], [4, 5, 6]])

print(nd_one)
print(nd_two)
print('nd_two.shape =', nd_one.shape)
print('nd_two.shape =', nd_two.shape)

nd_two.shape = (3,)
nd_two.shape = (2, 3)

# arange() 类似Python内置函数的 range()
# arange(初始值, 终值, 步长) 不包含终值
x0 = np.arange(1, 11, 2)
print(x0)

# 创建一个 5x3 的数组
x1 = np.arange(15).reshape((5, 3))
print(x1)

# linspace()线性等分向量
# linspace(初始值, 终值, 元素个数) 包含终值
x2 = np.linspace(1, 11, 6)
print(x2)
