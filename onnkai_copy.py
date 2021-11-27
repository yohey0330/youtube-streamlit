l = [1]
i = 1
gosa = 0.1

i *= 3
while i > 2:
    i /= 2
    if i < 2 - gosa:
        l.append(i)
        i *= 3
    elif abs(2 - i) <= gosa:
        l.append(i)
        break

l.sort()
l_n = list(map(lambda x: x * 440, l))
for i in l_n:
    print(i)