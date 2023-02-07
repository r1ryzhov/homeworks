# Level 1

l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
copy = [x for i, x in enumerate(l) if i != l.index(x)]
print(copy)

# Level 2

import numpy
from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
print(m)
print(max(numpy.concatenate(m)))
#я два часа думал, как это можно сделать, только через numpy получилось, так же нужно было?
#выводит ли max сам по себе значение или нужно обязтально перед этим указывать print?

# Level 3

d = {'name1' : 'id1', 'name2' : 'id2', 'name3' : 'id3'}
{v:k for k, v in d.items()}