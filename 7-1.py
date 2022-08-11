import numpy as np
rev = 0
x = -321
MIN_VALUE = np.power(-2 , 31)
MAX_VALUE = np.power(2 , 31) - 1
while (x != 0):
    pop = int(x) % 10
    x /= 10
    x = np.round(x, 0)
    if (rev > MAX_VALUE/10 or (rev == MAX_VALUE / 10 and pop > 7)): print(0)
    if (rev < MIN_VALUE/10 or (rev == MIN_VALUE / 10 and pop < -8)): print(0)
    rev = rev * 10 + pop
print(rev)