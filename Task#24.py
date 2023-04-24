#Задание 24
bush_number = int(input("Введите кол-во кустов: "))
berry_number = list(map(int, input("Введите кол-во ягод на кусте: ").split()))
max_berry = 0

for i in range(bush_number):
    counter_ = berry_number[i] + berry_number[(i-1)%bush_number] + berry_number[(i+1)%bush_number]
    if counter_ > max_berry:
        max_berry = counter_

print(max_berry)