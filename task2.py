import time
from threading import Thread

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

def task2_operations(array, target_sum):
    """Выполняет подсчет подмассивов с заданной суммой."""
    result = count_subarrays_with_sum(array, target_sum)
    print(f"Количество подмассивов с суммой {target_sum}: {result}")

def task2_menu():
    """Меню второго задания."""
    while True:
        print("\nЗадание 2: Подмассивы с заданной суммой")
        
        # Пауза перед вводом массива
        print("Пауза перед вводом массива...")
        time.sleep(7)  # Пауза на 7 секунд
        
        # Ввод массива и целевой суммы
        array_input = input("Введите массив чисел через пробел: ")
        
        try:
            # Преобразование ввода в список целых чисел
            array = list(map(int, array_input.split()))
        except ValueError:
            print("Ошибка ввода. Убедитесь, что введены только числа.")
            continue
            
        # Пауза перед вводом целевой суммы
        print("Пауза перед вводом целевой суммы...")
        time.sleep(7)  # Пауза на 7 секунд
        
        target_sum = int(input("Введите целевую сумму: "))
        
        # Создание потока для выполнения операции
        operations_thread = Thread(target=task2_operations, args=(array, target_sum))
        operations_thread.start()

        if input("Хотите продолжить? (y/n): ") != 'y':
            break

if __name__ == "__main__":
    task2_menu()
