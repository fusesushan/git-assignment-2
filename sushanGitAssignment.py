def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
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
        print("The Result:", add(num1, num2))
    elif choice == "2":
        print("The Result:", subtract(num1, num2))
    elif choice == "3":
        print("The Result:", multiply(num1, num2))
    elif choice == "4":
        print("The Result:", divide(num1, num2))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
