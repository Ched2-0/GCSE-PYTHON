#e means england, s means scotland
print('Welcome to the tax calculator!')
income= float(input('How much do you earn? £'))

#english tax bands
ebasic_rate = income-12570 #allows for the 0% bound
ebasic_rate_output = ebasic_rate*0.2 #gives 20% of anything above personal allowance
ehigher_rate = income - ebasic_rate_output #allows for the 20% bound
ehigher_rate_output = ehigher_rate*0.4 #gives 40% of anything above basic rate
eadditional_rate = income - ehigher_rate_output #allows for 40% bound
eadditional_rate_output = eadditional_rate*0.45 #gives 45% of anything above higher rate

#scottish tax bands
sstarter_rate = income - 12570
sstarter_rate_output = sstarter_rate*0.19 
sbasic_rate = income - sstarter_rate_output
sbasic_rate_output = sbasic_rate*0.20
sintermediate_rate = income - sbasic_rate_output
sintermediate_rate_output = sintermediate_rate*0.21
shigher_rate = income - sintermediate_rate_output
shigher_rate_output = shigher_rate*0.41
stop_rate = income - shigher_rate
stop_rate_output = stop_rate*0.46

#ask where you live
engscot = input('Do you live in england or scotland? ')

if engscot == 'england' or engscot == 'England':
    if income < 12570:
        e = 0
        print(f'You need to pay £{e} in tax this year.')

    elif income >= 12571 and income <= 50270:
        print(f'You need to pay £{round(ebasic_rate_output, 2)} in tax this year.')

    elif income >= 50271 and income <= 150000:
        print (f'You need to pay £{round(ehigher_rate_output, 2)} in tax this year.')

    elif income > 150000:
        print(f'You need to pay £{round(eadditional_rate_output, 2)} in tax this year.')
    
    else:
        print('That is not a valid response')


elif engscot == 'scotland' or engscot == 'Scotland':
    if income < 12570:
        s = 0
        print(f'You need to pay £{s} in tax this year.')

    elif income >= 12571 and income <= 14667:
        print(f'You need to pay £{round(sstarter_rate_output, 2)} in tax this year.')

    elif income >= 14668 and income <= 25296:
        print (f'You need to pay £{round(sbasic_rate_output, 2)} in tax this year.')

    elif income >= 25297 and income <= 43662:
        print (f'You need to pay £{round(sintermediate_rate_output, 2)} in tax this year.')

    elif income >= 43663 and income <= 150000:
        print (f'You need to pay £{round(shigher_rate_output, 2)} in tax this year.')

    elif income > 150000:
        print(f'You need to pay £{round(stop_rate_output, 2)} in tax this year.')

    else:
        print('That is not a valid response')

else:
    print('That is not a valid response')