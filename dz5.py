# Задание 2
# Пользователь вводит любое целое число. 
# Необходимо из этого целого числа удалить все цифры 3 и 6 
# и вывести обратно на экран.
# Будет плюсом если вы используете управляющие операторы continue, break и else.


# без реккурсии в консоли
""" def number_remove():
    try:
        number_str = input("Enter a whole number: ")
        
        result = number_str # для инициализации результата (чтобы удалить 3 и 6)
        result = result.replace('3', '').replace('6', '')
        
        # решение проблемы возникающей, если вводить строку, состоящую только из 3 и 6
        if result:
            result = int(result)
            print(f"Integer {number_str} without number '3' and '6': {result}")
        else:
            print("Empty string (happens if the input == '3' or '6')")
        
    except ValueError:
        print("Not a number Error")
number_remove()
 """
# с реккурсией в консоли

def number_remove_rec(number_str):
    if not number_str:
        return number_str
   
    result = number_str.replace('3', '').replace('6', '')
    # изменилась ли строка
    if result == number_str:
        return result
    return number_remove_rec(result)

def number_remove():
    while True:
        try:
            print("Enter 'q' to quit the operation or a whole number, if you wish to continue:")
            number_str = input("")
            
            if number_str.lower() == 'q':
                print("Closing...")
                break
            result = number_remove_rec(number_str)
            
            if result:
                result = int(result)
                print("Number without 3 and 6:", result)
            else:
                print("Result is empty after removing 3 and 6")
                
        except ValueError:
            print("It's not a number")

number_remove()

    

        

            