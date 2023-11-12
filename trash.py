def fibonacci(n):
  if n<0:
    return 0
  return fibonacci(n-1) * fibonacci(n-2)

#__main__

num = int(input("Enter the nth term of the fibonacci series: "))
print(f"The {num}th term of the fibonacci series is: {fibonacci(num)}."))
