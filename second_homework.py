#4.6.1
print("Задание 4.6.1")
import random

a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)

print((a+b+c)/3)
print()

#4.6.2
print("Задание 4.6.2")
x = 177
y = 10

a = x // y
b = x % y
print(a,b)

print()


#4.6.3
print("Задание 4.6.3")

x = float(input("Введите число: "))

print(f"{x:.{2}f}")
print(f"{x:.{0}f}")
print(str(x).rjust(11,"0"))

print()

#4.6.4
print("Задание 4.6.4")

x1 = int(input("Введите целое число: "))
x2 = 0
 
while x1 > 0:
    digit = x1 % 10
    x1 = x1 // 10
    x2 = x2 * 10
    x2 = x2 + digit  
 
print(f'Обратное число: {x2}')

print()

#4.6.5
print("Задание 4.6.5")



print()

