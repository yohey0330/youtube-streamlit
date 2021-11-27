i = 1
gosa = 0.1
print(i)
i *= 3
while i > 2:
    i /= 2
    if i < 2 - gosa:
        print(i)
        i *= 3
    elif abs(2 - i) <= gosa:
        print(i)
        break