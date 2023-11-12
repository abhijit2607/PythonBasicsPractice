def fibonacci(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# __main__
num = int(input("Enter the nth term of the Fibonacci series: "))
print(f"The {num}th term of the Fibonacci series is: {fibonacci(num)}.")
