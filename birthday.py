import math

def birth(n):
    n = int(n)
    p = math.factorial(365) / (365**n * math.factorial(365-n))
    result = 1 - p
    print(result)

def p(n):
    return(1 - (math.factorial(365) / (365**i * math.factorial(365-i))))

n = input('クラスの人数は何人ですか？：')
birth(n)

how_many = input('何%を超える人数を知りたいですか？：')
how_many = float(how_many)
i = 1
while i < 365:
    if p(i) < how_many/100:
        print(str(i) + '人')
        birth(i)
        i += 1
    else:
        print(str(i) + '人')
        birth(i)
        print(str(how_many) + '%を超える人数は' + str(i) + '人でした。')
        break