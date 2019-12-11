
def Combination(n,r):
    from math import factorial
    return factorial(n)/(factorial(r)* factorial(n-r))
def Probability(total_numbers,total_drawn,pool_numbers,drawn_numbers):
    '''
    Total_numbers - total numbers in the game
    Total_drawn - drawn numbers from the total pool
    Pool_numbers - total numbers in the pool for the study 
                    i.e 'even'
    Drawn_numbers - numbers drawn from the pool
    '''
    from math import factorial

    total = factorial(total_numbers)/(factorial(total_drawn)* factorial(total_numbers-total_drawn))
    pool = factorial(pool_numbers)/(factorial(drawn_numbers)* factorial(pool_numbers-drawn_numbers))

    return pool/total

def Groups(number):
    '''
    Function to divide total numbers into 4 groups.
    First group:
        low,even
    Second group:
        low, odd
    Third group:
        high,even
    Fourth group:
        high odd
    '''
    import numpy as np
    interger = (number)/2
    pool = np.arange(1,number+1)    # Generate pool values based on input
    group_a =pool[0:int(interger)]  # Lower end of the pool
    group_b = pool[int(interger):]  # High end of the pool
    group_c = []                    # Lower end; even numbers
    group_d = []                    # Lower end; odd numbers
    group_e = []                    # High end; even number
    group_f = []                    # High end; odd numbers

    for i in group_a:
        if i % 2 == 0:
            group_c.append(i)
        else:
            group_d.append(i)
    
    for i in group_b:
        if i % 2 == 0 :
            group_e.append(i)
        else:
            group_f.append(i)
    return group_c,group_d,group_e,group_f

def HighLow(numbers):
    '''
    Function to devide the range of numbers 
    Outputs, number of high  & number of low

    '''
    if numbers %2 == 0 :
        high_numbers = numbers/2
        low_numbers = numbers/2
    else:
        import math
        high_numbers = math.ceil(numbers/2)
        low_numbers = int(numbers/2)
    
    return high_numbers,low_numbers

def EvenOdd(numbers):
    '''
    Function to output number of odd and number of even in range
    First:
        even numbers
    Second:
        odd numbers
    '''
    if numbers %2 == 0 :
        even_numbers = numbers/2
        odd_numbers = numbers/2
    else:
        import math
        even_numbers = int(numbers/2)
        odd_numbers= math.ceil(numbers/2)
    
    return even_numbers,odd_numbers

def Analysis(numbers, pool_size):
    '''
    Function that takes list of numbers and integer of pool size
    Returns:
        - occurance of even numbers
        - occurance of odd numbers
        - occurance of low numbers
        - occurance of high numbers
    '''
    even = len(set(numbers).intersection(Groups(pool_size)[0]))  + len(set(numbers).intersection(Groups(pool_size)[2]))
    odd = len(set(numbers).intersection(Groups(pool_size)[1]))  + len(set(numbers).intersection(Groups(pool_size)[3]))
    low = len(set(numbers).intersection(Groups(pool_size)[0]))  + len(set(numbers).intersection(Groups(pool_size)[1]))
    high = len(set(numbers).intersection(Groups(pool_size)[2]))  + len(set(numbers).intersection(Groups(pool_size)[3]))
    
    return (even,odd,low,high)


import itertools

from time import time
tic = time()
probs = []
pool_size =35
drawn_size = 7
combos = [17,2,11,22,23,24,25,29,34,7,20,32,4,5,9]
drawn_numbersz = list(itertools.combinations(combos,drawn_size))
i = 0
while i <len(drawn_numbersz) :

    analytics = Analysis(drawn_numbersz[i],pool_size)
    even = EvenOdd(pool_size)[0]
    odd = EvenOdd(pool_size)[1]
    high = HighLow(pool_size)[0]
    low = HighLow(pool_size)[1]

    a = Combination(odd,analytics[1])*Combination(even,analytics[0])/Combination(pool_size,drawn_size)
    b = Combination(low,analytics[2])*Combination(high,analytics[3])/Combination(pool_size,drawn_size)
    probs.append(a*b)
    i+=1

import pandas as pd
data =  pd.DataFrame({'Numbers': drawn_numbersz, 'Probabilities': probs})
sorted_data = data.sort_values(by=['Probabilities'])
sorted_data.to_csv('numbers.csv',sep=',')
toc = time()
print(toc-tic)

