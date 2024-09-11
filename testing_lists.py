# Написать реализацию функции SortList(), которая принимает на себя список, и возвращает отсортированную его версию.
# Вам будет необходмо написать для этой функции ряд тестов (фиксированного количества нет).
# Напишите как положительные, так и отрицательные тесты.

import unittest

class TestingList(unittest.TestCase):
    def test_list(self):
        my_list = [4, 6, 1, 6, 13, -7]
        # result = my_list.sort()  ощибка была из за sort 
        # Метод sort() сортирует список на месте и возвращает None. 
        # Поэтому значение result будет равно None, а сравнение с expected даст ошибку
        # sorted() создает новый список
        result = sorted(my_list)
        expected = [-7, 1, 4, 6, 6, 13]
        self.assertEqual(result, expected)
        

# AssertionError: None != [-7, 1, 4, 6, 6, 13]

    def test_another_list(self):
        my_another_list = [3, -23, 89, 23, 4, 45]
        result = my_another_list.sort() # sort() сортирует список на месте и возвращает None. Поэтому значение result будет равно None, а сравнение с expected даст ошибку.
        expected = sorted(my_another_list)
        self.assertEqual(result, expected)
        
        #AssertionError: None != [-23, 3, 4, 23, 45, 89]
        
    def test_inverted_list(self):
        my_inverted_list = [5, 23, -8, 0, 32]
        result = my_inverted_list.sort(reverse=True)
        expected = [-8, 0, 5, 23, 32]
        self.assertEqual(result, expected)
      # AssertionError: None != [-8, 0, 5, 23, 32]  
      
      # уже без ошибки 
    def test_inverted_list(self):
        my_inverted_list = [5, 23, -8, 0, 32]
        my_inverted_list.sort(reverse=True)
        expected = [32, 23, 5, 0, -8]
        self.assertEqual(my_inverted_list, expected)
        
    def test_even_numbers(self):
        my_all = [7, 5, 8, 2, 11, 1, 14]
        result = my_all.sort(key=lambda x: x%2)
        expected = [8, 2, 14, 7, 5, 11, 1]
        self.assertEqual(result, expected)
     # AssertionError: None != [8, 2, 14, 7, 5, 11, 1]   
    
    def test_even_numbers(self):
        my_all = [7, 5, 8, 2, 11, 1, 14]
        my_all.sort(key=lambda x: x%2)
        expected = [8, 2, 14, 7, 5, 11, 1]
        self.assertEqual(my_all, expected)
if __name__ == '__main__':
    unittest.main()