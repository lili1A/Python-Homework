# Написать программу с использованием NumPy которая бы мешала числа между 0 и 10 (включительно).
# Ввод:
# [5 7 9 0 2 3 1 6 8 4]

# Вывод:
# [6 7 4 5 8 2 3 9 0 1]

# np.random.permutation() -  функция генерирует случайную перестановку элементов массива.

import numpy as np

numbers = np.arange(1, 11)

shuffled_numbers = np.random.permutation(numbers)

print(shuffled_numbers)

""" while True:
    user_input = input("Enter numbers frpm 1 - 10, use space between numbers: ")

    numbers = [int(num) for num in user_input.split() if num.isdigit() and 1 <= int(num) <= 10]

    if not numbers:
        print("You should have entered  at least one number from 1 - 10")
        continue
    else:
        shuffled_numbers = np.random.permutation(numbers)
    
        print("Shuffled numbers are: ", shuffled_numbers)
        break """
    
    #  np.random.shuffle() для перемешивания массива в NumPy. В отличие от np.random.permutation(), который возвращает новый массив, np.random.shuffle() изменяет массив на месте, что означает, что оригинальный массив будет изменён.
    
numbers = np.arange(1, 11)

shuffled_numbers = np.random.shuffle(numbers)

print(shuffled_numbers) # Функция np.random.shuffle() изменяет массив на месте и не возвращает новый массив, а просто возвращает None. Поэтому, если вы присваиваете результат np.random.shuffle(numbers) переменной, вы получите None, потому что функция не возвращает значения.