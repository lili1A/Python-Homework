import numpy as np

# array1D = np.array([1, 2, 3])

# array2D = np.array([1, 2, 3], [4, 5, 6])

# array3D = np.array([[1, 2], [3, 4], [5, 6]],
#                    [[1, 2], [3, 4], [5, 6]],
#                    [[1, 2], [3, 4], [5, 6]])

a = np.zeros((2, 2)) # нулевый массив
print(*a)
print(  )
print(a)

b = np.ones((1, 2)) # единичный массив
print(b)

pi = 3.14
c = np.full((2, 2), pi)
print(c)

d = np.eye(3) # eye creates a matrice на то колво 3*3, основная диагональ - 1, rest - 0
print(d)

e = np.random.random((3, 3)) # range from 0 to 1 
print(e)

f = np.random.random_integers(1, 10, (3, 3)) # 1 - lowest border, 2 - highest border, 3 - matrice size
print(f)

##############################################

# making a number sequence 
# Этот код создает массив с помощью функции np.arange() из библиотеки NumPy и выводит его на экран
A = np.arange(0, 30, 5)
print(A)

# np.arange(start, stop, step) start - beginning of the sequence, stop - end of the sequence, step - step between elements

B = np.linspace(1, 15, 3)
print(B)
# np.linspace(start, stop, num) - генерирует массив, состоящий из чисел, равномерно распределённых между значениями start и stop.

# start - 1, stop - 15, num - number of the numbers 

##############################################

# reshape method: меняет форму массива

b = np.ones((1, 2)) # единичный массив, 1 - row, 2 - column 
print(b)
b2 = np.reshape(b, (2, 1))
print()
print(b)
print()
print(b2)

# где мои деньги милый а думаешь как возвращать их можгно ты будешь хорошим можно можно ты меня не тронешь

############################################## 
# indexation and slicing (срезы)
# 
# Этот код работает с многомерными массивами NumPy, создавая двумерный массив (матрицу) и выполняя операции по выборке его элементов.

# Это создание двумерного массива (матрицы) размером 3x4:
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Эта строка выбирает элемент массива a, который находится на второй строке (индекс 1) и третьем столбце (индекс 2).
b = a[1, 2]
# Эта строка использует срез (сабсет) для выбора подмассива из массива a
# 0:2 указывает, что нужно выбрать строки с индексами 0 и 1 (то есть первые две строки).
# 1:4 указывает, что нужно выбрать столбцы с индексами 1, 2 и 3 (то есть 2-й, 3-й и 4-й столбцы).
c = a[0:2, 1:4]
print(a)
print()
print(c)
############################################## 
a = np.array([[1, 2, 5, 3]])  # Создаём 2D массив (матрицу)
print(a)
a = a.T  # Транспонирование, меняет строки и столбцы местами
print(a)
a += 3 # каждый элемент увелич-ся на 3
a -= 4
a *= 5

a **= 2
a = a.T
print(a)

############################################## 

arr = np.array([[1, 5, 6], 
                [4, 7, 2],
                [3, 1, 9]])
print(arr.max()) # arr.max() находит максимальное значение во всём массиве. В данном случае это число 9.
print(arr.max(axis=1)) # arr.max(axis=1) находит максимальные значения по строкам. То есть для каждой строки будет найдено максимальное число:
print(arr.max(axis=0)) # arr.max(axis=0) находит максимальные значения по столбцам. То есть для каждого столбца будет найдено максимальное число:
print(arr.sum()) # arr.sum() находит сумму всех элементов массива. Складываем все числа в массиве - 38
print(arr.sum(axis=1)) # arr.sum(axis=1) находит суммы по строкам. Для каждой строки считается сумма её элементов:
print(arr.cumsum(axis=1)) # arr.cumsum(axis=1) выполняет операцию кумулятивной суммы по строкам. Это означает, что для каждой строки будет считаться сумма текущего элемента и всех предыдущих элементов в этой строке:

############################################## 
a = np.array([[1, 2],
              [3, 4]])
a = np.array([[4, 3],
              [2, 1]])
# арифметические операции с матрицами 
print()
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#эээээ
