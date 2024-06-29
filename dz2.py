def max_numbers(a, b, c):
    return max(a, b, c)

def min_numbers(a, b, c):
    return min(a, b, c)

def average_numbers(a, b, c):
    return (a + b + c) / 3

def main():
    print("Enter three numbers: ")
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        num3 = float(input("Third number: "))
    except ValueError:
        print("Enter only numbers")
        return

    print("Choose operation: ")
    print("1: maximum of the numbers")
    print("2: minimum of the numbers")
    print("3: average of the numbers")

    choice = input("Choose (1, 2, 3): ")

    if choice == "1":
        result = max_numbers(num1, num2, num3)
        print("Result: ", result)
    elif choice == "2":
        result = min_numbers(num1, num2, num3)
        print("Result: ", result)
    elif choice == "3":
        result = average_numbers(num1, num2, num3)
        print("Result: ", result)
    else:
        print("Invalid choice")


main()
