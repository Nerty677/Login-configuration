import time

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result

def sum_numbers(a, b):
    return a + b

# Вимірювання часу роботи функції sum_numbers
elapsed_time, result = measure_time(sum_numbers, 5, 10)
print(f"Час виконання: {elapsed_time} секунд, Результат: {result}")


def test_measure_time():
    # Тест 1: Перевірка правильності результату функції
    elapsed_time, result = measure_time(sum_numbers, 5, 10)
    assert result == 15, "Тест не пройдено: очікуваний результат 15"

    # Тест 2: Перевірка правильності вимірювання часу
    def slow_function():
        time.sleep(2)
        return "done"

    elapsed_time, result = measure_time(slow_function)
    assert elapsed_time >= 2, "Тест не пройдено: очікуваний час виконання >= 2 секунд"
    assert result == "done", "Тест не пройдено: очікуваний результат 'done'"

    print("Усі тести пройдено успішно.")


# Виконання тестів
test_measure_time()
