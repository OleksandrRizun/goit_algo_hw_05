#------------------------------------------------------------------------------
# Реалізуйте функцію caching_fibonacci яка створює та використовує кеш для
#   зберігання і повторного використання вже обчислених значень чисел Фібоначчі
# Ряд Фібоначчи - це послідовність 0, 1, 1, 2,3,5,8
# Функція caching_fibonacci() повинна повертати функцію fibonacci(n), яка
#   обчислює n. Якщо число вже є у кеші, функція має повертати значення з кешу,
#   якщо немає, то обчислити, зберегти у кеші та повернути результат.
#------------------------------------------------------------------------------
from typing import Callable
def caching_fibonacci() -> Callable[[int], int]:
    cache = {}
    def fibonacci(n: int) -> int:
        nonlocal cache
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci
fib = caching_fibonacci()
print(fib(10))
print(fib(15))