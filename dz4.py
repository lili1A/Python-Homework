# Задание 1
# Пользователь вводит с клавиатуры два числа. 
# Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне,
# а также среднеарифметическое каждой группы.



# Задание 1
""" def main():
    try:
        first_number = float(input("Введите первое число: "))
        second_number = float(input("Введите второе число: "))
        
        if first_number > second_number:
            print("Второе число должно быть больше первого.")
            return
        
        numbers_list = [first_number, second_number]
        print("Список: ", numbers_list)
        
        print("Четные числа в диапазоне:")
        for num in numbers_list:
            if num % 2 == 0:
                print(num)
                
        print("Нечетные числа в диапазоне:")
        for num in numbers_list:
            if num % 2 != 0:
                print(num)
                
        print("Кратные 9 числа в диапазоне:")
        for num in numbers_list:
            if num % 9 == 0:
                print(num)
     
    except ValueError:
        print("Введите только числа.")

main()
 """
 
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

if number1 > number2:
    number1, number2 = number2, number1
   
number_range = range(number1, number2 + 1)
print("The first number of the range is ", number1, " and the second number is ", number2)

even_numbers = []
odd_numbers = []
multiples_of_9 = []

print("Even numbers in the range:")
for num in number_range:
    if num % 2 == 0:
        even_numbers.append(str(num))
        
print("Odd numbers in the range:")
for num in number_range:
    if num % 2 != 0:
        odd_numbers.append(str(num))
        
print("Multiples of 9:")
for num in number_range:
    if num % 9 == 0:
        multiples_of_9.append(str(num))

print("Even numbers in the range: ", ", ".join(even_numbers))
print("Odd numbers in the range: ", ", ".join(odd_numbers))
print("Multiples of 9 in the range: ", ", ".join(multiples_of_9))








            
            
   
    
