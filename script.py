print('Hello, world!')
print(1 + 2)

#forの練習
print('-------------------------------------')
for i in range(5):
    print(i)
print('-------------------------------------')
for j in range(2, 5):
    print(j)
print('-------------------------------------')
for x in range(2, 20, 3):
    print(x)
print('-------------------------------------')
word = 'kasituneho'
#for i in range(10):
for i in range(len(word)):
    print(word[i])
print('-------------------------------------')
l = ['youhei', 'manami', 'yuzuki']
for i in l:
    print(i)
print('-------------------------------------')

#whileの練習
i = 1
while i < 100:
    print(i)
    i += 19
    #print(i)　←順番大事！！
print('-------------------------------------')

i = 1
while i < 100:
    print(i)
    i += 19
    if 50 < i <= 60:
        break
print('-------------------------------------')

#タプル(編集できないメリットがある)
t1 = ('one', 'two', 'three')
t2 = ('four', 'five', 'six')
print(t1)
print(t1[0])
t1 = t1 + t2
print(t1)
print(t1[3])
print('-------------------------------------')

#dictionary辞書
d={'apple':80, 'banana':100}
print(d)
print(d['apple'])
d['banana']=120
print(d)
d['peach'] = 200
print(d)
#d.keys()
for key in d.keys():
    print(key)
#d.values()
for value in d.values():
    print(value)
#d.items()
for key, value in d.items():
    print(key, value)
#d.get()
print(d.get('apple'))
print(d.get('meron'))#エラーでなく「None」となるのがメリット
#d.pop()
print(d.pop('apple'))
print(d)#アップルが辞書から消えるのがメリット
print('-------------------------------------')

#set集合、ベン図
a = {1, 1, 2, 3, 5, 8, 13, 21}
print(a)#重複が削除される、順序はランダム
a = {1, 2, 3, 4, 5}
b = {2, 3, 5, 7, 9}
print(a - b)#差集合
print(b - a)#非可換
print(a & b)#積集合
print(a | b)#和集合
print(a ^ b)#排他的論理和
print('-------------------------------------')

#関数
l = [7, 13, 91]
print(max(l))
print(min(l))
def say_hello():#基本
    print('Hello!')
say_hello()
def say_hello():#returnの場合
    s = 'Hello!!'
    return s
returned_s = say_hello()
print(returned_s)

def fizzbuzz(x):#引数の活用
    if x % 15 == 0:
        result = 'FizzBuzz'
    elif x % 3 == 0:
        result = 'Fizz'
    
    elif x % 5 == 0:
        result = 'Buzz'
    else:
        result = x
    return result
r1 = fizzbuzz(30)
r2 = fizzbuzz(36)
r3 = fizzbuzz(40)
r4 = fizzbuzz(43)
print(r1, r2, r3, r4)

def f(x):#returnのイメージと数学の関数について
    return x**2 -2*x-3
print(f(3))

def get_full_name(first,name):#キーワード引数（メリット↓）
    return first + ' ' + name
r = get_full_name(name='陽平', first='渡邊')#アメリカンにならずに指定できる
print(r)

half_value = lambda x: x / 2#lambda式（defいらない）関数名をつけるまでもない簡単な処理のときに使える
r = half_value(6)
print(r)

f = lambda x: x if x % 2 == 0 else '2で割り切れません！'#lambda式の例２
print(f(4))
print(f(5))

add_num = lambda a, b: a + b
try: #例外処理
    r = add_num(1, '2')#intとstrの混合
    #print(r)←elseの方が良い
except TypeError as e:#エラーの理由出力
    print(e)
    print('例外が発生しました')
else:#tyr成功のときのみ有効
    print(r)
finally:#成功しようが失敗しようが出力
    print('例外処理を終わりました')
#スクレイピング（Websiteにアクセス）できなかったとき、エラーになったときに便利！
print('-------------------------------------')

#classクラス
class Child(object):#基本形（理解度イマイチ）
    def say_hello(self):
        print('yahooo----!!')
child = Child()
child.say_hello()

class Child(object):#__init__形（理解度イマイチ）
    def __init__(self):
        print('yatta----!!')
    def say_hello(self):
        print('Wahoo----!!')
child = Child()
child.say_hello()

class Child(object):#self,〇〇形（理解度イマイチ）
    def __init__(self,name):
        self.name = name
        print('My name is', self.name)
    def say_hello(self,name):
        print('Wahoo----!!',self.name)
child = Child('Yuzuki')
child.say_hello('Yuzuki')

#継承、親クラス子クラス
class Child(object):
    def say_hello(self):
        print('yayaya----!')
class JapaneseChild(Child):#Childを継承してます
    def say_ohayo(self):
        print('おはよー！')
    pass
japanese_child = JapaneseChild()
japanese_child.say_hello()#親クラスのsay_helloが継承されている
japanese_child.say_ohayo()#子クラスのsay_ohayoももちろん使える

#import、ライブラリ
import seaborn as sns
iris = sns.load_dataset('iris')
sns.pairplot(iris)