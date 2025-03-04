ITERATION = True

def display_student_average(name, math, english, science):
    print(f"\n{name}")
    print("\tMath = %.2f, English = %.2f, Science = %.2f" % (math, english, science))
    average = (math + english + science) / 3
    print("\tAverage = %.2f" % average)

studentRecord = []

print("BARTOLOME, JESSIE       2BSIT-1")

while ITERATION:
    studentName = str(input("Enter Student Name: "))
    mathGrade = int(input("Enter Grade (Math): "))
    englishGrade = int(input("Enter Grade (English): "))
    scienceGrade = int(input("Enter Grade (Science): "))

    studentDict = {
        "name": studentName,
        "math": mathGrade,
        "english": englishGrade,
        "science": scienceGrade
    }
    studentRecord.append(studentDict)

    continueLoop = input("Do you want to enter another student? [Y/N]: ").upper()

    if continueLoop == "N":
        ITERATION = False

for student in studentRecord:
    display_student_average(
        student.get("name"),
        student.get("math"),
        student.get("english"),
        student.get("science")
    )
