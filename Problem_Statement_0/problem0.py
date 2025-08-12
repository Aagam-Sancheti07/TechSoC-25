def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def power(a,b):
    return a**b
def root(a,b):
    return a**(1/b)
def sin(c):
    -1.57<=c<=1.57
    return c-(c**3)/6+(c**5)/120-(c**7)/5040
def cos(c):
    0<=c<=3.14
    return 1-(c**2)/2+(c**4)/24-(c**6)/720
def tan(c):
    -1.57<c<1.57
    return sin(c)/cos(c)
def cot(c):
    0<c<3.14
    return 1/tan(c)
def sec(c):
    0<=c<=3.14 
    return 1/cos(c)
def cosec(c):
    -1.57<=c<=1.57
    return 1/sin(c)
def inverse_sin(c):
    if not (-1 <= c <= 1):
        raise ValueError("Input out of range for inverse sin")
    return c + (c**3)/6 + (3*c**5)/40 + (5*c**7)/112
def inverse_cos(c):
    if not (-1 <= c <= 1):
        raise ValueError("Input out of range for inverse cos")
    return 3.14/2 - (c + (c**3)/6 + (3*c**5)/40 + (5*c**7)/112)
def inverse_tan(c):
    if not (-1 <= c <= 1):
        raise ValueError("Input out of range for inverse tan")
    return c + (c**3)/3 + (2*c**5)/15 + (17*c**7)/315
def inverse_cot(c):
    if not (-1 <= c <= 1):
        raise ValueError("Input out of range for inverse cot")
    return 3.14/2 - (c + (c**3)/3 + (2*c**5)/15 + (17*c**7)/315)
def inverse_sec(c):
    if not (c > 1 or c < -1):
        raise ValueError("Input out of range for inverse sec")
    return 3.14/2 - (c + (c**3)/6 + (3*c**5)/40 + (5*c**7)/112)
def inverse_cosec(c):
    if not ( c > 1 or c < -1):
        raise ValueError("Input out of range for inverse cosec")
    return c + (c**3)/6 + (3*c**5)/40 + (5*c**7)/112
def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Invalid input for logarithm")
    return ((a-1)-(a-1)**2/2+(a-1)**3/3-(a-1)**4/4)/((b-1)-(b-1)**2/2+(b-1)**3/3-(b-1)**4/4)
def exp(a):
    if a < 0:
        raise ValueError("Input for exponential must be non-negative")
    return 1 + a + (a**2)/2 + (a**3)/6 + (a**4)/24 + (a**5)/120 + (a**6)/720
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
def ln(a):
    if a <= 0:
        raise ValueError("Input for natural logarithm must be positive")
    return log(a, 2.7182)  
print("Welcome to the calculator program!")
print("choose between Basic/Advanced/Trignometry")
choice = input("Enter your choice: ").strip()
if choice == "Basic":
    print("Basic Operations: Addition, Subtraction, Multiplication, Division, Power, Root")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)") 
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Root ")
    operation = input("Enter the operation you want to perform(1,2,3,4,5,6): ").strip()
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    
    if operation == "1":
        print("Result:", {add(a,b)})
    elif operation == "2":
        print("Result:", {sub(a,b)})
    elif operation == "3":
        print("Result:", {mul(a,b)})
    elif operation == "4":
        if b != 0:
            print("Result:", {div(a,b)})
        else:
            print("Error: Division by zero is not allowed")
    elif operation == "5":
        print("Result:", {power(a,b)})
    elif operation == "6":
        print("Result:", {root(a,b)})
    else:
        print("Invalid operation")
elif choice =="Trignometry":
    print("Trignometric Equation: Sin, cos, tan etc")
    print("1. Sin")
    print("2. Cos")
    print("3. Tan")
    print("4. Cot")
    print("5. Sec")
    print("6. Cosec") 
    print("7. Inverse Sin")
    print("8. Inverse Cos")
    print("9. Inverse Tan")
    print("10. Inverse Cot")
    print("11. Inverse Sec")
    print("12. Inverse Cosec") 
    operation = input("Enter the operation you want to perform(1,2,3,4,5,6....): ").strip()  

    a = float(input("Enter the angle in principal radians/number(for inv): ")) 

    if operation == "1":
        print("Result:", {sin(a)})
    elif operation == "2":
        print("Result:", {cos(a)})
    elif operation == "3":
        print("Result:", {tan(a)})
    elif operation == "4": 
        print("Result:", {cot(a)})
    elif operation == "5":
        print("Result:", {sec(a)})
    elif operation == "6":
        print("Result:", {cosec(a)})
    elif operation == "7" and a != 0: 
        print("Result:", {inverse_sin(a)})
    elif operation == "8" and a != 1.57:
        print("Result:", {inverse_cos(a)})
    elif operation == "9" :
        print("Result:", {inverse_tan(a)})
    elif operation == "10" :
        print("Result:", {inverse_cot(a)})
    elif operation == "11":
        print("Result:", {inverse_sec(a)})
    elif operation == "12":
        print("Result:", {inverse_cosec(a)})
    else:
        print("Invalid operation")
elif choice == "Advanced":
    print("Advanced Operations: Logarithm, Exponential, Factorial")
    print("1. Logarithm")
    print("2. Natural Logarithm")
    print("3. Exponential")
    print("4. Factorial")
    operation = input("Enter the operation you want to perform(1,2,3,4): ").strip()
    
    if operation == "1":
        
        a = float(input("Enter the number: "))
        b = float(input("Enter the base: "))
        if a > 0 and b > 0 and b != 1:
            print("Result:", {log(a, b)})
        else:
            print("Error: Invalid input for logarithm")
    elif operation == "2":
        a = float(input("Enter the number: "))
        if a > 0:
            print("Result:", {ln(a)})
        else:
            print("Error: Input for natural logarithm must be positive")
    elif operation == "3":
        a = float(input("Enter the number: "))
        if a >= 0:
            print("Result:", {exp(a)})
        else:
            print("Error: Input for exponential must be non-negative")
    elif operation == "4":
        n = int(input("Enter a non-negative integer: "))
        if n >= 0:
            print("Result:", {factorial(n)})
        else:
            print("Error: Factorial is not defined for negative numbers")
    else:
      print("Invalid operation")
else:
    print("Invalid choice. Please choose Basic, Advanced, or Trignometry")

review = input("How much would you rate this calculator out of 5?")
if review == "5":
    print("Thank you for your positive feedback!")
elif review == "4":
    print("Thank you! I am glad you liked it")
elif review == "3":
    print("Thank you! I will try to improve it further")
elif review == "2":
    print("I am sorry. Next time I will work with more dedication")
elif review == "1":
    print("I am extremely sorry. I will do my best so next time you like it")
else:
    print("Bhaiya pls majak mat karo")
print("Thank you for using the calculator!")
print("Have a great day!")