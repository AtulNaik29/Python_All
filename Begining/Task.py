age =int(input('Enter the Age :-'))
if age<15 and age>60:
    print('Not allowed inside the Bus')
elif age>=15 and age<=25:
    print('price will 10')
elif age>=25 and age<=45:
    print('price will be 20')
elif age>=45 and age<=60:
    print('price will 30')
else:
    print('not in the list')