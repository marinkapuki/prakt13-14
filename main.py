import threading

from task1 import task1 
from task2 import task2 
from task3 import task3 
 

def user_menu(user_id):
    while True:
        print(f"\nПользователь {user_id}: Выберите пункт меню:")
        print("1. Ввод данных")
        print("2. Выполнение операции")
        print("3. Вывод результата")
        print("0. Выход")

        choice = input(f"Пользователь {user_id}, ваш выбор: ")

        if choice == '1':
            data = input(f"Пользователь {user_id}, введите данные: ")
            print(f"Пользователь {user_id} ввел данные: {data}")

        elif choice == '2':
            print(f"Пользователь {user_id} выполняет операцию...")

        elif choice == '3':
            print(f"Пользователь {user_id} выводит результат...")

        elif choice == '0':
            print(f"Пользователь {user_id} выходит из меню.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

def main():
    # Создаем два потока для двух пользователей
    user1_thread = threading.Thread(target=user_menu, args=(1,))
    user2_thread = threading.Thread(target=user_menu, args=(2,))

    # Запускаем потоки
    user1_thread.start()
    user2_thread.start()

    # Ждем завершения потоков
    user1_thread.join()
    user2_thread.join()

if __name__ == "__main__":
    main()
