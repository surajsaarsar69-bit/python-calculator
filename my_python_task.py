# taking input from the user
num1=float(input("enter first number"))
num2=float(input("enter second number"))


# performing mathematical operations
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2


print(f"addition is: {addition}")
print(f"subtraction is: {subtraction}")
print(f"multiplication is: {multiplication}")


if num2!=0:
    division=num1/num2
    print(f"division is: {division}")