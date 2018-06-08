# -*- coding: UTF-8 -*-

import re

x = 4

mid = x /2

for i in range(x):
    for j in range(x):
      
        if (mid +i/2>j and mid -i/2<j) :
            print('$', end=' ')
        else :
            print(' ', end=' ')
    print('')