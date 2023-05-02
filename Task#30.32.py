#Задача 30,32
a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

progression = []
for i in range(n):
    an = a1 + i * d
    progression.append(an)

print(progression)

min_num = int(input("Введите минимальное значение: "))
max_num = int(input("Введите максимальное значение: "))

indexes = []
for i in range(len(progression)):
    if min_num <= progression[i] <= max_num:
        indexes.append(i)

print(indexes)