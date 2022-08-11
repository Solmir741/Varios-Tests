import numpy as np


s = "words and 00987"

#s_list = list(s)
begin_digit = False
end_digit  = False
sign = 1
result_str = ''
for el in range(len(s)):
    if s[el] != ' ':
        if s[el] == '-': sign = -1
        try:
            d = int(s[el])
            result_str = result_str + s[el]
            begin_digit = True
        except:
            if begin_digit: break
result = int(result_str) * sign
result = result if result in range(np.power(-2, 31), np.power(2, 31) - 1) else 0
print(result)
        