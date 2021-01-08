print("\n------1:普通-------")

num = int(input("请问需要几项 7:"))

val_1 = 0
val_2 = 1

if num < 3:
    if num == 0:
        print("ERR")
    elif num == 1:
        print("{}".format(val_1), end=" ")
    else:
        print("{} {}".format(val_1, val_2), end=" ")
else:
    print("{} {}".format(val_1, val_2), end=" ")
    for i in range(3, num + 1):
        val_2 = val_1 + val_2
        val_1 = val_2 - val_1
        print("{}".format(val_2), end=" ")

print("\n------2:列表-------")

list_l = [0, 1]

if num < 3:
    if num == 0:
        print("ERR")
    elif num == 1:
        print("{}".format(val_1), end=" ")
    else:
        print("{} {}".format(val_1, val_2), end=" ")
else:
    for i in range(0, num - 2):
        s = list_l[i] + list_l[i + 1]
        list_l.append(s)
    print(list_l)

print("\n------3:递归-------")


def fibonacci(parameter_num):
    if parameter_num == 1:
        return 0
    elif parameter_num == 2:
        return 1
    else:
        return fibonacci(parameter_num - 1) + fibonacci(parameter_num - 2)


if num < 1:
    print("ERR")
else:
    for i in range(1, num + 1):
        print(fibonacci(i), end=" ")

print("\n------4:迭代器-------")


class FibIterator(object):

    def __init__(self, items):
        self.val1 = 0
        self.val2 = 1
        self.items = items
        self.current = 0  # 记录当前位置

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.items:
            return_val = self.val1
            # self.val2 = self.val2 + self.val1
            # self.val1 = self.val2 - self.val1
            self.val1, self.val2 = self.val2, self.val1 + self.val2
            self.current += 1
            return return_val
        else:
            raise StopIteration


class MyFib(object):
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return FibIterator(self.items)


Test_Fib = MyFib(7)

for i in Test_Fib:
    print(i, end=" ")

print("\n--------------")

Test_Iter = iter(Test_Fib)
print(next(Test_Iter))
print(next(Test_Iter))
print(next(Test_Iter))
print(next(Test_Iter))
print(next(Test_Iter))
print(next(Test_Iter))
print(next(Test_Iter))

print("\n-------5:生成器------")


def Generator(parameter_num):
    current = 0
    val1 = 0
    val2 = 1
    while True:
        if current < parameter_num:
            yield val1
            current += 1
            val1, val2 = val2, val1 + val2
        else:
            return


Test_Generator = Generator(7)
# Test_List = list(Test_Generator)
# print(Test_List)

print(next(Test_Generator))
print(next(Test_Generator))
print(next(Test_Generator))
print(next(Test_Generator))
print(next(Test_Generator))
print(next(Test_Generator))
print(next(Test_Generator))
