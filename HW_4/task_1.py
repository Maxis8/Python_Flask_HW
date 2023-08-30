# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# При решении задачи нужно использовать многопоточность.
# В каждом решении нужно вывести время выполнения
# вычислений.
from random import randint
import threading
import time

numbers = [randint(1, 100) for _ in range(1000000)]
res = 0


def sum_array(start, end):
    global res
    for i in range(start, end):
        res += numbers[i]
    print(f'. Result = {res:_}')


start_time = time.time()
threads = []
cnt_threads = 10


def get_sum():
    for i in range(cnt_threads):
        starts = i * len(numbers) // cnt_threads
        ends = (i + 1) * len(numbers) // cnt_threads
        thread = threading.Thread(target=sum_array, args=(starts, ends))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return res


if __name__ == '__main__':
    get_sum()
    print(f'Time: {time.time() - start_time:.8f} sec')

