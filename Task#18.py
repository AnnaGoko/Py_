size = int(input("Введите кол-во элементов в масиве:  "))
array = list(map(int, input("Введите элементы массива через пробел: ").split()))
number = int(input("Введите нужный элемент"))

closest_number = array[0]

for num in array:
    if abs(num - number) < abs(closest_number - number):
        closest_number = num

print(closest_number)