for i in range(2, 4):
    print(i)

list = [2, "hi", 3.9]

for n in list:
    n = 1

print(list)

for i in range(len(list)):
    list[i] = 1

print(list)