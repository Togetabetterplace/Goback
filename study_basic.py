# # 打印乘法表
# if __name__ == '__main__':
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             print(i, '*', j, '=', i * j, end = '   ')
#         print()
#
# # 统计1~100的和
# if __name__ == '__main__':
#     sums = 0
#     for i in range(1, 101):
#         sums += i
#     print(sums)
#
# # 输入数组
# if __name__ == '__main__':
#     a = input()
#     b = a.split('*')  # a.split()默认按空格分开
#     print(b)
#     print(b[3])
#
# # 环型序列
# if __name__ == '__main__':
#     n = int(input())
#     while n != 0:
#         s = input()
#         lens = len(s)
#         p = s
#         for i in range(0, lens):
#             d = s[0]
#             s = s[1:]
#             s = s + d
#             # print(s,'00')
#             if p > s:
#                 p = s  # print(s, '11')
#         print(p)
#
# # pipi的变形课
# import numpy as np
#
# start = ord('b') - ord('a')
# end = ord('m') - ord('a')
# flags = 0  # 全局变量
#
#
# def dfs(b1, data):
#     if b1 == end:
#         print('Yes.')
#         global flags  # 修改全局变量
#         flags += 1
#         return
#     for im in range(0, 27):
#         if data[b1][im] == 1:
#             dfs(im, data)
#     return
#
#
# if __name__ == '__main__':
#     s = '&'
#     a = np.zeros((27, 27), dtype = int)  # 写二维数组要(n,m)，多加一层括号
#     flags = 0
#     while s != '0':
#         s = input()
#         lens = len(s)  # 注意不是.len()，而是len()
#         p = s[0]
#         q = s[lens - 1]  # ord(a)是a的ascii码
#         if p != '0' and q != '0':
#             a[ord(p) - ord('a')][ord(q) - ord('a')] = 1
#     flags = 0
#     for i in range(0, 27):
#         if a[start][i] == 1:
#             dfs(i, a)
#     if flags == 0:
#         print('No.')
#
#
# def factorial(x):
#     if x == -1:
#         return "do away"
#     elif x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
#
# def falling_factorial(ns, ks):
#     return factorial(ns) / (factorial(ns - ks))
#     # return n * falling_factorial(n-1,k-1)
#
# num = int(input())
# print(factorial(num))
# k = int(input())
# print(falling_factorial(num, k))

# d = dict()
# d["jefferson"] = "Chris"
# print(d["jefferson"])
# print(d)
import numpy as np


def wait():
    for i in range(1, 10000):
        if i % 100 == 0:
            print("waiting...")


if __name__ == "__main__":

    Max = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]])
    Allocation = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]])
    Need = Max - Allocation
    # print(Need)
    Available = np.array([3, 3, 2])
    Request = []
    for i in range(0, 5):
        Request.append(input().split())
    for i in range(0, 5):
        for j in range(0, 3):
            Request[i][j] = int(Request[i][j])

    print(Request)
    k = 0
    safeQueue = []
    while k != 5:
        for i in range(0, 5):
            for j in range(0, 3):
                if Request[i][j] <= Need[i][j]:
                    if Request[i][j] <= Available[j]:
                        Available = Available - Request[i]
                        Allocation[i, j] = Allocation[i, j] + Request[i][j]
                        Need[i][j] = Need[i, j] - Request[i][j]
                    else:
                        wait()
                else:
                    print("error!!!")
            flagl = 0
            for j in range(0, 5):
                for m in range(0, 3):
                    if Available[m] < Need[i][m]:
                        flagl = 1
                if flagl == 0:
                    safeQueue.append(i)
                    k += 1
                    Available = Available + Request[i]
                    break
