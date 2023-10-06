# Enter

name = input('Whats is your name? ')
print('Hello,', name)

# Numbers

x = int(input('Provide number x '))
y = int(input('Provide number y '))
print( '1 - addition, 2 - subtraction, 3 - divide, 4 - multiplication ')
action = int(input('Provide action '))

# Solution

if(action == 1):
    print(x + y)
if(action == 2):
    print(x - y)
if(action == 3):
    print(x / y)
if(action == 4):
    print(x * y)