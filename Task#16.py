size = int(input("Введите кол-во элементов в масиве:  "))
array = list(map(int, input("Введите элементы массива через пробел: ").split()))
number = int(input("Введите нужный элемент: "))
count = 0

for i in range(size):
    if array[i] == number:
        count += 1

print(count)