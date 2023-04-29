import numpy as np


class MyClass:
    """myfirst class"""
    class_count = 1;

    def __init__(self, name, data):
        self.name = name
        self.data = data
        MyClass.class_count += 1
        return

    def display_class(self, cnt):
        print("The class name is : ", self.name)
        for i in cnt:
            print("data[", i, "]-------->", self.data)
            self.data *= self.data
        return


MC = MyClass('Class1', 4028)
print(MC.name)
cnt = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=int)
MC.display_class(cnt)  # 注意：形参进入后为迭代器，那么传入参数也尽量是迭代器
