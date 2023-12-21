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
        return "Cannot divide by zero"


while True:
    print("Do calculations: Press C")
    print("To Exit : Press E")
    choice = input("Enter choice: ")
    if choice == 'e' or choice == 'E':
        print("Exiting the calculator. Goodbye!")
        break
    elif choice == 'c' or choice == 'C':
        # Input numbers and operation choice
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter a valid choice.")
            continue

        # Perform calculation based on user's choice
        if choice == '1':
            result = add(num1, num2)
            operation = "addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "division"

        # Display the result
        print(f"The result of {operation} is: {result}\n")
        print("Do calculations again : Press C")
    else:
        print('invalid input: Try Again\n\n')
