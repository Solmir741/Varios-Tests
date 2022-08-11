s = "dvdf"
s = "abcabcbb"
s = ''
s = ' '
s = "bbbbb"
s = "pwwkew"
maxres = 0
uniqmas = []
for f in s:
    if f in uniqmas:
        maxres = max(len(uniqmas), maxres)
        uniqmas = uniqmas[uniqmas.index(f) + 1:]
    uniqmas.append(f)
maxres = max(len(uniqmas), maxres)
print(maxres)