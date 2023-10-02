
# Задача 30
a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

progression = []
for i in range(n):
 element = a1 + (i * d)
progression.append(element)

print("Массив элементов арифметической прогрессии: ", progression)

# Задача 32


def find(arr, min, max):
 indexes = []
 for i, element in enumerate(arr):
  if min <= element <= max:
   indexes.append(i)
 return indexes

array = [1, 5, 2, 7, 3, 9, 4, 6]
min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))

result = find(array, min, max)
print("Индексы элементов, принадлежащих заданному диапазону:", result)