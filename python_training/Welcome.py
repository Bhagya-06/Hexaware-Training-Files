'''print ("**********************************")
print ("* Welcome to the Smart Library! *")
print ("**********************************")

student_record = {
    "id": 12345,
    "name": input("Enter student name: "),
    "fine_amount": 50.0}

print("\nStudent Record:")
print("Student ID:", student_record["id"])
print("Student Name:", student_record["name"])
print("Fine Amount:", student_record["fine_amount"])'''

#String Functions ----------------------
'''opt1='Hi'
opt2="Hi"
opt3="Hi"
opt4="""Hi"""
str("Hello")
word = "Alphabet"
print(word[-1])
text="Library Management"
print(text[0:7]) #Library
print(text[7:]) # Management
print(text[:7]) #Library
print(text[::2]) #LbayMngmn
print(text[::-1])
print(text.replace("Library", "Vendor"))
print(text)
print(text.find('z')) #-1 cuz not there
print(text.index('b'))
print(text.startswith("Lib"))
print(text.endswith("ment"))
print(text.upper())

newText = "Hello Hi Hello How are you?"
print(newText.count("Hello"))
print(newText.split(" "))

languages = ["Python", "Java", "C++", "JavaScript"]
print(",".join(languages))'''

'''name = input("Enter your name: ")
print(name.isalpha())  #True if all characters are letters
phone = input("Enter your phone number: ")
print(phone.isdigit())  #True if all characters are digits
username = input("Enter a username: ")
print(username.isalnum())  #True if all characters are letters or digits
print(name.center(20, "*"))  #Center the name with a width of 20 and fill with '*'
print(name.ljust(20, "-"))  #Left justify the name with a width of 20 and fill with '-'
print(name.rjust(20, "."))  #Right justify the name with a width of 20 and fill with '.' 
print("25".zfill(5))  #Pad the number with zeros to a width of 5
print("mypassword".encode("utf-8"))  #Encode the password using UTF-8 encoding (secure for real use)

mypartitiontext = "Welcome-to-the-Smart-Library"
print(mypartitiontext.partition("-"))  #Partition the text at the first occurrence (splits in 3 and gives tuple as result)

name = "Bhagya"
print(f"Welcome {name}!") 
print("My name is {}".format(name))  '''

#TASK
'''taskString = " Python Programming "
# remove the space from head and end,
# convert every character to capital,
# change python to java,
# check how many times m occurrence
print(taskString.strip())
print(taskString.upper())
print(taskString.replace("Python", "Java"))
print(taskString.count("m"))'''

#List Functions -----------------------------------
'''book_names = ["python", "java", "c++", "javascript"]
print(book_names[1:2])
book_names[2] = "C#"
print(book_names)
book_names.append("ruby")
print(book_names)
book_names.insert(1, "go")
print(book_names)
book_names.extend(["mongoDB", "sql"])
print(book_names)
book_names.pop() #removes last element
print(book_names)
book_names.pop(5) #removes element at index 5
print(book_names)
book_names.remove("go")
print(book_names)
book_names.sort()
print(book_names)
book_names.sort(reverse=True)
print(book_names)
book_names.reverse()
print(book_names)
book_copies = book_names.copy()
print(book_copies)
book_copies.clear()
print(book_copies)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
print(list1 * 2)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[0])
print(matrix[0][1]) '''

#List Comprehension - shorter way to create lists -----------------
'''even = [x for x in range(1,11) if x % 2 == 0]
print(even)
odd = [x for x in range(1,11,2)]
print(odd)'''

#Dictionary Functions ------------------------------
''' student_record = {
    "id": 12345,
    "name": "Bhagya",
    "book_name": "Python Programming"
}
print(student_record["name"])
print(student_record.get("book_name")) #safer than above cuz it won't throw error if key not found
student_record["fine_amount"] = 50.0
print(student_record)
student_record.pop("id")
print(student_record)
removed_item = student_record.popitem() #returns and removes last inserted item
print("Removed item:", removed_item)
print(student_record)
del student_record["book_name"] #doesnt return removed item
print(student_record)
print(student_record.keys())
print(student_record.values())
print(student_record.items()) 

for key, value in student_record.items():
    print(key, ":", value)
'''

#Nested Dictionaries ------------------------------
'''students = {
    12345: {"name": "Bhagya", "book_name": "Python Programming"},
    67890: {"name": "Alice", "book_name": "Java Programming"},
    54321: {"name": "Bob", "book_name": "C++ Programming"}
}
print(students[12345]["name"]) 

for student_id, student_info in students.items():
    print("Student ID:", student_id)
    for key, value in student_info.items():
        print(key, ":", value)'''

