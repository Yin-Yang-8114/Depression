# question 01

print("addolt"if int(input("Enter your age: "))>=18 else  "minor")


# question 02
print("positive" if (num1 := int(input("Enter your number: "))) > 0 else "negative" if num1 < 0 else "zero")

# question 03

print("even" if int(input("Enter your number: "))%2==0 else "odd")

# question 04

print(num1 if (num1 := int(input("Enter first number: "))) > (num2 := int(input("Enter second number: "))) else num2 if num2>num1 else "both numbers are equal")

# question 05
print("Access Granted." if input("Enter your password")=="Python123" else "Access Denied.")

# question 06
print("between 1 and 10" if (num := int(input("Enter your number: "))) in range(1,11) else "between 11 and 50" if num in range(11,51) else "between 51 and 100" if num in range(51,101) else "out of range")


# question 07

print("Excellent" if (grade := int(input("Enter your grade: "))) in range(90,101) else "Very Good" if grade in range(80,90) else "Good" if grade in range(70,80) else "Passed" if grade in range(60,70) else "Failed" if grade in range(0,60) else "Invalid Grade")

# question 08

print("Login Successful." if (username := input("Enter your username: ")) == "admin" and (password := input("Enter your password: ")) == "123456" else "Wrong Password." if username == "admin" else "Invalid Username.")

# question 09

print("the price after discount is", float(input("Enter the price of the product: ")) * (0.8 if (age := int(input("Enter your age: "))) > 60 else 0.9 if age < 18 else 1))

# question 10

print("divisible by 3" if (num := int(input("Enter a number: "))) % 3 == 0 and num % 5 != 0 else "divisible by 5" if num % 5 == 0 and num % 3 != 0 else "divisible by both 3 and 5" if num % 3 == 0 and num % 5 == 0 else "not divisible by either")
# question 11

print("Access Granted." if (age := int(input("Enter your age: "))) >= 18 or (age >= 16 and (accompanied := input("Are you accompanied by an adult? True/False: ")) == "True") else "Access Denied.")

# question 12

print("Eligible for scholarship." if (average_grade := float(input("Enter your average grade: "))) > 90 or (average_grade > 85 and (monthly_income := float(input("Enter your monthly income: "))) < 5000) else "Not eligible for scholarship.")

# question 13

print("Access Granted." if (username := input("Enter your username: ")) == "admin" and (password := input("Enter your password: ")) == "123456" and (account_active := input("Is your account active? True/False: ")) == "True" else "Access Denied.")

# question 14

print("The number is in the range of 20-80." if (num := int(input("Enter a number: "))) >= 20 and num <= 80 else "The number is out of the range of 20-80.")
print("The number is in the range of 20-80." if not (num := int(input("Enter a number: "))) < 20 and not num > 80 else "The number is out of the range of 20-80.")

# question 15

# I SURVUVED UNTILL HERE FROM HERE IM ALLREDY DEED ! 