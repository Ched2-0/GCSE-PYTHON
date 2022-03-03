a=3 #allows for the extra £3 for the first journey
dist=int(input('Please enter your distance (km): '))
pas=int(input('How many passengers? '))
d = dist*2 #charge £2 for every km
if pas < 5:
    print(f'Your total is £{d-2+a}. Thank you for your service!')

elif pas >= 5:
    b = d-2+a
    c = d/2 #allows for the adding of 50% to the charge
    print(f'Your total is £{b+c}. Thank you for your service!')