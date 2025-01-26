user_name = input("Enter Your Name : ")

if len(user_name)>12 :
    print("Your username can't more than 12 character")
elif not user_name.find(" ")== -1:
    print("Your username can't contain space")
elif not user_name.isalpha():
    print("Your username can't contain digit")
else:
    print(f"Welcome {user_name}")