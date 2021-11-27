import math

#平方根
x = math.sqrt(2)
print(x)

#対数
y = math.log10(2)
print(y)

#三角関数sinπ小数点第2位を四捨五入
z = round(math.sin(math.pi), 2)
print(z)

#出力順を逆に
print('My name is {1}{0}'.format('Watanabe', 'Yohei'))

#円の面積、クロージャー
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    
    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

print(int(3.8)) #切り捨てて整数に
print(float(3)) #整数を浮動小数点数に