#TASK
'''
# create a dictionary to store book information on book_id,title,author
# price with your own values.add new key available with boolean, update the book price increased with 200 from your original price,remove the author
# check the book is available. the add multiple books to your dictionary and count the total no of books in the dictionary

book = {
    "id": 1,
    "title": "Python Programming",
    "author": "John Doe",
    "price": 25.99,
}
book["is_available"] = True
book["price"] = 225.00
book.pop("author")
print(book)
print(book["is_available"])

books = {
    1: {"id": 1, "title": "Python Programming", "author": "John Doe", "price": 25.99},
    2: {"id": 2, "title": "Java Programming", "author": "Jane Smith", "price": 30.99},
    3: {"id": 3, "title": "C++ Programming", "author": "Alice Johnson", "price": 20.99}
}
count = 0
for book in books:
    count += 1
print("Number of books:", count)'''

#Sets ---------------------------------------
'''l = {} #this is a dictionary not a set because set is defined using set() function or using {} with values inside it. {} alone creates an empty dictionary
print(type(l))
mailid = {"bhagya@gmail.com", "alice@gmail.com", "bob@gmail.com", "alice@gmail.com"}
print(mailid) #duplicates removed and sorted in Set
mailid.add("test@gmail.com")
print(mailid)
mailid.update(["test1@gmail.com", "test2@gmail.com"])
print(mailid)
mailid.remove("test@gmail.com")
print(mailid)
mailid.discard("test1@gmail.com")
print(mailid)
mailid.pop() #removes random element
print(mailid)'''

#Set Operations ---------------------------------------
'''a={1,2,3,4}
b={1,6,7,8}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

c={1,6}
print(c.issubset(b))
print(b.issuperset(c))

student_age = [20, 24, 26, 28, 23, 22, 20]
unique_age = set(student_age)
print(unique_age)'''

#Maps -------------------------------------------
''' a=[1,2,3,4]
b=[]
for x in a:
    b.append(x*2)
print(b)
#(or)
result = map(lambda x:x*2,a)
print(list(result))
#(or)
def square(x):
    return x*2
result1 = map(square,a)
print(list(result1))'''

#TASK
'''# prices=[100,200,300] updated=[]
# updated should have 50 rs added to the original price
# do both lambda and function
prices = [100,200,300]
updated = map(lambda x:x+50,prices)
print(list(updated))

def addprice (x):
    return x+50
updated1 = map(addprice,prices)
print(list(updated1))

book_names=["python", "java", "ca"]
bookUpper=map(str.upper, book_names)
print(list(bookUpper))
prices=[100,200,300]
tax=[10,20,30]
bookprice=map(lambda x,y:x+y, prices, tax)
print(list(bookprice))

books=[
    {"title":"Python","price":100},
    {"title":"Java","price":200}
]
updatedBook = map(lambda x:{
    "title": x["title"], "price":x["price"]+50
}, books)
print(list(updatedBook))'''

#TASK
'''#book_names=["python","java","c#"] find the length of every bookname
book_names=["python","java","c#"]
namelength = map(lambda x:len(x),book_names)
print(list(namelength))'''

#TASK
'''price=[100,500,700]
result=filter(lambda x:x>300,price)
print(list(result))

from functools import reduce
total = reduce(lambda x,y:x+y,price)
print(total)'''

#TASK
'''books = [
    {"title": "Python", "price": 500, "available": True},
    {"title": "Java", "price": 800, "available": False},
    {"title": "AI", "price": 1200, "available": True},
    {"title": "Cloud", "price": 300, "available": True},
    {"title": "Data Science", "price": 1500, "available": False}
]

#1.Filter only the books that are available
# 2.increase the price of available books by 100
# 3.find the total price of updated books
# 4.print only book titles
# 5.find the highest priced book

availablebooks = list(filter(lambda x:x["available"]==True,books))
print(availablebooks)
updated = list(map(lambda x:x["price"]+100,availablebooks))
print(updated)
from functools import reduce
total = reduce(lambda x,y:x+y,updated)
print(total)
titles = list(map(lambda x:x["title"],books))
print(titles)
highest = max(map(lambda x:x["price"],books))
print(highest)'''

#Number functions ----------------------------------------------
'''price=999
discountPrice=price * 0.1
print(discountPrice)
print(round(discountPrice,2))
print(sum(cost))
print(sorted(cost))
print(list(reversed(cost)))
print(4%3)
print(divmod(4,3))
print(math.sqrt(5))
print(math.floor(10.635))'''

#Datetime functions --------------------------------------------------
'''import datetime
print(datetime.datetime.now().timestamp())
print(datetime.date.today())
customized_date=datetime.date(2025,3,26)
print(customized_date)
# %Y, %m, %d, %H, %M, %S, %A, %B
print(customized_date.strftime("%d - %B - %Y"))
print(datetime.datetime.now().strftime("%H - %I %p"))
import datetime
dob = "23-May-2026"
date_obj = datetime.datetime.strptime(dob, "%d-%b-%Y")
print(date_obj)'''

#TASK
'''price = 999
discount = price * 0.10
print(round(discount,2))
import datetime
issue_date = datetime.date(2026, 5, 5)
submitted_date = datetime.date(2026, 5, 22)
fine_amount = 10
late_days = (submitted_date - issue_date).days - 5
if late_days > 0:
    fine = late_days * fine_amount
else:
    fine = 0
print(fine)        
print(late_days)'''

