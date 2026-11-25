# question 01

tuple1= (10,20,30,40,50)
print(tuple1)
print(tuple1[-1])
print(tuple1[0])
print(len(tuple1))
print(tuple1[2])


# question 02 

tuple1 =("chaim","ori","michael","gad","renana")
for i in tuple1:
    print(i)
print(name if (name:= input("Enter your name to serch ")) in tuple1 else "Not found")
print(len(tuple1))

# question 03 
tuple1 = (1,2,3,4,5,6,7,8,9,10)
print(tuple1[:3])
print(tuple1[-3:])
print(tuple1[:-1])


# question 04 and 5
tuple1 = ("Computer",1200,5,"Tech")
print(f"Item {tuple1[0]} , Price {tuple1[1]} quantity {tuple1[2]} Catogory {tuple1[2]}")

# question 06 

tuple1 = (1,2,3,4,5,6,7,8,9,10)
amount =0
for i in tuple1:
    amount += i
print(amount)


# question 07 
products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
print(tuple1:= products[:3])
print(tuple2:=products[-2:])
print(tuple2:=tuple1+tuple2)


# question 07 agin? 
dict1={"name":"chaim","age":22,"grade":100,"city":"tel aviv"}
for i in dict1:
    print(i)
for i in dict1:
    print(dict1[i])

# question 08 
car = {"brande":"volvo","model":"xc 60","year":2026,"price":346000}
car["price"]=367000
car["year"]=2027
car["color"]="forest green"
print(car)

# question 09 
salaries = { "David": 12000,"Moshe": 15000,"Dana": 13500}
for i in salaries:
    print(f"{i} {salaries[i]}") 

salaries["chaim"]=1000000000000000
print(salaries)


# question 10 
products = {"Laptop":1000, "Mouse":50, "Keyboard":500, "Screen":400, "Printer":830}
print(products[product] if (product:=input("Enter product to serch ")) in products else "Not found")

# question 11
dict1 ={"chaim":100,"ori":10,"michael":90,"gad":0,"renana":80}
for i in dict1:
    print(f"Student: {i} | Grade: {dict1[i]}")

# question 12
grades = {    "David": 90,    "Moshe": 75,    "Dana": 100,    "Noa": 55,    "Avi": 82}
for i in grades:
    if grades[i]>=80:
        print(i)
print(f"{sum([grades[i] for i in grades])}/{len(grades)}")
highest = grades[i]
for i in grades:
    if grades[i] > highest:
        highest = grades[i]
print(highest)
fiald= 0
for i in grades:
    if grades[i] <60:
        fiald+=1
print(f'Stodent faild {fiald}')

# question 13

products = {"Laptop":1000, "Mouse":50, "Keyboard":500, "Screen":400, "Printer":830}
product=input("Enter product to serch ")
for i in products:
    if i==product:
        price=input("Enter updated price ")
        products[product]=price
        break
else:
    products[product]=input("Enter price ")
print(products)

# question 14
students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
# for i in students:
#     print(i["name"])

# for i in students:
#     print(i["grade"])
print([i["name"] for i in students])
print([i["grade"] for i in students])
print([i["name"] for i in students if i["grade"]>=80])
print(f"{sum([i["grade"] for i in students])/len(students)}")
highest = students[0]["grade"]
for i in students:
    if i["grade"] > highest:
        highest = i["grade"]
print(highest)

# question 15
students = [    {"name": "David", "age": 20, "grade": 90},    {"name": "Moshe", "age": 22, "grade": 75},    {"name": "Dana", "age": 21, "grade": 100},    {"name": "Noa", "age": 19, "grade": 55},    {"name": "Avi", "age": 23, "grade": 82}]
students.append({"name":"Chaim","age":22,"grade":100})
students[0]["grade"] = 30

