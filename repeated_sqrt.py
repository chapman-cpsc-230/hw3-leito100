
"""
File: <filename>

Copyright (c) 2016 <your name>

License: MIT

<brief description of the code>
"""

from math import sqrt
for n in range(1, 60):
    r= 2.0
    if n > 51:
        n = 45
    for i in range(n):
        r = sqrt(r)
    print ("r", r)
    for i in range(n):
        r = r**2
    print '%d times sqrt and **2: %16f' %(n, r)
# This program repeatedly takes the square root of a number n times and squares it n times.