#TASK
'''def greet(name,bname):
    print(f"Reader: {name}\nBook name: {bname}")
username=input("ur name: ")
bookname=input("book name:")
greet(username,bookname)

def greet(name,gender):
    if gender=="m":
        return "Mr. " + name
    else:
        return "Ms. " + name
print(greet("likhitha",'f'))

days=int(input("Days: "))

def fine(days):
    return days*10

print("Total Fine Amount is ",fine(days))

def greet(name="Guest"):
    print("welcome", name)

username = input("enter your name")
greet()
greet("John")

def memberInformation(name,age):
    print("MemberName",name)
    print("Age",age)
    memberInformation(age=21, name="Likhi")

def calculateTotal(*numbers):
    return sum(numbers)
print(calculateTotal(40,70,90))

#|                interview question can be asked |
#|                                                |
#|                     *args vs **kwargs          |

def Books(*books):
    return books
print(Books("CS", "ML", "AI", "DS", "Robotics"))

def student(**details):
    print("Name:", details.get("name"))
    print("Age:", details.get("age"))
    print("Course:", details.get("course"))
student(name="Dodo", age=21, course="Python")'''

#Higher Order functions -------------------------------------------
'''def execute(operation):
    print("From execute function....")
    operation()

def calculate_fine():
    print("I calculate fine amount")

def register_candidate():
    print("I register candidates")  

execute(calculate_fine) #can pass functions as input
execute(register_candidate)'''

#Nested Functions ------------------------------------------
'''def library_role(role):
    def admin():
        print("Admin Access")
    return admin()

library_role("admin")'''

#TASK
'''#Create
#one function to search by book name
#one function to search by author
#one Higher Order Function to execute search dynamically

def booksearch():
    print("Searching by book....")

def authorsearch():
    print("Searching by author....")

def executesearch(operation):
    print("Executing search dynamically")
    operation()

executesearch(booksearch)
executesearch(authorsearch)'''

#TASK
'''#MEMBERSHIP ACCESS USING RETURN FUNCTION
#Return different functions based on membership type gold or silver

def membershipaccess(membership):
    def goldmember():
        print("You have access to Gold Membership")
    def silvermember():
        print("You have access to Silver Membership")
    if(membership=="gold"): return goldmember()
    elif(membership=="silver"): return silvermember()
    else: print("Not a valid member")

membershipaccess("gold")
membershipaccess("silver")
membershipaccess("diamond")'''

#TASK
'''#INNER FUNCTION FOR LOGIN VALIDATION
#Create:
#outer function → login_system()
#inner function → validate_user()

def login_system():
    def validate_user(username, password):
        if username == "admin" and password == "password123":
            return True
        else:
            return False
 
    username = input("Enter username: ")
    password = input("Enter password: ")
 
    if validate_user(username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")
 
login_system()'''

#Modules -------------------------------------------------------
'''#books.py
books = []
def add_book(book_name):
    books.append(book_name)
    print(f"{book_name} added successfully")
def show_books():
    print("Available Books:")
    for book in books:
        print(book)'''

'''#ravi(fine.py), arun(main.py) - kitchen (pvm)
#fine.py
print("Kitchen Open")
def prepare_food():
    #print(__name__) to see what happens
    print("Preparing food....")
def cut_vegetables():
    #print(__name__) to see what happens
    print("Cutting Vegetables....")

if __name__ == "__main__": #when executed directly it is __main__
    print("Ravi is the main hero of kitchen")
    prepare_food()
else:
    print("Arun is the main hero of kitchen and Ravi will help Arun")
    cut_vegetables()
#main.py
import fine.py #now fine.py will run as supporting file and __name__ is not __main__'''

#Packages -------------------------------------------------------
'''from student.studentinfo import * #everything is imported
(or) from student.studentinfo import add_student #only add_student is imported
from .fine import * #Intra package import --> importing a module in another module when both are inside same package

#student/studentinfo.py
def add_student():
    print("Student added successfully")
def update_student():
    print("Student updated successfully")
    
#To make a folder to be used as package as __init__.py file in the folder (best practice)
'''

#Exception Handling ----------------------------------------
'''#try(risky code),except(handling code),else,finally
try:
    num=int(input("Enter a number:"))
    print(100/num)
    print(num+"is a number")
    raise ZeroDivisionError("number cannot be zero")

except ZeroDivisionError:
    print("Enter a number greater than 0")

except ValueError:
    print("Enter a valid integer")

except Exception as e:
    #print("Error occured:", e)
    print("Error occured:", type(e).__name__)'''

#TASK
'''Create book issue system:
accept student ID
if invalid → error
if valid → success
finally print:
"Visit Again"

print("Book Issue System")
try:
      id = int(input("Enter student id"))
      print("Success")
except:
      print("invalid input")
finally:
       print("visit again")'''

