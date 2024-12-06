# task3.py
import math
from threading import Thread

def calculate_distances(points1, points2):
    """Вычисляет расстояния между двумя массивами точек."""
    distances = []
    
    for p1, p2 in zip(points1, points2):
        distance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        distances.append(distance)
        
    return distances

def filter_distances(distances, threshold):
    """Фильтрует расстояния по заданному порогу."""
    return [d for d in distances if d > threshold]

def task3_operations(points1, points2, threshold):
    """Выполняет вычисление и фильтрацию расстояний."""
    distances = calculate_distances(points1, points2)
    filtered_distances = filter_distances(distances, threshold)
    
    print(f"Расстояния между точками: {distances}")
    print(f"Расстояния больше порога {threshold}: {filtered_distances}")

def task3_menu():
    """Меню третьего задания."""
    while True:
        points_input_1 = input("Введите точки первого массива (x,y) через пробел: ")
        points_input_2 = input("Введите точки второго массива (x,y) через пробел: ")
        
        # Преобразование ввода в список кортежей
        try:
            points1 = [tuple(map(int, point.split(','))) for point in points_input_1.split()]
            points2 = [tuple(map(int, point.split(','))) for point in points_input_2.split()]
        except ValueError:
            print("Ошибка ввода. Убедитесь, что точки введены в формате 'x,y'.")
            continue
        
        threshold = float(input("Введите порог расстояния: "))
        
        # Создание потока для выполнения операции
        operations_thread = Thread(target=task3_operations, args=(points1, points2, threshold))
        operations_thread.start()
        operations_thread.join()  # Ожидание завершения потока

        if input("Хотите продолжить? (y/n): ") != 'y':
            break