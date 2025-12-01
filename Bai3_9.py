# Chương trình máy tính thực hiện các phép tính đơn giản
# Program make a simple calculator that can add, subtract, multiply and divide using functions

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y  # Đã sửa từ '+' thành '-'

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4): ")  # Đã sửa dấu ngoặc và thêm 4
num1 = int(input("Enter first number: "))  # Đã sửa dấu chấm thành dấu hai chấm
num2 = int(input("Enter second number: "))  # Đã sửa dấu chấm thành dấu hai chấm

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))  # Đã sửa dấu phẩy và dấu chấm
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))  # Đã sửa dấu '+' thành '-' và sửa dấu chấm
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))  # Đã sửa dấu '+' thành '*' và sửa dấu chấm
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))  # Đã sửa dấu '+' thành '/' và sửa dấu chấm
else:
    print("Invalid input")