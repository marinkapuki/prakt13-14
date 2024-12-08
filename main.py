import threading
import task1
import task2
import task3

# Список для отслеживания активных потоков
active_threads = []

def main_menu():
    """Главное меню приложения."""
    while True:
        print("\nГлавное меню:")
        print("1) Задание 1")
        print("2) Задание 2")
        print("3) Задание 3")
        print("4) Завершить работу программы")

        choice = input("Выберите опцию: ")

        if choice == '1':
            thread = threading.Thread(target=task1.task1_menu)
            thread.start()
            active_threads.append(thread)

        elif choice == '2':
            thread = threading.Thread(target=task2.task2_menu)
            thread.start()
            active_threads.append(thread)

        elif choice == '3':
            thread = threading.Thread(target=task3.task3_menu)
            thread.start()
            active_threads.append(thread)

        elif choice == '4':
            print("Выход из программы.")
            # Завершение всех активных потоков перед выходом
            for t in active_threads:
                t.join()  # Дождаться завершения потоков
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main_menu()