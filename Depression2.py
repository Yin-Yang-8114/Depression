# question 01

num1 = 25
num2 = 7

print("the sum of", num1, "and", num2, "is", num1 + num2)
print("the dubstraction of", num1, "and", num2, "is", num1 - num2)
print("the multiplication of", num1, "and", num2, "is", num1 * num2)
print("the division of", num1, "and", num2, "is", num1 / num2)
print("the modulus of", num1, "and", num2, "is", num1 % num2)
print("the exponentiation of", num1, "and", num2, "is", num1 ** num2)
print("the floor division of", num1, "and", num2, "is", num1 // num2)

# question 02

balance = 1000
balance += 250
print("the new balance is", balance)
balance -= 100
print("the new balance is", balance)
balance *= 2
print("the new balance is", balance)
balance /= 4
print("the new balance is", balance)

# question 03
num1 = int(input("im going to scream soon : "))
prosent = int(input("im losing my mind  : "))

price = num1 * (prosent / 100)
print("the price is", price)
dicounted_price = num1 - price
print("the discounted price is", dicounted_price)


# question 04
num1 = int(input("enter your bank account info : "))
anual_Interest = int(input("enter your interest rate : "))

new_balance = num1 * (anual_Interest / 100)
print("the new balance is", new_balance)


# question 05\
grade1 = float(input("enter your first grade : "))
grade2 = float(input("enter your second grade : "))
grade3 = float(input("enter your third grade : "))
average = (grade1 + grade2 + grade3) / 3
print("the average is", average)


# question 06
first_name = "Chaim"
last_name = "Sapir"
city = "jerusalm"

print(f"hello my name is  {first_name} {last_name}, and i want to To be buried in {city}!")
print("hello my name is" + first_name + " " + last_name + ", and i want to To be buried in " + city + "!")

# question 07

name = input("enter your name : ")
print(len(name))
print(name.lower())
print(name.upper())

# question 08
sentence = input("enter your sentence : ")
print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print(sentence.capitalize())


# question 09
name = input("enter your name : ")
print(name)
print(f" the length of your name is {len(name)}")
name.strip()
print(name)
print(f" the length of your name is {len(name)}")


# question 10

sentence = "I love Java programming"
sentence = sentence.replace("Java", "Python")
print(sentence)
print(sentence.count("love"))
print(sentence.startswith("I"))
print(sentence.endswith("programming"))


# question 11
word = "Programming"
print(word[0])
print(word[-1])
print(word[2])
print(word[:3])
print(word[-4:])
print(word[::-1])

# question 12

a = "100"
b = "25"
c = 10
d = 5.5

a = int(a)
b = float(b)
c = str(c)
d = int(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# question 13

age = input("Enter your age: ")
# print(age + 10) # becouse age is a string and you cannot add int to string


# question 14

price_before_vat = float(input("Enter the price before VAT: "))
price_after_vat = price_before_vat * 1.18
print(f"Price before VAT: {price_before_vat}\nPrice after VAT: {price_after_vat}")



# question 15

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))
years_of_experience = int(input("Enter your years of experience: "))
annual_salary = salary * 12
salary_after_increase = salary * 1.05
full_name_length = len(first_name + last_name)
print(f"Full Name: {first_name} {last_name}\nAge: {age}\nMonthly Salary: {salary}\nAnnual Salary: {annual_salary}\nSalary after 5% increase: {salary_after_increase}\nLength of Full Name: {full_name_length}")

# question 16
usd_rate = 3.25
shekel = int(input("enter price in ILS "))
print(f"the amount in Dollars is {shekel*usd_rate}")
ero_rate = 3.75
print(f"the amount in Euros is {shekel*ero_rate}")
print(f"the amount after 2% conversion fee is {shekel*usd_rate*1.02}")

# question 17

first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()
year_of_birth = int(input("Enter your year of birth: "))
print(f"{first_name}.{last_name}.{year_of_birth}@gmail.yayou.il.plastin.er.com.co.il.si.ll.iwant_to_go_HOME.com")


# question 18
sentence = input("Enter a sentence: ")
print(f"Original sentence: {sentence}")
print(f"Number of characters: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Reversed: {sentence[::-1]}")
print(f"Number of times 'a' appears: {sentence.count('a')}")
print(f"Sentence with spaces replaced by hyphens: {sentence.replace(' ', '-')}")



# fnal boooooooooooooooooooooooooooooooooosssssssssssssssss

"""
בנו תוכנית המדמה מערכת רכישה בחנות.
התוכנית תבקש מהמשתמש להכניס:
שם הלקוח.
שם המוצר.
מחיר המוצר.
כמות מוצרים.
אחוז הנחה.
אחוז מע"מ.
לאחר קבלת הנתונים, התוכנית תחשב ותציג חשבונית מסודרת.
החשבונית צריכה לכלול:
שם הלקוח.
שם המוצר באותיות גדולות.
מחיר יחידה.
כמות.
מחיר לפני הנחה.
סכום ההנחה.
מחיר לאחר הנחה.
סכום המע"מ.
מחיר סופי לתשלום.



"""
name_ = input("Enter your name: ")
product = input("Enter the product name: ").upper()
price = float(input("Enter the product price: "))
quantity = int(input("Enter the quantity: "))
discount = float(input("Enter the discount percentage: "))
vat = float(input("Enter the VAT percentage: "))
price_before_discount = price * quantity
discount_amount = price_before_discount * (discount / 100)
price_after_discount = price_before_discount - discount_amount
vat_amount = price_after_discount * (vat / 100)
final_price = price_after_discount + vat_amount
print(f"Customer Name: {name_}\nProduct Name: {product}\nUnit Price: {price}\nQuantity: {quantity}\nPrice Before Discount: {price_before_discount}\nDiscount Amount: {discount_amount}\nPrice After Discount: {price_after_discount}\nVAT Amount: {vat_amount}\nFinal Price to Pay: {final_price}")