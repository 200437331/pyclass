import random
name = input("Enter your name: ")
salary =int(input("Enter your salary: $"))
print(f"{name}, your current salary is ${salary}.")
raise_per = random.randint(1, 100)
print(f"Your raise is {raise_per}% of ${salary}")
salary_percent = (salary * raise_per) / 100
raise_amount = salary + salary_percent
print(f"{name}, your new salary is ${raise_amount}.")