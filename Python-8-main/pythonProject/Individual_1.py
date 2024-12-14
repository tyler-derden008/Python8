#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def input_routes():
    """Функция для ввода данных о маршрутах."""
    routes = []
    while True:
        start = input("Введите начальный пункт маршрута (или 'stop' для завершения ввода): ")
        if start.lower() == 'stop':
            break
        end = input("Введите конечный пункт маршрута: ")
        number = input("Введите номер маршрута: ")
        route = {
            'start': start,
            'end': end,
            'number': number
        }
        routes.append(route)
    return routes

def sort_routes(routes):
    """Функция для сортировки маршрутов по номерам."""
    return sorted(routes, key=lambda x: x['number'])

def filter_routes(routes, point):
    """Функция для фильтрации маршрутов по начальному или конечному пункту."""
    filtered_routes = [route for route in routes if route['start'] == point or route['end'] == point]
    return filtered_routes

def display_routes(routes):
    """Функция для отображения маршрутов."""
    if not routes:
        print("Маршруты не найдены.")
    else:
        for route in routes:
            print(f"Маршрут {route['number']}: {route['start']} -> {route['end']}")

def main():
    """Основная функция программы."""
    routes = input_routes()
    sorted_routes = sort_routes(routes)
    point = input("Введите название пункта для поиска маршрутов: ")
    filtered_routes = filter_routes(sorted_routes, point)
    display_routes(filtered_routes)

if __name__ == "__main__":
    main()
