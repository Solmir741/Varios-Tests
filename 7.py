import numpy as np
x = 1534236469
sign = 1
if x < 0:
    x = abs(x)
    sign = -1
x_str = reversed(str(x))
x_list = list(x_str)
while len(x_list) > 0 and x_list[0] == 0:
    x_list.pop(0)
result = sign * int(''.join(x_list))
result = result if result in range(np.power(-2, 31), np.power(2, 31) - 1) else 0
print(result)