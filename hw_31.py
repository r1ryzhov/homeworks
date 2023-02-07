# Level 1

x = float(input()) #изначальная сумма вклада
y = float(input()) #конечная сумма вклада
p = float(input()) #процент

p = p/100

l = float(y/(x+x*p))
l = int(-1 * l // 1 * -1) #округление в большую сторону
print(l)
#Почему-то подумал, что нужно округлить в большую сторону,
#в таком случае возникает вопрос, что лучше использовать для округления? эту формулу "int(-1 * l // 1 * -1)",
#import.math или from math import ceil с точки зрения улучшения качества кода?

# Level 2
n = int(input())
i = 0

while i != n:
    i += 1
    print('for - частный случай цикла while')

# Level 3
n = int(input())
n = str(n)
n_num = map(int, n)
print(sum(n_num))




