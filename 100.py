for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}".format(j, i, j * i), end=' ')
    print()

print()

for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print("{}*{}={}".format(j, i, j * i), end=' ')
    print()

print()
