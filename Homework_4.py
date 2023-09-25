# Задача 22
n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
 num = int(input())
 set1.add(num)

print("Введите элементы второго множества:")
for i in range(m):
 num = int(input())
 set2.add(num)

num = sorted(list(set1.intersection(set2)))

print("Числа, которые встречаются в обоих множествах:")
for num in num:
 print(num)


# Задача 24

n = int(input("Введите количество кустов: "))
berries = []
for i in range(n):
 num = int(input("Введите количество ягод на кусте: "))
 berries.append(num)

max_berries = 0
for i in range(n):
 curr_berries = berries[i] + berries[(i+1) % n] + berries[(i+2) % n]
 if curr_berries > max_berries:
  max_berries = curr_berries

print("Максимальное количество ягод, которые можно собрать за один заход, составляет:", max_berries)