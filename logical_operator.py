temp =float(input("Enter the temperature : "))
if (temp > 0) and (temp<30):
    print("Normal temperature")
elif (temp >30 ) or (temp < 60):
    print("Its normal.")
elif not (temp > 100):
    print("Cold!")

