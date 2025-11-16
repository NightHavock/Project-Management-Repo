def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def power(x, y):
    return x ** y


x = int(input("Enter your first number: \n"))
y = int(input("Enter your second number: \n"))
Calculation = input("Please select calculation type: add(1), subtract(2), divide(3), multiply(4), to the power of(5): \n")

if Calculation == "1" or Calculation.lower() == "add":
    result = add(x, y)
elif Calculation == "2" or Calculation.lower() == "subtract":
    result = subtract(x, y)
elif Calculation == "3" or Calculation.lower() == "divide":
    result = divide(x, y)
elif Calculation == "4" or Calculation.lower() == "multiply":
    result = multiply(x, y)
elif Calculation == "5" or Calculation.lower() == "to the power of":
    result = power(x, y)
else:
    result = "Invalid input"

print("Result:", result)
