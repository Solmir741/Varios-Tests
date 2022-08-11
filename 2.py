#l1 = [0]
#l2 = [0]

#l1 = [2,4,3]
#l2 = [5,6,4]

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

len1 = len(l1)
len2 = len(l2)
dec = (0, 0)
result = []
for f in range(1, max(len1, len2) + 1):
    num1 = l1[-f] if f <= len1 else 0
    num2 = l2[-f] if f <= len2 else 0
    # сложениe
    summ = num1 + num2 + dec[0]
    dec = (0, summ) if summ < 10 else (1, summ - 10)
    result.append(dec[1])
if dec[0] == 1:
    result.append(1)
print(result)