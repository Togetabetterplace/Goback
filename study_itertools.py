import itertools
from itertools import combinations

# ..............................................................................
for i in itertools.count(1100, 23):
    print(i)
    if i > 2220:
        break
# ..............................................................................
lens = 0
for i in itertools.cycle("abcd"):
    if lens < 10:
        print(i)  # 具有无限的输出，可以按ctrl+c来停止。
        lens += 1
    else:
        break
# ..............................................................................
for i in itertools.product([1, 2, 3], [4, 5, 6]):
    print(i)
# ..............................................................................
iters = ['a', 'b', 'c']
for c in combinations(iters, 2):
    print(c)
# ..............................................................................
for i in itertools.permutations('abcdefgh', 6):
    print(i)
# ..............................................................................
for i in itertools.accumulate([0, 1, 0, 1, 1, 2, 3, 5]):
    print(i)
for i in itertools.accumulate([2, 1, 4, 3, 5], max):  # 其中max可以替换为其他函数
    print(i)
