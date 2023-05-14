num1,num2=0,1
lst=[num1,num2]
while len(lst)<9:
    num3=num1+num2
    lst.append(num3)
    num1,num2=num2,num3
print("The required fibonacci series is:",lst)