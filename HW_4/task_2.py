# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# При решении задачи нужно использовать многопроцессорность.
# В каждом решении нужно вывести время выполнения
# вычислений.
from multiprocessing import Pool
from random import randint
import time

start_time = time.time()


def sum_list(lst):
    res = 0
    for i in lst:
        res += i
    print(f'Result = {res:_}')
    return res


def multi_proc(lst):
    pool = Pool(processes=10)
    res = pool.map(sum_list, lst)
    return sum(res)


if __name__ == '__main__':
    my_array = [randint(1, 100) for _ in range(1_000_000)]
    split_array = [my_array[i:i + 100_000] for i in range(0, 1_000_000, 100_000)]
    result = multi_proc(split_array)

    print(f'\nAll sum = {result:_} \n Time: {time.time() - start_time:.8f} sec')

