#Задание 22
set_n = set()
set_m = set()

size_n = int(input("Введите количество элементов первого множества: "))
size_m = int(input("Введите количество элементов второго множества: "))

print("Введите элементы первого множества:")
for i in range(size_n):
    set_n.add(int(input()))

print("Введите элементы второго множества:")
for i in range(size_m):
    set_m.add(int(input()))

print(sorted(set_n & set_m))