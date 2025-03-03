print("BARTOLOME, JESSIE      2BSIT-1")
name = input("Enter employee name: ")
years = int(input("Enter years-in-service: "))
office = input("Enter office: ").lower()

bonus = 0

if office == "it":
    if years >= 10:
        bonus = 10000
    else:
        bonus = 5000
elif office == "acct":
    if years >= 10:
        bonus = 12000
    else:
        bonus = 6000
elif office == "hr":
    if years >= 10:
        bonus = 15000
    else:
        bonus = 7500
else:
    bonus = 0
    print("\nInvalid Office")

print(f"Hi, {name}, your bonus is {bonus}")
