import threading 
import time 
import random
import numpy as np 

def perform_calculation(matrix1, matrix2, result): 
    """Сложение двух матриц и сохранение результата в 'result'."""
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Создаем результирующую матрицу
    sum_matrix = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    result.extend(sum_matrix)  # Сохраняем результат
    print("Сложение матриц выполнено") 

def input_matrices(user_id): 
    """Вводит две квадратные матрицы от пользователя.""" 
    size = int(input(f"Пользователь {user_id}, введите размер матриц (n x n): ")) 
     
    print(f"Пользователь {user_id}, введите элементы первой матрицы:") 
    matrix1 = [] 
    for i in range(size): 
        row = list(map(int, input(f"Введите строку {i + 1} через пробел: ").split())) 
        matrix1.append(row) 

    print(f"Пользователь {user_id}, введите элементы второй матрицы:") 
    matrix2 = [] 
    for i in range(size): 
        row = list(map(int, input(f"Введите строку {i + 1} через пробел: ").split())) 
        matrix2.append(row) 

    return np.array(matrix1), np.array(matrix2) 

def calculate_result(matrix1, matrix2): 
    """Выполняет алгоритм: сумма матриц.""" 
    sum_matrix = matrix1 + matrix2 
    return sum_matrix 

def task1_menu(user_id): 
    """Меню первого задания.""" 
    matrix1, matrix2 = input_matrices(user_id) 
    
    time.sleep(3)  # Пауза перед выполнением алгоритма 
    result_sum = calculate_result(matrix1, matrix2) 
    
    print(f"Пользователь {user_id}, сумма матриц:") 
    print(result_sum) 

def count_subarrays_with_sum(array, target_sum): 
    """Подсчитывает количество подмассивов с заданной суммой.""" 
    count = 0 
    n = len(array) 

    for i in range(n): 
        current_sum = 0 
        for j in range(i, n): 
            current_sum += array[j] 
            if current_sum == target_sum: 
                count += 1 
                 
    return count 

def task2_menu(user_id): 
    """Меню второго задания.""" 
    
    while True: 
        array_input_1 = input(f"Пользователь {user_id}, введите элементы первого массива через пробел (или 'exit' для выхода): ") 
        
        if array_input_1.lower() == 'exit': 
            break 
        
        array_input_2 = input(f"Пользователь {user_id}, введите элементы второго массива через пробел: ") 
        
        array_input_3 = input(f"Пользователь {user_id}, введите элементы третьего массива через пробел: ") 

        try: 
            arr1 = list(map(int, array_input_1.split())) 
            arr2 = list(map(int, array_input_2.split())) 
            arr3 = list(map(int, array_input_3.split())) 
             
            if len(arr1) != len(arr2) or len(arr2) != len(arr3): 
                print("Все массивы должны быть одинакового размера.") 
                continue 

            results = []  # Список для хранения результатов 

            for a, b, c in zip(arr1, arr2, arr3): 
                if a + b == c: 
                    results.append((a + b + c) ** min(a, b, c))   
             
            print(f"Пользователь {user_id}, результаты:", results)  # Выводим результаты проверки сумм 

        except ValueError: 
            print("Ошибка ввода. Убедитесь, что введены только числа.") 

        time.sleep(3)  # Пауза перед возвратом в меню 

def rotate_matrix(matrix): 
    """Поворачивает матрицу на 90 градусов против часовой стрелки."""     
    return [list(reversed(col)) for col in zip(*matrix)] 

def task3_menu(user_id):     
    while True:         
        rows = int(input(f"Пользователь {user_id}, введите количество строк матрицы: "))         
        cols = int(input(f"Пользователь {user_id}, введите количество столбцов матрицы: "))         
        matrix_data = [] 
        
        for i in range(rows):             
            row_input = input(f"Пользователь {user_id}, введите элементы строки {i + 1} через пробел: ")             
            row_data = list(map(int, row_input.split()))             
            if len(row_data) != cols:                 
                print(f"Ошибка! Должно быть {cols} элементов в строке.")                 
                continue             
            matrix_data.append(row_data) 
        
        direction_input = input(f"Пользователь {user_id}, введите направление поворота (по часовой стрелке/против часовой стрелки): ") 
        
        if direction_input.lower() == "по часовой стрелке":             
            for _ in range(3):  
                matrix_data = rotate_matrix(matrix_data)                 
        elif direction_input.lower() == "против часовой стрелки":             
            matrix_data = rotate_matrix(matrix_data)         
        else:             
            print("Неверное направление поворота.")             
            continue 
        
        print(f"Пользователь {user_id}, повернутая матрица:")         
        for row in matrix_data:             
            print(" ".join(map(str, row)))         
        
        time.sleep(3)  # Пауза перед возвратом в меню

def run_menu(user_id): 
    """Запуск меню для пользователя"""  
    while True:
        print(f"\nПользователь {user_id}: Выберите пункт меню:\n"
              "1. Задание 1 (Сложение матриц)\n"
              "2. Задание 2 (Подмассивы с заданной суммой)\n"
              "3. Задание 3 (Поворот матрицы)\n"
              "0. Выход из программы")
        
        choice = input() 
        
        if is_int(choice):  
            choice = int(choice)
            
            if choice == 1:
                task1_menu(user_id)
                
            elif choice == 2:
                task2_menu(user_id)
                
            elif choice == 3:
                task3_menu(user_id)
                
            elif choice == 0:
                print(f"Пользователь {user_id} выходит из программы.")
                break
                
            else:
                print('Неверный выбор.')

def is_int(choice): 
    """Проверка на то, что choice - целое число""" 
    try: 
        if isinstance(choice, int):  
            return True 
        if choice is None: 
            return False 
        if not choice.isdecimal():  
            return False  
        int(choice)  
        return True  
    except (Exception, ValueError, TypeError):  
        return False 

def menu(): 
    """Создаем два потока для двух пользователей""" 
    user1_thread = threading.Thread(target=run_menu, args=(1,))  
    user2_thread = threading.Thread(target=run_menu, args=(2,))
    
    # Запускаем потоки   
    user1_thread.start()   
    user2_thread.start()  
    
    # Ждем завершения потоков   
    user1_thread.join()   
    user2_thread.join()  

if __name__ == "__main__":   
    menu()  # Запуск основной функции при выполнении скрипта
