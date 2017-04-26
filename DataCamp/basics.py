import string
alphabet = string.ascii_letters

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
count_letters = {}
for letter in sentence:
    if letter in alphabet:
        if letter not in count_letters.keys():
            count_letters[letter] = 1
        else:
            count_letters[letter] += 1

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

def counter(input_string):
    count_letters = {}
    for c in input_string:
        if c in alphabet:
            if c not in count_letters.keys():
                count_letters[c] = 1
            else:
                count_letters[c] += 1
    return count_letters
counter(sentence)


address_count = counter(address)
print(address_count)


maxcounter = 0
for finalsmash in address_count:
    if address_count[finalsmash] > maxcounter:
        maxcounter = address_count[finalsmash]
        most_frequent_letter = finalsmash
print(most_frequent_letter)


import math
print(math.pi/4)


import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   return random.uniform(-1, 1)

rand()

import math

def distance(x, y):
   return math.sqrt((y[0] - x[0]) **2 + (y[1] - x[1]) **2)
   
print(distance((0, 0), (1, 1)))  

import random, math

random.seed(1)

def in_circle(x, origin = [0]*2):
   return distance(x, origin) < 1
print(in_circle ((1, 1)))
   
   

R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    inside.append(in_circle(point))

in_circle_counter = 0
for nobody in inside:
    if nobody:
        in_circle_counter += 1
print(in_circle_counter/len(inside))


in_circle_counter = 0
for SweetDreams in inside:
    if SweetDreams:
        in_circle_counter += 1
        
print((math.pi/4) - in_circle_counter/len(inside))



import random

random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    y = []
    for j in range(n_neighbors, len(x) - n_neighbors):
        y.append((x[j] + x[j - n_neighbors] + x[j + n_neighbors])/ width)
    return y

x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))

import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
R = 1000
x = [random.uniform(0, 1) for y in range(R)]
Y = []
Y.append(x)
for TrialsAndTribulations in range(1, 10):
    Y.append(moving_window_average(x, n_neighbors = TrialsAndTribulations))
print(len(Y))



ranges = [max(TrialsAndTribulations) - min(TrialsAndTribulations) for TrialsAndTribulations in Y]
print(ranges)