#TASK
'''check user for the status fine paid?
if yes: say book issued
if no finenotpaiderror with message please clear the fine to proceed issuing the book
 
class FineNotPaidError(Exception):
    pass
try:
    status = input("Have you paid the fine (yes/no):")
    if status=="yes":
        print("Book issued")
    elif status=="no":
        raise FineNotPaidError("Please clear the fine to proceed with issuing the book")
    else:
        print("Input must be yes or no")
except Exception as e:
    print(e)'''

#File Handling
'''fr = open("sample.txt", "r")
data = fr.read()
print(data)
for line in fr:
    print (line)
fr.close()

with open("sample.txt", "r") as file:
    data1=file.readlines()
    print(data1)

import os
if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File Not Found")

os.remove("sample.txt") #deleting file'''

#TASK
'''
choice = int(input("1.Add Student\n 2.View Student\n 3.Exit\n Choose an operation:"))
if(choice==1):
    name = input("Enter student name:")
    mark = input("Enter student marks:")
    with open("sample.txt","a") as file:
        file.write(f"{name},{mark}\n") 
elif(choice==2):
    with open("sample.txt","r") as file:
        data=file.readlines()
        if not data:
            print("No students yet.")
        else:
            for line in data:
                name, mark = line.strip().split(",")
                print(f"Name: {name}, Marks: {mark}")
elif(choice==3):
    print("Exiting application....")
else:
    print("Invalid choice")'''

#Working with binary files
'''data = b"Hello Python"
file = open("binaryfile.dat","rb")
data=file.read()
print(data)
file.close()

with open("photo1.jpg","rb") as src:
    content = src.read()
with open("newphoto.jpg","wb") as des:
    des.write(content)
print("Image copied")'''

#File Methods
'''fr = open("sample.txt", "r")
fr.seek(0) #start from a specific character. 0 will go to beginning of file
print(fr.tell()) #tells where cursor is right now
data = fr.read()
print(data)'''

#Pickle Module - used for storing data in binary format and can store complex data types like lists, dictionaries, etc.
'''import pickle #used for binary formats
student = {
    "name":"Ram",
    "mark":90
}
with open("studentrecord.dat","wb") as file:
    pickle.dump(student,file)
with open("studentrecord.dat","rb") as file:
    studentdata=pickle.load(file)
    print(studentdata)'''

#Constructors and Destructors --------------------------------------
'''def __init__(self): #Default Constructor 

class Library:
    def __init__(self, name): #Constructor
        self.name = name
        print(f"Library {self.name} created")

    def __del__(self): #Destructor
        print(f"Library {self.name} destroyed")'''

#Classes and Objects --------------------------------------
'''class Book:
    library_name = "Smart Library" #class variable
    def __init__(self, id, title, author, price):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
    
    def display_info(self):
        print(f"ID: {self.id} | Title: {self.title} | Author: {self.author} | Price: {self.price}")
    
    @classmethod #decorator to define class method which can access class variables and can be called using class name or object name
    def show_library(cls): #cls is a convention to refer to current class
        print(f"Welcome to {cls.library_name}!") 
        print(f"Library Name: {Book.library_name}")
    
    @staticmethod #utility or helper function which doesn't access class variables and can be called using class name or object name
    def calculate_gst(amount):
        gst = amount * 0.05
        print(f"GST: {gst}")

python = Book("B101", "Python Programming", "Guido van Rossum", 25.99)
Book.show_library()
python.show_library()
python.display_info()
python.calculate_gst(python.price)
Book.calculate_gst(200)'''

#TASK
'''#You are building an inventory system for a warehouse.
#Each product has: - Product name - Quantity - Rack location
#The warehouse also maintains: - Total products added - Warehouse name
#And utility tasks like: - Checking whether stock is low

class Product:
    warehouse_name = "Central Warehouse"
    total_products = 0 
    def __init__(self, name, quantity, rack_location):
        self.name = name
        self.quantity = quantity
        self.rack_location = rack_location
        Product.total_products += 1
    def check_stock(self):
        if self.quantity < 10:
            print(f"Stock for {self.name} is low. Only {self.quantity} left.")
        else:
            print(f"Stock for {self.name} is sufficient. Quantity: {self.quantity}")

Laptop = Product("Laptop", 5, "A1")
Phone = Product("Phone", 15, "B2")
print(Product.warehouse_name)
print(Product.total_products)
Laptop.check_stock()
Phone.check_stock()'''

#Encapsulation --------------------------------------
#we use _ for protected variable, __ for private variable, getter and setter methods to access private variables
#name mangling is used to access private variables using _ClassName__variableName where private variable is stored as _ClassName__variableName in memory
'''class Book:
    def __init__(self, title, author, price):
        self.title = title 
        self.__author = author #private variable
        self.price = price 

    def get_author(self): #getter method to access private variable
        return self.__author
    def set_author(self, author): #setter method to update private variable
        self.__author = author

python = Book("Python Programming", "Guido van Rossum", 25.99)
#print(python.__author) #will throw error because __author is private
print(python._Book__author) #name mangling to access private variable
print(python.get_author()) #accessing private variable using getter method
python.set_author("New Author") #updating private variable using setter method
print(python.get_author()) #accessing updated private variable using getter method'''

