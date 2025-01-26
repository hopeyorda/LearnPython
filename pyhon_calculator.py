operator = input("Enter the operator : ")
A =int(input("Enter the first number : "))
B=int(input("Enter the second number : "))

if operator== "+":
    C = A + B
    print(f"The Sum of A and B is : {C}")
elif operator == "-":
    C= A-B
    print(f"The Subtraction of A and B is : {C}")
elif operator == "*":
    C = A * B
    print(f"The Product of A and B is : {C}")
elif operator =="/":
    C = A / B
    print(f"The division of A and B is : {C}")
else:
    print("Wrong Choice")

