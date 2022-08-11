s = 'PAYPALISHIRING'
ls = len(s)
numRows = 1
result = '' if numRows > 1 else s
str_num = {}
for n_row in range(1, (2 * numRows - 2) + 1):
    n = 0
    mas = []
    while (n * (2 * numRows - 2) + n_row) <= ls:
        mas.append(n * (2 * numRows - 2) + n_row)
        n += 1
    str_num[n_row] = mas

for r in range(1, (numRows - 2) + 1):
    res_mas = str_num.get(numRows - r) + str_num.get(numRows + r)
    res_mas = sorted(res_mas)
    str_num[numRows - r] = res_mas
    str_num.pop(numRows + r)
for key, val in str_num.items():
    for res in val:
        result = result + s[res - 1]
print(result)