#TASK
'''#create a class and quantity as private variable with help of constructor , set and get  when set quantity > 10
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.__quantity = self.set_quantity(quantity) #using setter method to set quantity

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        if quantity > 10:
            self.__quantity = quantity
        else:
            print("Quantity must be greater than 10")

product1 = Product("Laptop", 5)
print(product1.get_quantity())
product1.set_quantity(15)
print(product1.get_quantity())'''

#Abstraction --------------------------------------
'''from abc import ABC, abstractmethod #Abstract Base Class
class Library(ABC):
    @abstractmethod
    def issue_book(self):
        pass
    @abstractmethod
    def return_book(self):
        pass
    def display_library_name(self):
        print("Welcome to the Smart Library!")

class CollegeLibrary(Library):
    def issue_book(self):
        print("Book issued to College student successfully")  
    def return_book(self):
        print("Book returned to College student successfully")

clibrary = CollegeLibrary()
clibrary.display_library_name()
clibrary.issue_book()   
clibrary.return_book()'''

#TASK
'''#You are developing a Restaurant Management System.
#Different restaurants: Dine-in restaurant,Online delivery restaurant
#Both should support: - Taking orders - Generating bills
from abc import ABC, abstractmethod
class Restaurant(ABC):
    @abstractmethod
    def take_order(self):
        pass
    @abstractmethod
    def generate_bill(self):
        pass
class DineInRestaurant(Restaurant):
    def take_order(self):
        print("Taking order for Dine-in restaurant")
    def generate_bill(self):
        print("Generating bill for Dine-in restaurant")
class OnlineDeliveryRestaurant(Restaurant):
    def take_order(self):
        print("Taking order for Online delivery restaurant")
    def generate_bill(self):
        print("Generating bill for Online delivery restaurant")
dine_in = DineInRestaurant()
dine_in.take_order()
dine_in.generate_bill()
online_delivery = OnlineDeliveryRestaurant()
online_delivery.take_order()
online_delivery.generate_bill()'''

'''#Create: PaymentSystem abstract class
# Methods: pay_bill(), refund()
#Child classes: CashPayment, UPIPayment, CardPayment
from abc import ABC, abstractmethod
class PaymentSystem(ABC):
    @abstractmethod
    def pay_bill(self):
        pass
    @abstractmethod
    def refund(self):
        pass

class CashPayment(PaymentSystem):
    def pay_bill(self):
        print("Paying bill with cash")
    def refund(self):
        print("Refunding cash payment")

class UPIPayment(PaymentSystem):
    def pay_bill(self):
        print("Paying bill with UPI")
    def refund(self):
        print("Refunding UPI payment")

class CardPayment(PaymentSystem):
    def pay_bill(self):
        print("Paying bill with card")
    def refund(self):
        print("Refunding card payment")

cash = CashPayment()
cash.pay_bill()
cash.refund()
upi = UPIPayment()
upi.pay_bill()
upi.refund()
card = CardPayment()
card.pay_bill()
card.refund()'''

#Inheritance --------------------------------------
'''class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def display_info(self):
        print(f"Name: {self.name} | Email: {self.email}")
    def login(self):
        print(f"{self.name} logged in successfully")
    def logout(self):
        print(f"{self.name} logged out successfully")

class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name, email) #calling parent class constructor
        self.student_id = student_id
    def display_info(self):
        super().display_info() #calling parent class method
        print(f"Student ID: {self.student_id}")

class Librarian(User):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email) #calling parent class constructor
        self.employee_id = employee_id
    def display_info(self):
        super().display_info() #calling parent class method
        print(f"Employee ID: {self.employee_id}")'''

#Polymorphism - Method Overriding --------------------------------------
'''class Notification:
    def send_notification(self):
        print(f"From Base Notification class")

class EmailNotification(Notification):
    def send_notification(self):
        print(f"Sending Email Notification")

class SMSNotification(Notification):
    def send_notification(self):
        print(f"Sending SMS Notification")

general = Notification()
email = EmailNotification()
sms = SMSNotification()
general.send_notification()
email.send_notification()
sms.send_notification()'''

#Method Overloading - Python does not support method overloading like other languages but we can achieve it using default parameters or variable length arguments
'''class searchBooks:
    def search(self,title=None, author=None):
        if title and author:
            print(f"Searching for book with title '{title}' and author '{author}'")
        elif title:
            print(f"Searching for book with title '{title}'")
        elif author:
            print(f"Searching for book with author '{author}'")
        else:
            print("Please provide either title or author to search")

search = searchBooks()
search.search(title="Python Programming")
search.search(author="Guido van Rossum")
search.search(title="Python Programming", author="Guido van Rossum")
search.search()'''

