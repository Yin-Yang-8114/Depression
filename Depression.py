# question 01

first_name = "muchamad"
last_name = "def"
age =10000000000000000000000
city = "bite chanone"
email= "m.d@chamas.teror.com"

print(f"First Name: {first_name}\n Last Name: {last_name}\n Age: {age}\n City: {city}\n Email: {email}")


# qustion 02

birthday_year = 1840
currenr_year = 1939

print("you are aproximately", currenr_year - birthday_year, "years old")

# question 03

wide = 10
height = 20

print("the area of the rectangle is", wide * height)
print("the perimeter of the rectangle is", 2 * (wide + height))


# question 04

name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(salary))

# question 05
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"First Name: {first_name}\n Last Name: {last_name}\n Age: {age}\n City: {city}")


# question 06

num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))

print("the sum of", num1, "and", num2, "is", num1 + num2)
print("the difference of", num1, "and", num2, "is", num1 - num2)
print("the product of", num1, "and", num2, "is", num1 * num2)
print("the quotient of", num1, "and", num2, "is", num1 / num2)

# question 07

name_of_pruct = input("Enter the name of the product: ")
price_of_product = float(input("Enter the price of the product: "))
quantity_of_product = int(input("Enter the quantity of the product: "))

print(f"Product: {name_of_pruct}\nPrice: {price_of_product}\nQuantity: {quantity_of_product}\nTotal: {price_of_product * quantity_of_product}")

# question 09

worker_name = input("Enter the worker's name: ")
hours_worked = float(input("Enter the number of hours worked: "))
per_hour_rate = float(input("Enter the pay rate per hour: "))

print(f"Worker Name: {worker_name}\nHours Worked: {hours_worked}\nPay Rate: {per_hour_rate}\nTotal Salar: {hours_worked * per_hour_rate}")


# question 10
bill_percent = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))
number_of_people = int(input("Enter the number of people: "))

print(f"Bill Amount: {bill_percent}\nTip Percentage: {tip_percent}\nNumber of People: {number_of_people}\nTotal Tip: {bill_percent * (tip_percent / 100)}\nTotal Bill: {bill_percent + (bill_percent * (tip_percent / 100))}\nAmount per Person: {(bill_percent + (bill_percent * (tip_percent / 100))) / number_of_people}")

# question 12
a = 10
b = 20

c = a
a = b
b = c

print("After swapping: a =", a, "b =", b)


# final boos !!!!!!!!!!!!!!!!!!
student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))
institution_name = input("Enter your institution name: ")
course_name = input("Enter your course name: ")
course_duration = input("Enter the course duration: ")
monthly_price = float(input("Enter the monthly price: "))


print(f"Student Name: {student_name}\nAge: {student_age}\nInstitution Name: {institution_name}\nCourse Name: {course_name}\nCourse Duration: {course_duration}\nMonthly Price: {monthly_price}\nTotal Cost: {monthly_price * int(course_duration.split()[0])}")