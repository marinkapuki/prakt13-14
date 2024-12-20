import threading 
import time 
from task1 import task1 
from task2 import task2 
from task3 import task3 
 
def print_menu(): 
    """Выводит меню с доступными заданиями.""" 
    print("\nГлавное меню:") 
    print("1) Задание 1") 
    print("2) Задание 2") 
    print("3) Задание 3") 
    print("4) Завершить работу программы") 
 
def main_menu(): 
    """Главное меню приложения.""" 
    while True: 
        print_menu()  # Выводим меню 
        choice = input("Выберите опцию: ") 
 
        if choice == '1': 
            thread = threading.Thread(target=task1.task1_menu) 
            thread.start() 
            thread.join()  # Ожидаем завершения потока 
            input("Нажмите Enter, чтобы продолжить...")  # Пауза перед возвратом в меню 
 
        elif choice == '2': 
            thread = threading.Thread(target=task2.task2_menu) 
            thread.start() 
            thread.join()  # Ожидаем завершения потока 
            input("Нажмите Enter, чтобы продолжить...")  # Пауза перед возвратом в меню 
 
        elif choice == '3': 
            thread = threading.Thread(target=task3.task3_menu) 
            thread.start() 
            thread.join()  # Ожидаем завершения потока 
            input("Нажмите Enter, чтобы продолжить...")  # Пауза перед возвратом в меню 
 
        elif choice == '4': 
            print("Выход из программы.") 
            break  # Выходим из цикла 
 
        else: 
            print("Неверный выбор.") 
         
if __name__ == "__main__": 
    main_menu()  # Запуск главного меню при выполнении скрипта 