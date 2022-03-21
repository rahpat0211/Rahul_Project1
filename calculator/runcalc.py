from calculator.operations import Addition, Subtraction, Multiplication, Division
from calculator.calculations import Addition as Add, Subtraction as Sub, Multiplication as Mul, Division as Div
from calculator import Calculator

print("Select an option to begin.")
print("Option 1: Addition")
print("Option 2: Subtraction")
print("Option 3: Multiplication")
print("Option 4: Division")

while True:
    # Get the user input
    option = input("Enter your option to begin: ")

    # Check if option is one of the four options
    if option in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == '1':
            print(num1, "+", num2, "=", Addition.add(num1, num2))

        elif option == '2':
            print(num1, "-", num2, "=", Subtraction.subtract(num1, num2))

        elif option == '3':
            print(num1, "*", num2, "=", Multiplication.multiply(num1, num2))

        elif option == '4':
            print(num1, "/", num2, "=", Division.divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (Y/N): ")
        if next_calculation == "N":
          break

    else:
        print("Invalid Input")





