class Calculator:

    def __init__(self) -> None:
        pass

    def add(self, x, y):
        ''' A function that adds two numbers.'''
        return x + y

    def subtract(self, x, y):
        ''' A function that subtracts two numbers.'''
        return x - y

    def multiply(self, x, y):
        ''' A function that multiplies two numbers.'''
        return x * y

    def divide(self, x, y):
        ''' A function that divides two numbers'''
        return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Please, enter your choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f'{num1} + {num2} = {Calculator.add(0, num1, num2)}')

        elif choice == '2':
            print(f'{num1} - {num2} = {Calculator.subtract(0, num1, num2)}')
        
        elif choice == '3':
            print(f'{num1} * {num2} = {Calculator.multiply(1, num1, num2)}')

        elif choice == '4':
            print(f'{num1} / {num2} = {Calculator.divide(0, num1, num2)}')
    
        next_operation = input("Do you want to do another operation? (yes/no): ")
        if next_operation == 'no':
            break
        elif next_operation not in ('no', 'yes'):
            print("Invalid Input")
            break