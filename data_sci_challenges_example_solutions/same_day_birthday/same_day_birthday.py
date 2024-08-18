'''
If you were to bet your data sci honor (not money) on the following: 'At least two people in a group have their birthday on the same day of year',
at least how many people should be in the group for this bet to be worthwhile?

'''

# probability = factorial(365) / factorial(365−n)
# So, the total number of possible birthday combinations if each person could be born on any of the 365 days without restriction / the number of ways to assign unique birthdays to n people
def probability_of_same_day_birthday_in_group_of_n(n):
   product1 = product2 = 1
   for i in range(0, n):
       # product1: 365 raised to the power of n (i.e., 365 ** n)
       product1 *= 365
        # product2: is the product of (365 * 364 * ... * (365 - (n - 1))) 
       product2 *= (365 - i)
   return 1 - product2/ product1


for n in range(1, 50):
    probability = probability_of_same_day_birthday_in_group_of_n(n)
    if probability > 0.5:
        print(f'if there are at least {n} people in the group, the probability of at least two people in a group having their birthday on the same day of year is {probability:.2f}')
        print(f'So, once there are at least {n} people in the group, the probability of winning the bet is > 0.5')
        break

print(f'{probability_of_same_day_birthday_in_group_of_n(n-1)=:.2f} at {n-1=}')
print(f'{probability_of_same_day_birthday_in_group_of_n(n)=:.2f} at {n=}')
print(f'{probability_of_same_day_birthday_in_group_of_n(50)=:.2f}')
print(f'{probability_of_same_day_birthday_in_group_of_n(100)=:.7f}')
# in a group of 100 people the probability of at least two people in a group have their birthday on the same day of year is > 99%
print(f'{probability_of_same_day_birthday_in_group_of_n(365)=:.2f}')