#Composition - when one class contains an object of another class as a member variable --------------------------------------
#Aggregation - when one class contains an object of another class as a member variable but the contained object can exist independently of the container object (the class is just using the object)
'''class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Library:
    def __init__(self, student):
        self.book = Book("Python Programming", "Guido van Rossum") #Library must contain books (composition)
        self.student = student; #Library may have students but students can exist without library and vice versa (aggregation)
class Student:
    def __init__(self, name):
        self.name = name

lib = Library(Student("Alice"))
print(lib.book.title,"-",lib.book.author)
print(lib.student.name) '''

#Magic Methods - special methods that start and end with __ and are used to define the behavior of objects --------------------------------
'''class Library:
    def __init__(self, name):
        self.name = name
    def __str__(self): #used to return a string representation of the object when print() is called
        return f"Library Name: {self.name}"
    def __len__(self): #used to return the length of the object when len() is called
        return len(self.name)
    def __add__(self, other): #used to define the behavior of the + operator for objects of this class
        return self.name + " & " + other.name
    def __eq__(self, other): #used to define the behavior of the == operator for objects of this class
        return self.name == other.name
    def __del__(self): #used to define the behavior of the object when it is destroyed (garbage collected)
        print(f"Library {self.name} is being destroyed")

lib1 = Library("Smart Library")
lib2 = Library("Central Library")
print(lib1)
print(len(lib1))
print(lib1 + lib2)
print(lib1 == lib2)
lib3 = Library("Smart Library")
print(lib1 == lib3)
del lib1 #automatically called when object is destroyed but can also be called explicitly to see the destructor in action'''

#Collections - provides specialized containered datatypes ------------------------------------------
'''import collections
#Counter - counts the occurrences of elements in a collection
from collections import Counter
data = ['Python', 'Java', 'Python', 'C++', 'Java', 'Python']
counter = Counter(data)
print(counter) #Counter({'Python': 3, 'Java': 2, 'C++': 1})
print(counter.most_common(1)) #most common element and its count

from collections import defaultdict
#defaultdict - provides a default value for a key that does not exist in the dictionary
default_dict = defaultdict(int) #default value is 0 for int
default_dict['Python'] += 1
default_dict['Java'] += 1
print(default_dict) #defaultdict(<class 'int'>, {'Python': 1, 'Java': 1})

from collections import namedtuple
#namedtuple - factory function for creating tuple subclasses with named fields
Book = namedtuple('Book', ['title', 'author', 'price'])
book1 = Book('Python Programming', 'Guido van Rossum', 25.99)
print(book1) #Book(title='Python Programming', author='Guido van Rossum', price=25.99)

from collections import deque
#deque - double-ended queue that allows fast appends and pops from both ends
queue = deque()
queue.append('Task 1')
queue.append('Task 2')
queue.appendleft('Task 0') #add to the left end of the queue
print(queue) #deque(['Task 0', 'Task 1', 'Task 2'])
queue.pop() #remove from the right end of the queue
print(queue) #deque(['Task 0', 'Task 1'])
queue.popleft() #remove from the left end of the queue
print(queue) #deque(['Task 1'])

from collections import OrderedDict
#OrderedDict - dictionary that remembers the order of keys as they were inserted
ordered_dict = OrderedDict()
ordered_dict['Python'] = 1
ordered_dict['Java'] = 2
ordered_dict['C++'] = 3
print(ordered_dict) #OrderedDict([('Python', 1), ('Java', 2), ('C++', 3)])

from collections import ChainMap
#ChainMap - groups multiple dictionaries together to create a single view
dict1 = {'Python': 1, 'Java': 2}
dict2 = {'C++': 3, 'JavaScript': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map) #ChainMap({'Python': 1, 'Java': 2}, {'C++': 3, 'JavaScript': 4})
print(chain_map['Python']) #1 from dict1'''

