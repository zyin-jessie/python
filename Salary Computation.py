print("BARTOLOME, JESSIE      2BSIT-1")

name = input("Enter employee name: ").upper()
hours = int(input("Enter number of hours: "))
sss = int(input("SSS contribution: "))
phil = int(input("Phil health: "))
loan = int(input("Housing loan: "))

rate_per_hour = 500
gross_salary = hours * rate_per_hour
tax = gross_salary * 0.10
total_deductions = sss + phil + loan + tax
net_salary = gross_salary - total_deductions

# Printing Payslip
print("\n==========PAYSLIP==========")
print("===EMPLOYEE  INFORMATION===")
print(f"Employee Name: {name}")
print(f"Rendered Hours: {hours}")
print(f"Rate per Hour: {rate_per_hour}")
print(f"Gross Salary: {gross_salary:.2f}")

print("\n=========DEDUCTION=========")
print(f"SSS: {sss}")
print(f"PhilHealth: {phil}")
print(f"Other Loan: {loan}")
print(f"Tax: {tax:.2f}")
print(f"Total Deductions: {total_deductions:.2f}")

print(f"\nNet Salary: PHP {net_salary:.2f}")
