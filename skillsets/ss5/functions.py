def get_requirements():
    print("\nDeveloper: Aliya Gamez")
    print("Python Selection Structures")
    print("\nProgram Requirements:"
          + "\n1. Use Python selection struture."
          + "\n2. Prompt user for two numbers, and a suitable operator."
          + "\n3. Test for correct numeric operator."
          + "\n4. Replicate display below.\n")
    
def calculate_python_selection_structures():
    num1 = 0
    num2 = 0
    operator = ''
    result = 0.0
    
    print("Python Calculator")
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    
    print("\nSuitable Operators: +, -, *, /, // (integer divsion), % (modulo operator), ** (power)")
    while True:
        operator = str(input("Enter operator: "))
        if (operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '//' or operator == '%' or operator == '**'):
            if (operator == '+'):
                result = num1 + num2
            elif (operator == '-'):
                result = num1 - num2
            elif (operator == '*'):
                result = num1 * num2
            elif (operator == '/'):
                result = num1 / num2
            elif (operator == '//'):
                result = num1 // num2
            elif (operator == '%'):
                result = num1 % num2
            else:
                result = num1 ** num2
            break
        else:
            print("Incorrect operator!\n")
    print('{0:.1f}'.format(result))
    