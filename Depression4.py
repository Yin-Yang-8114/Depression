# question 01


while True:
    for i in range(1, 11):
        print(i)
    break

num =1
while num <= 10:
    print(num)
    num += 1

# question 02
while True:
    for i in range(10, 0, -1):
        print(i)
    print("START!")
    break
num = 10
while num >= 1:
    print(num)
    num -= 1
    # print("START!")

# question 03 


while True:
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)
    break

# question 04

while True:
    num = int(input("Enter a number: "))
    for i in range(1,5):
        print(num * i)
    break

# question 05

while True:
    sum = 0
    for i in range(1, 100):
        sum += i
    print("the sum of the first 100 numbers is", sum)
    break

# question 06

# password = "Python123"
# input_password = input("Enter the password: ")
# while input_password != password:
#     input_password = input("Enter the password: ")


while True:
    password = input("Enter the password: ")
    if password == "Python123":
        print("Welcome!")
        break

# question 07


while True:
    secret_number = 27
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        print("Try again!")

# question 08 


total_sum = 0
while True:
    number = int(input("Enter an integer O to stop: "))
    if number == 0:
        print(total_sum)
        break
    total_sum += number


#  question 09

total_grade = 0 
number_of_grades = 0
while True:
    grade = int(input("Enter a grade (or 999 to stop): "))
    if grade == 999:
        print("Number of grades entered:", number_of_grades)
        print("Sum of grades:", total_grade)
        print("Average of grades:", total_grade / number_of_grades if number_of_grades > 0 else 0)
        break
    total_grade += grade
    number_of_grades += 1


# question 10

