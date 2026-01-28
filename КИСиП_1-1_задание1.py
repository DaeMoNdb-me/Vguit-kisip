Вариант 2
Задание 1

# Запрос на объем массива
n = int(input("Введите количество элементов массива: "))

# Запрос на ввод данных массива
array = []
print(f"Введите {n} целочисленных элементов:")
for i in range(n):
    element = int(input())
    array.append(element)

# Начало работы цикла по поиску минимального значения
min_value = array[0]  # По умолчанию безем первое значения в массиве как минимальное, что бы было с чем далее сравнивать
min_index = 0

for i in range(1, n):
    if array[i] < min_value:
        min_value = array[i]
        min_index = i

# Вывод результата
print("Индекс минимального элемента:", min_index)




Задание 2

# Запрос на объем масива
n = int(input("Введите количество элементов массива: "))

# Запрос на ввод данных массива
array = []
print(f"Введите {n} целых чисел:")
for i in range(n):
    element = int(input())
    array.append(element)

# Делаем 2 массива для вывода
positive = []   # для положительных элементов
others = []    # для остальных (нулевых и отрицательных)

# Раскидываем основной массив на 2 части
for num in array:
    if num > 0:
        positive.append(num)
    else:
        others.append(num)

# Выводим результаты
print("Положительные элементы:", positive)
print("Остальные элементы:", others)