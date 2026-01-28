Вариант 2
Задание 1

# ядро
def is_magic_square(matrix):
    n = len(matrix)
    
    
    # Вычисляем сумму первой строки (эталон)
    target_sum = sum(matrix[0])
    
    # Проверяем суммы всех строк
    for i in range(n):
        row_sum = sum(matrix[i])
        if row_sum != target_sum:
            return False, f"Сумма строки {i} ({row_sum}) не равна эталонной ({target_sum})"
    
    # Проверяем суммы всех столбцов
    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != target_sum:
            return False, f"Сумма столбца {j} ({col_sum}) не равна эталонной ({target_sum})"
    
    # Если все проверки прошли
    return True, f"Матрица является магическим квадратом"

# запросы
def input_matrix():
    print("Введите размер квадратной матрицы (n):")
    n = int(input("> "))
    
    if n <= 0:
        raise ValueError("Размер матрицы должен быть положительным числом")
    
    print(f"\nВведите элементы матрицы {n}×{n} построчно (через пробел):")
    matrix = []
    
    for i in range(n):
        print(f"Строка {i + 1}:")
        row = list(map(int, input("> ").split()))
        
        if len(row) != n:
            raise ValueError(f"В строке должно быть ровно {n} элементов")
            
        matrix.append(row)
    
    return matrix

# 
try:
    matrix = input_matrix()
    is_magic, message = is_magic_square(matrix)
    
    print("\nРезультат проверки:")
    print(message)
    
except ValueError as e:
    print(f"Ошибка ввода: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")




Задание 2

def input_matrix(n):
    
    matrix = []
    print(f"Введите элементы матрицы {n}×{n} (по строкам, через пробел):")
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Строка {i+1}: ").split()))
                if len(row) != n:
                    print(f"Ошибка: нужно ввести ровно {n} чисел. Попробуйте снова.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Ошибка: введите целые числа через пробел. Попробуйте снова.")
    return matrix

def swap_first_last_columns(matrix):
    """Переставляет первый и последний столбцы матрицы местами."""
    n = len(matrix)
    for i in range(n):
        matrix[i][0], matrix[i][n-1] = matrix[i][n-1], matrix[i][0]  # Обмен элементов


def print_matrix(matrix, title="Матрица"):
    """Выводит матрицу в виде таблицы с заголовком."""
    print(f"\n{title}:")
    for row in matrix:
        print(" ".join(f"{x:4}" for x in row))

# Основная программа
try:
    n = int(input("Введите размер матрицы N: "))
    if n <= 0:
        raise ValueError("Размер матрицы должен быть положительным числом.")
    
    if n == 1:
        print("В матрице 1×1 первый и последний столбцы — это один и тот же столбец. Перестановка не изменит матрицу.")
    
    # Ввод матрицы
    matrix = input_matrix(n)
    
    # Вывод исходной матрицы
    print_matrix(matrix, "Исходная матрица")
    
    # Перестановка столбцов
    if n > 1:
        swap_first_last_columns(matrix)
        # Вывод изменённой матрицы
        print_matrix(matrix, "Матрица после перестановки первого и последнего столбцов")
    else:
        print_matrix(matrix, "Матрица 1×1 (без изменений)")
        
except ValueError as e:
    print(f"Ошибка ввода: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
