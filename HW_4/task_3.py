# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# При решении задачи нужно использовать асинхронность.
# В каждом решении нужно вывести время выполнения
# вычислений.
import asyncio
import time
from random import randint

res = 0
numbers = [randint(1, 100) for _ in range(1000000)]
start_time = time.time()


async def sum_async(lst, start_idx, end_idx):
    result = 0
    for i in range(start_idx, end_idx):
        result += lst[i]
    print(f'. Result = {result:_}')
    return result


async def main():
    global res
    tasks = []
    num_tasks = 10
    for i in range(num_tasks):
        starts = i * len(numbers) // num_tasks
        end = (i + 1) * len(numbers) // num_tasks
        task = asyncio.create_task(sum_async(numbers, starts, end))
        tasks.append(task)
    for task in tasks:
        res += await task
    return res


if __name__ == '__main__':
    asyncio.run(main())
    print(f'All sum: {res} Time: {time.time() - start_time:.8f} sec')

