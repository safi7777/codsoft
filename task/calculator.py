def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")

    while True:
        try:
            # Prompt user for the first number
            num1 = float(input("Enter the first number: "))

            # Prompt user for the second number
            num2 = float(input("Enter the second number: "))
           
            # Prompt user for the operation choice
            print("Select operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = input("Enter the operation number (1/2/3/4): ")

            # Perform the calculation based on user choice
            if choice == '1':
                result = add(num1, num2)
                print(f"The result of {num1} + {num2} is: {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"The result of {num1} - {num2} is: {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"The result of {num1} * {num2} is: {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"The result of {num1} / {num2} is: {result}")
            else:
                print("Invalid input! Please enter a number between 1 and 4.")
           
            # Option to continue or exit
            cont = input("Do you want to perform another calculation? (y/n): ").lower()
            if cont != 'y':
                break

        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()