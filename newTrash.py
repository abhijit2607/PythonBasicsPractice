def factorial(num):
    if num < 1:
        return 1
    return num * factorial(num-1)

#__main__

num1 = int(input("Enter the number to find out its factorial: "))
print(f"The factorial of {num1} is {factorial(num)}")