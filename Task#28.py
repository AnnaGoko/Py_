#Задание 26
def sum(num_a, num_b):
    if num_b == 0:
        return num_a
    else:
        return sum(num_a ^ num_b, (num_a & num_b) << 1)
    
num_a = int(input("Введите число A: "))
num_b = int(input("Введите число B: "))
print(sum(num_a, num_b))