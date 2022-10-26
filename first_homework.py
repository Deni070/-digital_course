#3.6.1
name = input()
surname = input()
print(f'Hello {name} {surname}! You just delved into Python. Great start!')

#3.6.2
a = 5
b = 'H'

for i in range(a):
    print((b*i).rjust(a-1) + b + (b*i).ljust(a-1))

for i in range(a+1):
    print((b*a).center(a*2) + (b*a).center(a*6))

for i in range((a+1)//2):
    print((b*a*5).center(a*6))    

for i in range(a+1):
    print((b*a).center(a*2) + (b*a).center(a*6))    

for i in range(a):
    print(((b*(a-i-1)).rjust(a) + b + (b*(a-i-1)).ljust(a)).rjust(a*6))  

#3.6.3
a = 'hello world'
print(a.title())

#3.6.5
height = 11
width = height * 3

for stick_count in range(1, height, 2):
    print(('.|.' * stick_count).center(width, '-'))

print('WELCOME'.center(width, '-'))

for stick_count in range(height-2, 0, -2):
    print(('.|.' * stick_count).center(width, '-'))