#Regular Expressions - Regex -------------------------------------
'''import re
email = "student@gmail.com"
result = re.fullmatch(r'[a-zA-Z0-9]+@gmail\.com', email)
#r - raw string, [a-zA-Z0-9]+ - one or more alphanumeric characters, @gmail\.com - followed by @gmail.com (dot is escaped with \ because dot is a special character in regex)
print(result is not None) #True if email matches the pattern, False otherwise

mobile = "9876543210"
result1 = re.fullmatch(r'[89]\d{9}', mobile)
#r - raw string, [89] - starts with 8 or 9, \d - digit, \d{9} - followed by 9 digits
print(result1 is not None)

number = "1234567890"
result2 = re.fullmatch(r'\d+', number)
#r - raw string, \d+ - one or more digits
print(result2 is not None)

string = "HelloWorld"
result3 = re.fullmatch(r'[A-Za-z]+', string)
#r - raw string, [A-Za-z]+ - one or more letters (both uppercase and lowercase)
print(result3 is not None)

searchBook = "Python Programming"
testSearch = re.search('Python', searchBook) 
#searches for the pattern in the string and returns a match object if found, None otherwise
#works without raw string as well but using raw string is a good practice to avoid issues with escape characters in regex patterns
print(testSearch is not None)

rackNos = "Rack1, Rack2, Rack3, Rack8, Rack10"
rackList = re.findall(r'\d+', rackNos) 
#finds all occurrences of the pattern in the string and returns a list of matches 
print(rackList)

memberID = "STU12345"   
result4 = re.fullmatch(r'STU\d{5}', memberID)
#r - raw string, STU - starts with STU, \d{5} - followed by exactly 5 digits
print(result4 is not None)
result5 = re.match(r'STU',memberID)
print(result5 is not None) #True if memberID starts with STU, False otherwise
#match checks only at the beginning of the string while fullmatch checks the entire string for a match

file= "library_data.csv"
result6 = re.search(r'.+\.csv$', file)
#\.csv - ends with .csv extension, $ - end of string
print(result6 is not None)
'''
#Decorators --------------------------------------
'''def security_check(func):
    def wrapper(*args, **kwargs):
        print("Performing security check...")
        print("Security check completed.")
        func(*args, **kwargs)
    return wrapper

@security_check
def enter_lounge():
    print("Welcome to the VIP Lounge")

enter_lounge()

def passport_check(func):
    def wrapper(*args, **kwargs):
        print("Checking passport...")
        print("Passport check completed.")
        func(*args, **kwargs)
    return wrapper

def baggage_check(func):
    def wrapper(*args, **kwargs):
        print("Scanning baggage...")
        print("Baggage scan completed.")
        func(*args, **kwargs)
    return wrapper

@security_check
@baggage_check
@passport_check
def board_flight(name):
    print(name,"Boarded the flight")

board_flight("Alice")'''


#TASK
'''def hygiene_check(func):
    def wrapper():
        print("Washing hands....")
        print("Wearing gloves....")
        func()
        print("Food served with hygiene.")
    return wrapper

@hygiene_check
def serve_food():
    print("Serving food to customers")'''

#TASK
#get user credentials and validate and authenticate user then open dashboard
'''def get_user_credentials(func):
    def wrapper():
        print("Getting user credentials...")
        print("User credentials obtained.")
        func()
    return wrapper

def validate_user(func):
    def wrapper():
        print("Validating user credentials...")
        print("User credentials validated.")
        func()
    return wrapper

def authenticate_user(func):
    def wrapper():
        print("Authenticating user...")
        print("User authenticated successfully.")
        func()
    return wrapper

@get_user_credentials
@validate_user
@authenticate_user
def access_dashboard():
    print("Welcome to the dashboard!")

access_dashboard()'''

'''def tax(func):
    def calculating_tax():
        amount = func()
        return amount + 500
    return calculating_tax

@tax
def ticket_price():
    return 2000

print("Total ticket price with tax:", ticket_price())'''

#Applying decorator to a class
'''def airport_features(cls):
    def tracking_system(self):
        print("Tracking system activated")
        print(f"Tracking the {self.name}'s location....")
    cls.tracking_system = tracking_system
    return cls

@airport_features
class Passenger:
    def __init__(self, name):
        self.name = name
    @property
    def upgrade(self):
        print("VIP access granted")

p = Passenger("Alice")
p.tracking_system()
p.upgrade'''

#Generators --------------------------------------
#used to generate values one by one instead of storing them all in memory at once like a list, used for large datasets or infinite sequences
'''def passengers():
    #yield will pause the function and return the value to the caller + it will maintain the state of the function so that when next() is called again it will resume from where it left off
    yield "John"
    yield "David"
    yield "Sam"
    yield "Emily"
    yield "Anna"
    yield "Bob"

p=passengers()
print(next(p))
print(next(p))
print(next(p)) '''

#TASK
'''def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib = fibonacci(10)
for num in fib:
    print(num)'''

#Context Managers --------------------------------------
#automatically manage resources like file handling, database connections, etc.
'''with open("sample.txt", "w") as file:
    file.write("Hello, World!")
# here with keyword is used to open the file and it will automatically close the file after the block of code is executed 
# even if an error occurs within the block, so we don't have to worry about closing the file explicitly 
# and it also ensures that resources are properly released.

class Library:
    def __enter__(self):
        print("Entering the library...")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the library...")
        
with Library() as lib:
    print("Welcome to the library!")
'''
#TASK
'''#"Scanner Activated" inside __enter__()
#"Scanner Deactivated" inside __exit__()
#Accept passenger name as input
#Print: "Passenger <name> Cleared"

class SecurityScanner:
    def __enter__(self):
        print("Scanner Activated")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Scanner Deactivated")

with SecurityScanner() as scanner:
    name = input("Enter passenger name: ")
    print(f"Passenger {name} Cleared")'''

