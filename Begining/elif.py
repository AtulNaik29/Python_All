#WAP a no. didvisible by 2 and 3 then print divisible by both ,
# divisible by 2 print 2, divisible by 3 print 3
 num = int (input('Enter a no.:-'))
 if num%2==0 and num%3==0:
     print('It is divisible by both 2 & 3')

 elif num%2==0:
     print('It is divisible by only 2')

 elif num%3==0:
     print('It is divsible by only 3')

 else:
     print('Not divsible with any no.')