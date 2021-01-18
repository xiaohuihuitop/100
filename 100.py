people = []
for i in range(1, 31):
    people.append(i)
print(people)

die = []
for i in range(0, 15):
    die.append(0)

"""
使用 index_count 计数9次 表示第九次报数的人
index 下标 每次报数就+1 如果该下标成员已经被剔除，则再次+1 
下标再次加1后 需要重新判断 当前下标成员是否已经被剔除 如此循环
"""
die_count = 0
index = 0
index_count = 0
while die_count < 15:

    index_count += 1

    if index >= 30:
        index = 0

    i = 0
    while i < 15:
        if die[i] == people[index]:
            index += 1
            if index >= 30:
                index = 0
            i = 0
            continue  # 这里如果不提前返回 会执行 i+=1 die[0] 就无法进入判断。
        i += 1

    if index_count == 9:
        die[die_count] = people[index]
        die_count += 1
        index_count = 0

    index += 1

print(die)

# 第二种 直接取出第9位 然后将前8为分割到列表尾部 然后重新开始
print(people)

while len(people) > 15:
    print(people.pop(8), end=" ")
    for i in range(8):
        people.append(people.pop(0))

print(people)
