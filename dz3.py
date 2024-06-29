def mile(a):
    return a / 1609.34

def yard(a):
    return a * 1.09361

def inch(a):
    return a * 39.3701

meters = float(input("Enter meters: "))

def main():
    try:
        meters = float(input("Enter meters: "))
    except ValueError:
        print("Enter only numbers")
        return

    print("Choose operation: ")
    print("1: convert meters to miles")
    print("2: convert meters to yards")
    print("3: convert meters to inches:")

choice = input("Choose (1, 2, 3): ")
    
if choice == "1":
    result = mile(meters)
    print("Result: ", result)
elif choice == "2":
    result = yard(meters)
    print("Result: ", result)
elif choice == "3":
    result = inch(meters)
    print("Result: ", result)
else:
    print("Invalid choice")


