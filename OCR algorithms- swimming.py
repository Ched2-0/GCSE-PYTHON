a = 3.50 #default price
e = a * 0.3 #multiplier for age 13-15ys
b = a * 0.2 #multiplier for age 16-17ys
c = a * 0.4 #multiplier for age 50-99ys
f = 0 #while loop variable
m = 0#  -
n = 0#  - 
v = 0#  -     variables to calculate total
x = 0#  -
z = 0#  -
total = 0# -

print('Welcome to the swim zone! Would you like to book a session?')
d = int(input('How many people are you booking for? '))
while f < d: #keeps the while loop going for the number of people booking
    f = f+1 #adds 1 to the f counter to ensure the loop stops when it reaches d

    age = int(input('Please enter your age: '))
    if age >= 13 and age < 16:
        print(f'It will cost you £{a -e}')
        m = a - e

    elif age >= 16 and age < 18:
        print(f'It will cost you £{a - b}')
        n = a - b
        
    elif age >= 50 and age < 100:
        print(f'It will cost you £{a - c}')
        v = a - c

    elif age >= 0 and age < 13: #added because a classmate was being pedantic
        print(f'It will cost you £{a}')
        x = a

    elif age >= 18 and age < 50:
        print(f'It will cost you £{a}')
        z = a

    elif age >= 100:
        print('You are too old!')

    else:
        print('invalid syntax')
    
    total = total + m + n + v + x + z #adds the total every time the while loop loops

print(f'Your combined total is £{total}')