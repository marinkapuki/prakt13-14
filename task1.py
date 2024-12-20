import numpy as np  # type: ignore
import time 
 
def input_matrices(): 
    """Вводит две квадратные матрицы от пользователя.""" 
    size = int(input("Введите размер матриц (n x n): ")) 
     
    print("Введите элементы первой матрицы:") 
    matrix1 = [] 
    for i in range(size): 
        row = list(map(int, input(f"Введите строку {i + 1} через пробел: ").split())) 
        matrix1.append(row) 
 
    print("Введите элементы второй матрицы:") 
    matrix2 = [] 
    for i in range(size): 
        row = list(map(int, input(f"Введите строку {i + 1} через пробел: ").split())) 
        matrix2.append(row) 
 
    return np.array(matrix1), np.array(matrix2) 
 
def calculate_result(matrix1, matrix2): 
    """Выполняет алгоритм: сумма матриц и вычисление их определителя.""" 
    sum_matrix = matrix1 + matrix2 
    determinant = np.linalg.det(sum_matrix) 
    return sum_matrix, determinant 
 
def task1_menu(): 
    """Меню первого задания.""" 
    matrix1, matrix2 = input_matrices() 
     
    time.sleep(3)  # Пауза перед выполнением алгоритма 
    result_sum, result_determinant = calculate_result(matrix1, matrix2) 
     
    print("Сумма матриц:") 
    print(result_sum) 
     
    print(f"Определитель суммы матриц: {result_determinant}") 