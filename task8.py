'''Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no'''

n = int(input("please enter n: "))
m = int(input("please enter m: "))
k = int(input("please enter k: "))

if ((k%n==0) or (k%m==0)) and (k<(n*m)):
    result = "yes"
else:
    result = "no"

print(f"{n}x{m} {k} -> {result}")