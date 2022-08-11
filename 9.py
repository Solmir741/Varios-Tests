
x = -121
if x < 0: print(False)
x_fol = x
mas = []
while x_fol != 0:
    x_fol = x // 10
    mas.append(x % 10)
    x = x_fol
print(mas == list(reversed(mas)))