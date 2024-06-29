"""  .split() - метод разделения строки на части. 
 .split() - разделяет строку по пробелам 
 .split(',') - по запятым 
 
 str.split(sep=None, maxsplit=-1)
 
 sep=None - разделитель, None - любой пробельный символ 
 
 maxsplit=-1 - максимальное кол-во разделений. при -1 - максимальное колво разделений
 
 """

def sum_numbers(a, b, c):
    return a + b + c

def mult_numbers(a, b, c):
    return a * b * c

def main():
    print("Enter three numbers: ")
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        num3 = float(input("Third number: "))
    except ValueError:
        print("Enter only numbers")
        return
    
    print("Choose operation")
    print("1: Sum")
    print("2: Multiplication")

    choice = input("Choose between 1 and 2: ")

    if choice == "1":
        result = sum_numbers(num1, num2, num3)
        print("Result: ", result)
    elif choice == "2":
        result = mult_numbers(num1, num2, num3)
        print("Result: ", result)
    else:
        print("Invalid choice. Please choose between 1 and 2.")
        main()  # Повторный вызов функции 

if __name__ == "__main__":
    main()
    
    

    


