age = int(input("Enter your age: "))

if age < 0 or age > 120:
    print("Invalid age")
elif age >= 18:
    print("Valid age. You are eligible for voting")
else:
    print("Valid age. You are not eligible for voting")
