def fun(parameter_fish):
    for i in range(5):
        if (parameter_fish - 1) % 5 == 0:
            parameter_fish = (parameter_fish - 1) / 5 * 4
        else:
            return False
    return True


fish = 1
while not fun(fish):
    fish += 1

print(fish)