# delete_name = input("Enter name to delete: ")
# for i in students:
#     if i["name"]==delete_name:
#         students.remove(i)
#         break
delete_name = input("Enter name to delete: ")
students = [s for s in students if s["name"] != delete_name]
print(students)

# question 16
classroom = {"Class A": ["David", "Moshe", "Dana"],"Class B": ["Noa", "Avi", "Michael"],    "Class C": ["Daniel", "Shir", "Yossi"]}
for i in classroom:
    print(i)
print(*classroom["Class A"], sep="\n")
classroom["Class B"].append("Chaim")
classroom["Class C"].pop()

print(classroom)

# question 17 
products = {    "Laptop": {        "price": 4500,        "stock": 10    },    "Mouse": {        "price": 80,        "stock": 50    },    "Keyboard": {        "price": 150,        "stock": 20    }}
for product in products:
    print(f"{product} price: {products[product]['price']}")
print(*[products[product]['price'] for product in products],sep='\n')
for product in products:
    print(f"{product} stock: {products[product]["stock"]}")
print(*[products[product]["stock"] for product in products],sep="\n")
products["Laptop"]["stock"]=9
products["Printer"]={"price":900,"stock":1}
print(*[product for product in products if products[product]["price"]>=100],sep="\n")

# question 18 
employees = [    ("David", "Development", 15000),    ("Moshe", "Marketing", 12000),    ("Dana", "Development", 18000),    ("Noa", "HR", 11000)]
print(*[employ[0] for employ in employees],sep="\n")
print(*[employ[0] for employ in employees if employ[1]=="Development"],sep="\n")
print([employ for employ in employees if employ])

highest_salary = employees[0][2]
highest_employee = employees[0][0]
for employ in employees:
    if employ[2] > highest_salary:
        highest_salary = employ[2]
        highest_employee = employ[0]
print(highest_employee, highest_salary)
print(f"{sum([employ[2] for employ in employees])/len(employees)}")


# question 19
inventory = {    "Laptop": 10,    "Mouse": 50,    "Keyboard": 20}
product = input("Enter product to buy ")
amount = int(input("How much you want to buy "))
if product in inventory and inventory[product] > amount:
    inventory[product]-=amount
print(inventory)

# question 20
votes = {"David": 0,"Moshe": 0,"Dana": 0}
while True:
    print(*votes,sep="\n")
    chose = input("Please coose person to vote to or stop to stop :")
    if chose == "stop":
        break
    for i in votes:
        if i == chose:
            votes[chose]+=1
print(votes)
viner = 0
viner_name =""
for vote in votes:
    if votes[vote] > viner:
        viner = votes[vote]
        viner_name = vote

print(f"The winner is {viner_name} with {viner} votes")



# question 21
dict1 = {"Chaim":"0548234959","michael":"0533140466"}
while True:
    print("""
    1. Add Contact Person
    2. Serch Contact Person
    3. Update Contact Person
    4. Delete Contact Person
    5. Print all Contact Person
    6. Exit
""")
    choice = input("Please coose between 1-6: ")
    match choice:
        case "1":
            contact = input("Please enter contact name ")
            phone = input("Please enter contact phone number ")
            dict1[contact]=phone
        case "2":
            contact_to_serch = input("Please enter contact name to serch ")
            for i in dict1:
                if i == contact_to_serch:
                    print(dict1[i])
                    break
            else:
                print("Contact not found ")
        case "3":
            contact_to_serch = input("Please enter contact name to serch ")
            for i in dict1:
                if i == contact_to_serch:
                    dict1[i]=input("Enter a new phone number ")
                    break
            else:
                print("Contact not found ")
        case "4":
            contact_to_serch = input("Please enter contact name to serch ")
            dict1.pop(contact_to_serch)
        case "5":
            print(*[f"{name} {phone}" for name,phone in dict1.items()],sep="\n")
            for name,phone in dict1.items():
                print(f"Name {name} | Pohne {phone}")
        case "6":
            print("Goodby ")
            break