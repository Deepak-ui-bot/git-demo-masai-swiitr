age = int(input("Enter your age: "))


if age < 18:
    print("You are a minor.")
    print("Deepak")
elif age >= 18 and age < 50:
    print("You are an adult.")
elif age == 50:
    print("You are middle-aged.")
    print("Deepak")
    print("You are eligible for senior citizen benefits.")
else:
    print("You are a senior citizen.")