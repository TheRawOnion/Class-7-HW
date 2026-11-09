age = int(input("Enter your age: "))
if age <= 20:
    print("Your age is below 20.")
else:
    print("Your age is above 20.")
    if age >= 10 and age <= 20:
        print("Your age is above 10 AND below 20.")
    elif age > 20 and age < 30:
        print("You are (kind of) old.")
    elif age < 10:
        print("Your age is below 10.")
    
if age > 100:
    print("You are not that old buddy.")