   
import time  
 
def rotate_matrix(matrix): 
    """Поворачивает матрицу на 90 градусов против часовой стрелки.""" 
     
    return [list(reversed(col)) for col in zip(*matrix)] 
 
def task3_menu(): 
     
    while True: 
         
        rows = int(input("Введите количество строк матрицы: ")) 
         
        cols = int(input("Введите количество столбцов матрицы: ")) 
         
        matrix_data = [] 
         
        for i in range(rows): 
             
            row_input = input(f"Введите элементы строки {i + 1} через пробел: ") 
             
            row_data = list(map(int, row_input.split())) 
             
            if len(row_data) != cols: 
                print(f"Ошибка! Должно быть {cols} элементов в строке.") 
                continue 
             
            matrix_data.append(row_data) 
 
         
        direction_input = input("Введите направление поворота (по часовой стрелке/против часовой стрелки): ") 
 
         
        if direction_input.lower() == "по часовой стрелке": 
             
            for _ in range(3):  
                matrix_data = rotate_matrix(matrix_data) 
                 
        elif direction_input.lower() == "против часовой стрелки": 
             
            matrix_data = rotate_matrix(matrix_data) 
             
         
        else: 
             
            print("Неверное направление поворота.") 
             
            continue 
         
         
        print("Повернутая матрица:") 
         
        
        for row in matrix_data: 
             
            print(" ".join(map(str, row))) 
         
        time.sleep(3)  # Пауза перед возвратом в меню