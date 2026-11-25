# num1= [2,4,6,8]
# for n in num1:
#     if n % 2 ==0:
#         num1.remove(n)
# print(num1)

# num1= [2,4,6,8]
# for i in range(len(num1)):
#     if num1[i]%2==0:
#         num1.remove(num1[i])

# print(num1)




# for i in range(5):
#     print(i)

# for i in range(1,5):
#     print(i)


# list1 = [1, 2, 3, 1]
# sum2 = 0
# sum1 = [sum2 := sum2 + i for i in list1]
# print(sum2)
# print([sum2 :=i for i in list1])

# products = {"Laptop":1000, "Mouse":50, "Keyboard":500, "Screen":400, "Printer":830}
# for i in products:
#     if products[i]==(product:=input("Enter product to serch"):

# list1= [(1,"A"),(1,"B"),(2,"B"),(2,"A")]
# print(sorted(list1,key=lambda x : x[1]))

# question 20 

# products = [    {"name": "Laptop", "price": 4500, "stock": 10},    {"name": "Mouse", "price": 80, "stock": 50},    {"name": "Keyboard", "price": 150, "stock": 20},    {"name": "Screen", "price": 900, "stock": 15}]

# while True:
#     print("""
# ===== Store Management =====

# 1. Show all products
# 2. Add product
# 3. Search product
# 4. Update product price
# 5. Update product stock
# 6. Sell product
# 7. Show products by price
# 8. Show products with low stock
# 9. Show total inventory value
# 0. Exit
# """)
#     choice = input("Enter a number between 1-9. 0-to exit ")
#     match choice:
#         case "1":
#             for product in products:
#                 print(f"Name : {product["name"]} Price : {product["price"]} Stock {product["stock"]}")
#         case "2":
#             product_to_serch = input("Please enter product name to serch ")
#             if any(product["name"]==product_to_serch for product in products):
#                 print(products[product_to_serch])


products = [    {"name": "Laptop", "price": 4500, "stock": 10},    {"name": "Mouse", "price": 80, "stock": 50},    {"name": "Keyboard", "price": 150, "stock": 20},    {"name": "Screen", "price": 900, "stock": 15}]

while True:
    print("""
===== Store Management =====

1. Show all products
2. Add product
3. Search product
4. Update product price
5. Update product stock
6. Sell product
7. Show products by price
8. Show products with low stock
9. Show total inventory value
0. Exit
""")
    choice = input("Enter a number between 1-9. 0-to exit ")
    match choice:
        case "1":
            for product in products:
                print(f"Name : {product["name"]} Price : {product["price"]} Stock {product["stock"]}")
        case "2":
            product_to_serch = input("Please enter product name to serch ")
            product = next((product for product in products if product["name"]==product_to_serch) ,None)
            if product:
                print(f"Name: {product['name']}, Price: {product['price']} Amount: {product['stock']}")
            else:
                print("Product not found")
            