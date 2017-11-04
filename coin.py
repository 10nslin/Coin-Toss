
'''
Scott Enslin
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
'''

import random

total_heads = 0
total_tails = 0
count = 0


while count <= 5000:
    coin = random.randint(1, 2)

    if coin == 1:
        total_heads += 1 
        count += 1
        print "attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(count, total_heads, total_tails)

    else:
        total_tails += 1 
        count += 1
        print "attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(count, total_heads, total_tails)

print "Ending The Program. Thank You!"