#Database Connectivity --------------------------------------
#1. pip install pyodbc
#2. import pyodbc
#3. establish connection using pyodbc.connect() with appropriate connection string for your database
'''import pyodbc

connection = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=(localdb)\\MSSQLLocalDB;"
    "DATABASE=AirportDb;"
    "Trusted_Connection=yes;"
)
print("Connection established successfully")
cursor = connection.cursor()
query = """ 
    CREATE TABLE Passengers (
    ID INT PRIMARY KEY,
    Name NVARCHAR(100),
    PassportNumber NVARCHAR(100),
    FlightNumber NVARCHAR(20),
    [From] NVARCHAR(100),
    [To] NVARCHAR(100) )"""
cursor.execute(query)
print("Table created successfully")

insert_query = """
    INSERT INTO Passengers (ID, Name, PassportNumber, FlightNumber, [From], [To])
    VALUES (1, 'Alice', 'P123456', 'AA101', 'New York', 'Los Angeles')
    """
cursor.execute(insert_query)
print("Passenger added successfully")

select_query = "SELECT * FROM Passengers"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)

update_query = """
    UPDATE Passengers
    SET [From] = 'India'
    WHERE ID = 1"""
cursor.execute(update_query)
print("Passenger updated successfully")

select_query = "SELECT * FROM Passengers"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)

delete_query = "DELETE FROM Passengers WHERE ID = 1"
cursor.execute(delete_query)
print("Passenger deleted successfully")

connection.close()
'''

#Best Practices --------------------------------------
'''
1. Use meaningful variable and function names
2. Write clean and readable code
3. Avoid unnecessary code
4. Reuse code using functions and classes
5. Handle exceptions properly
6. Keep functions and classes small and focused on a single responsibility
7. Use comments when necessary
8. Close resources properly (like files, database connections, etc.)
9. Follow coding standards and conventions
'''

#PEP 8 - Style Guide for Python Code ---------------
'''
variable_name: book_name, student_id, etc. (snake_case)
function_name: add_book(), search_book(), etc. (snake_case)
class_name: Book, Student, etc. (PascalCase)
constants: MAX_BOOKS, MIN_AGE, etc. (UPPER_SNAKE_CASE)
a = 10 #variable assignment should have spaces around the operator
Indentation: 4 spaces per indentation level
Maximum line length: 75-100 characters
import statements should be on separate lines and at the top of the file
'''

#Code Optimization --------------------------------------
'''
1. Reduce memory usage
2. Reduce time complexity
3. Use built-in functions and libraries
4. Avoid redundant computations
5. For large data use generators instead of lists
6. Avoid unnecessary loops and nested loops
7. Consistent Indentation and formatting
8. Follow the Single Responsibility Principle - each function or class should have
9. Follow the DRY (Don't Repeat Yourself) principle - avoid code duplication by reusing code through functions and classes
10. Create reusable code using functions and classes to avoid code duplication and improve maintainability
'''

#Unit Testing --------------------------------------
'''import unittest

def issue_book(book_available):
    if book_available:
        return "Book issued successfully"
    else:
        raise Exception("Book not available")
    
def calculate_fine(days):
    return days * 10

class LibraryTests(unittest.TestCase):
    def test_calculate_fine(self):
        self.assertEqual(calculate_fine(5), 50)
        self.assertEqual(calculate_fine(0), 0)
        self.assertEqual(calculate_fine(10), 100)

    def test_issue_book(self):
        self.assertEqual(issue_book(True), "Book issued successfully")
        with self.assertRaises(Exception) as context:
            issue_book(False)
        self.assertTrue("Book not available" in str(context.exception))

if __name__ == '__main__':
    unittest.main()

#Instead of running all tests we can run specific tests using TestSuite
suite = unittest.TestSuite()
suite.addTest(LibraryTests('test_calculate_fine'))
runner = unittest.TextTestRunner()
runner.run(suite)
#(or) python -m unittest -k test_calculate_fine to run specific test from command line'''

'''#TestFixture - setUp() and tearDown() methods to set up test environment and clean up after tests
class LibraryTests(unittest.TestCase):
    def setUp(self):
        print("Setting up test environment...")
        self.book_available = True
    def tearDown(self):
        print("Cleaning up test environment...")
    def test_issue_book(self):
        self.assertEqual(issue_book(self.book_available), "Book issued successfully")
        print("Test for issue_book passed")

if __name__ == '__main__':
    unittest.main()

#Parameterized Tests - run the same test with different inputs using subTest
class LibraryTests(unittest.TestCase):
    def test_calculate_fine(self):
        test_data = [(5, 50), (0, 0), (10, 100)]
        for days, expected in test_data:
            with self.subTest(days=days, expected=expected):
                self.assertEqual(calculate_fine(days), expected)

if __name__ == '__main__':
    unittest.main()

assertFalse(1==2, "1 is not equal to 2")
assertTrue(2>1, "2 is greater than 1")
assertEqual(5, 5, "5 is equal to 5")
assertNotEqual(5, 10, "5 is not equal to 10")
assertRaises(ValueError, int, "abc") #assert that int("abc") raises a ValueError'''