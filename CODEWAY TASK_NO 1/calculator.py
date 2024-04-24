# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main function
def main():
    print("Welcome to Simple Calculator")
    while True:
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter operation choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
