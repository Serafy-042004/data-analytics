name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"


print("--- Lowercase Names ---")
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())


print("\n--- Title Case Names ---")
print(name_1.title())
print(name_2.title())
print(name_3.title())


print("\n--- Remove Currency Symbols ---")
salary_1_clean = salary_1.replace("$", "")
salary_2_clean = salary_2.replace("$", "")

print(salary_1_clean)
print(salary_2_clean)



salary_1_number = int(salary_1.replace("$", "").replace(",", ""))
salary_2_number = int(salary_2.replace("$", "").replace(",", ""))

print("\n--- Clean Salary Numbers ---")
print(salary_1_number)
print(type(salary_1_number))

print(salary_2_number)
print(type(salary_2_number))



total_salary = salary_1_number + salary_2_number

print("\n--- Total Salary ---")
print(f"Combined salaries: ${total_salary:,}")