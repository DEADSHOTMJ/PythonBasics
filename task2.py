while True:
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operator.")
            continue
        
        print("Result:", result)
        
        another = input("Do you want to perform another calculation? (yes/no): ")
        if another.lower() != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
