def add(x, y):
    """function to add two float numbers input by the user"""
    return x + y


def subtract(x, y):
    """function to subtract two float numbers input by the user"""
    return x - y


def multiply(x, y):
    """function to multiply two float numbers input by the user"""
    return x * y


def divide(x, y):
    """function to divide two float numbers input by the user, avoiding division by zero error"""
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")


def main():
    print("Choose what you want to do:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(add.__doc__)
        print("Result:", add(num1, num2))
    elif choice == "2":
        print(subtract.__doc__)
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        print(multiply.__doc__)
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        print(divide.__doc__)
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice!!")


if __name__ == "__main__":
    main()
