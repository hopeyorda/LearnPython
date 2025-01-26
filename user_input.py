#age = int(input("Enter Your age : "))


#print(f"Hello {name}")
#print(f"You are {age} years old.")

#Mad libs
adjective1 = input("Enter the first adjective : ")
adjective2 = input("Enter the second adjective : ")
adjective3 = input("Enter the third adjective : ")
noun = input("Enter a noun : ")
verb = input("Enter a verb : ")
print(f"Today I went to  a{adjective1} zoo.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2}  and {verb}ing")
print(f"I was {adjective3}")

#Area of Rectangle
length = int(input("Enter the length : "))
width = int(input("Enter the width : "))

Area = length * width
print(f"The Area  of the Rectangle is : {Area}")

#Shopping cart
item = input("What item would you like to buy? : ")
price = float(input("What is the price? : "))
quantity =int( input("How many would you like? : "))

total = price * quantity

print(f"You have bought {quantity} * {item}/s")
print(f"Your total is : ${round(total,2)}")