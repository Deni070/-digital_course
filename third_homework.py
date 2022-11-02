#5.6.1
print("Задание 5.6.1")
a = int(input("Введи целое число: "))

if (a % 3 == 0) and (a % 5 == 0):
    print("Fizz Buzz")
elif a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("Buzz")
else:
    print(a)
print()

#5.6.2
print("Задание 5.6.2")

x = int(input("Введи целое число: "))

if x % 2 != 0:
    print("Плохо")

elif (x > 2 and x < 5) and (x % 2 == 0):
    print('Неплохо')

elif (x > 6 and x < 20) and (x % 2 == 0):
    print('Так себе')

elif (x > 20) and (x % 2 == 0):
    print("Отлично")

print()


#5.6.3
print("Задание 5.6.3")

a= []
x = int(input())

for i in range(1, x+1):
    a += [str(i)]
    if x <= 0:
        break

print("".join(a))

print()

#5.6.4
print("Задание 5.6.4")

a = input('Введите текст: ')
def find_upper_letter(s):
    result = ""
    for i in s:
        if i.isupper():
            result += i
    return result
 
 
print(find_upper_letter(a))


print()

#5.6.5
print("Задание 5.6.5")
a = input()
def words_in_row (words) :
    count = 0
    for w in words.split() :
        if w.isalpha() :
            count += 1
            if count == 3 :
               return True
        else :
            count = 0

    return False

print(words_in_row(a))

print()

#5.6.6
print("Задание 5.6.6")

a = str(input("Введите список: "))

def left_join(words):
    b = ''
    words = a.replace('right','left')
    n = b.join(words)
    return n

print(left_join(a))

print()