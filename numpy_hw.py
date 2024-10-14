import numpy as np

""" Написать программу, использующую NumPy, чтобы получить степени значений массива по-элементно.
Пояснение: Элементы первого массива подняты в степени значений из второго. Вывод:
Основной массив
[0 1 2 3 4 5 6]
Элементы первого массива подняты в степени значений из второго: [ 0 1 8 27 64 125 216]
 """
arr1 = np.array([0, 1, 2, 3, 4, 5 ,6])
arr2 = np.array([0, 1, 8, 27, 64, 125, 216])
print("Задание 1")
# поэлементарное возведение
res = np.power(arr1, arr2)
print("Возведение элементов первого массива в степени элементов второго: ", *res, sep=', ')

print("Задание 2")

""" Написать программу, использующую NumPy, которая округляет элементы массива до указанного количества значений после запятой.
Вывод:
[ 1. 2. 2.]
[ 0.3 0.5 0.6] [ 0. 2. 2. 4. 4.] """

arr1 = np.array([0.234, 1.5676, 2.355, 3.22, 4.99, 5.543 ,6.86])
arr2 = np.array([0.24, 1.5333, 8.432, 27.43, 64.532, 125.422, 216.53])

res1 = np.round(arr1, 2)
res2 = np.round(arr2, 2)

print(f"Массив 1: {arr1}\n Округление: {res1}")
print(f"Массив 2: {arr2}\n Округление: {res2}")

print("Задание 3")

""" Написать программу, использующую NumPy, которая создаёт внутреннее произведение двух массивов.
Вывод:
Array x:
[[[ 0 1 2 3]
[ 4 5 6 7]
[ 8 9 10 11]]
[[12 13 14 15]
[16 17 18 19]
[20 21 22 23]]]
Array y:
[0 1 2 3]
Внутреннее произведение: [[ 14 38 62]
[ 86 110 134]] """

# Внутреннее произведение (или скалярное произведение) двух массивов
# — это операция, при которой соответствующие элементы двух массивов перемножаются,
# а затем результаты суммируются.

arrx = np.array([[[0, 1, 2, 3],
                   [4, 5, 6, 7],
                   [8, 9, 10, 11]],

                  [[12, 13, 14, 15],
                   [16, 17, 18, 19],
                   [20, 21, 22, 23]]])

arry = np.array([0, 1, 2, 3])

# Внутреннее произведение
res = np.dot(arrx, arry)

print("Array x:")
print(arrx)
print("Array y:")
print(arry)
print("Внутреннее произведение:")
print(res)