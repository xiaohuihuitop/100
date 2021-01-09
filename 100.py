# 3*4  是3个列表 每个列表4个元素
Test_li = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

"""
展平
"""

li = [i for row in Test_li for i in row]
print(li)

li = []
for row in Test_li:
    for i in row:
        li.append(i)

print(li)


"""
改成 4*3
"""

li = [[row[i] for row in Test_li] for i in range(4)]
print(li)

li = []
for i in range(4):
    temp_li = []
    for row in Test_li:
        temp_li.append(row[i])
    li.append(temp_li)

print(li)
