'''Airport Security Management System - Python OOPS Activity

TASK 1 — CLASS AND OBJECT
Create classes:
 - Passenger
 - Flight
 - SecurityOfficer
 - Baggage

 Create minimum:
 - 2 passengers
 - 2 flights
TASK 2 — CONSTRUCTOR
Use constructors to initialize:
 - passenger details
 - flight details
 - baggage details
TASK 3 — INSTANCE VARIABLES
Passenger should contain:
 - passenger_id
 - passenger_name
 - passport_number
 - baggage_weight

 Flight should contain:
 - flight_id
 - flight_name
 - destination
TASK 4 — INSTANCE METHODS
Create methods:
 - verify_passport()
 - scan_baggage()
 - board_flight()
 - display_passenger()
TASK 5 — CLASS VARIABLE
Create class variable:
 airport_name = "Chennai International Airport"
TASK 6 — CLASS METHOD
Create class method:
 show_airport_name()
TASK 7 — STATIC METHOD
Create static method:
 calculate_extra_baggage_fee(weight)

 Condition:
 - If baggage > 20kg
 - Charge ₹500 per extra kg
TASK 8 — SINGLE INHERITANCE
Create:
 Person → Passenger

 Person methods:
 - login()
 - logout()
TASK 9 — MULTILEVEL INHERITANCE
Create:
 Person → Passenger → VIPPassenger

 VIPPassenger features:
 - priority_checkin()
 - lounge_access()
TASK 10 — MULTIPLE INHERITANCE
Create classes:
 - SecurityCheck
 - ImmigrationCheck

 Passenger should inherit both.
TASK 11 — HIERARCHICAL INHERITANCE
Create:
 Person → Passenger
 Person → SecurityOfficer
TASK 12 — POLYMORPHISM
Create method:
 security_check()

 Different behavior for:
 - DomesticPassenger
 - InternationalPassenger
 - VIPPassenger
TASK 13 — METHOD OVERRIDING
Override show_details() in:
 - Passenger
 - SecurityOfficer
TASK 14 — ENCAPSULATION
Hide passenger passport number using private variable:
 __passport_number

 Create:
 - set_passport()
 - get_passport()
TASK 15 — GETTER AND SETTER
Create private variable:
 __security_pin

 Use getter and setter methods.
TASK 16 — ABSTRACTION
Create abstract class:
 SecurityProcess

 Abstract methods:
 - verify_identity()
 - baggage_scan()
TASK 17 — COMPOSITION
Airport contains:
 - multiple flights
 - multiple security officers
TASK 18 — AGGREGATION
Security system uses existing Passenger objects.
TASK 19 — MAGIC METHODS
Implement:
 __str__()

 Should print passenger name directly.
TASK 20 — OPERATOR OVERLOADING
Add baggage weights of two passengers using + operator.
TASK 21 — EXCEPTION HANDLING
Handle:
 - Invalid passport number
 - Negative baggage weight
 - Invalid boarding pass
 - Unauthorized access

from abc import ABC, abstractmethod

class Person:
    def login(self):
        return "Logged in successfully"

    def logout(self):
        return "Logged out successfully"

    def show_details(self):
        return "Person details"

class SecurityCheck:
    def security_check(self):
        return "Performing security check"

class ImmigrationCheck:
    def immigration_check(self):
        return "Performing immigration check"

class Passenger(Person, SecurityCheck, ImmigrationCheck):
    def __init__(self, passenger_id, passenger_name,passport_number, baggage_weight):
        if baggage_weight < 0:
            raise ValueError("Negative baggage weight is not allowed")
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name
        self.set_passport(passport_number)
        self.baggage_weight = baggage_weight

    def __str__(self):
        return self.passenger_name

    def set_passport(self, passport_number):
        self.__passport_number = passport_number

    def get_passport(self):
        return self.__passport_number

    def show_details(self):
        return (f"Passenger ID: {self.passenger_id}, Name: {self.passenger_name}")

    def verify_passport(self):
        if (len(self.__passport_number) == 9 and self.__passport_number.isalnum()): return "Passport verified successfully"
        raise ValueError("Invalid passport number")

    def scan_baggage(self):
        print(f"Scanning baggage for {self.passenger_name}")
        print(Baggage.calculate_extra_baggage_fee(self.baggage_weight))
        print("Baggage scan complete.")

    def board_flight(self, boarding_pass=True):
        try:
            if not boarding_pass:
                raise Exception("Invalid boarding pass")
            self.verify_passport()
            return (f"{self.passenger_name} has boarded the flight.")
        except Exception as e:
            return str(e)

    def display_passenger(self):
        return (f"Passenger ID: {self.passenger_id}, Name: {self.passenger_name}, Baggage Weight: {self.baggage_weight}kg")

class VIPPassenger(Passenger):
    def priority_checkin(self):
        return (f"{self.passenger_name} has priority check-in access.")

    def lounge_access(self):
        return (f"{self.passenger_name} has access to VIP lounge.")

    def security_check(self):
        return (f"{self.passenger_name} is undergoing VIP security check.")

class DomesticPassenger(Passenger):
    def security_check(self):
        return (f"{self.passenger_name} is undergoing domestic security check.")

class InternationalPassenger(Passenger):
    def security_check(self):
        return (f"{self.passenger_name} is undergoing international security check.")

class Flight:
    def __init__(self, flight_id, flight_name, destination):
        self.flight_id = flight_id
        self.flight_name = flight_name
        self.destination = destination

class Airport:
    airport_name = "Chennai International Airport"
    def __init__(self, name):
        self.name = name
        self.flights = []
        self.security_officers = []

    @classmethod
    def show_airport_name(cls):
        return cls.airport_name

class Baggage:
    def __init__(self, baggage_id, weight):
        if weight < 0:
            raise ValueError("Negative baggage weight is not allowed")
        self.baggage_id = baggage_id
        self.weight = weight

    @staticmethod
    def calculate_extra_baggage_fee(weight):
        if weight > 20:
            extra_weight = weight - 20
            fee = extra_weight * 500
            return (f"Extra baggage: {extra_weight}kg \nExtra Fee: ₹{fee}")
        return "Baggage within limit"

    def __add__(self, other):
        return self.weight + other.weight

class SecurityProcess(ABC):
    @abstractmethod
    def verify_identity(self):
        pass

    @abstractmethod
    def baggage_scan(self):
        pass

class SecurityOfficer(Person, SecurityProcess):
    def __init__(self, officer_id, officer_name):
        self.officer_id = officer_id
        self.officer_name = officer_name
        self.__security_pin = None

    def set_security_pin(self, pin):
        self.__security_pin = pin

    def get_security_pin(self):
        return self.__security_pin

    def show_details(self):
        return (
            f"Security Officer ID: "
            f"{self.officer_id}, "
            f"Name: {self.officer_name}"
        )

    def verify_identity(self):
        return (f"{self.officer_name} is verifying identity... Identity Verified successfully.")

    def baggage_scan(self):
        return (f"{self.officer_name} is scanning baggage... Baggage scan complete.")

    def access_security_system(self, pin):
        if pin != self.__security_pin:
            raise PermissionError("Unauthorized access")
        return "Access granted"

class SecuritySystem:
    def __init__(self, passengers):
        self.passengers = passengers

passenger1 = Passenger(1, "Alice", "A12345678", 25)
flight1 = Flight(101, "Flight A", "New York")
flight2 = Flight(102, "Flight B", "London")
security_officer1 = SecurityOfficer(1, "Officer Smith")
security_officer1.set_security_pin("1234")
security_officer2 = SecurityOfficer(2, "Officer Johnson")
security_officer2.set_security_pin("5678")
baggage1 = Baggage(1, 25)
baggage2 = Baggage(2, 15)

print(passenger1.show_details())
print(passenger1.verify_passport())
passenger1.scan_baggage()
print(passenger1.board_flight())
print("Total baggage weight:",baggage1 + baggage2)

try:
    passenger2 = Passenger(2, "Bob", "123456", -15) 
    passenger2 = Passenger(2, "Bob", "B87654321", -15)
    print(security_officer1.access_security_system("0000"))
except ValueError as e:
    print(e)
except PermissionError as e:
    print(e)'''


#TASK - REGULAR EXPRESSIONS
'''Python Regular Expression Practice
Airport Security System Management
 
1. Validate Passenger ID
Passenger IDs should start with PSG followed by 4 digits.
Valid Examples
PSG1234 
PSG9876
Invalid Examples
psg1234 
PSG12
Task
Write a regex to validate passenger IDs using re.fullmatch().
 
2. Validate Flight Number
Flight numbers should contain:
2 uppercase letters
followed by 3 or 4 digits
Valid
AI203 
EK5678
Invalid
aI203 
AIR203
Task
Create regex using re.fullmatch().
 
3. Detect Dangerous Words in Luggage Notes
Find words:
bomb
gun
knife
inside a text.
Sample Input
"Passenger carrying a knife in baggage"
Task
Use re.search().
 
4. Validate Airport Email
Only airport staff emails allowed.
Format:
name@airport.com
Valid
john@airport.com
Invalid
john@gmail.com
Task
Write regex validation.
 
5. Extract Passport Numbers
Passport format:
1 uppercase letter
followed by 7 digits
Sample Text
"Passenger passports: A1234567, B7654321"
Task
Use re.findall() to extract all passport numbers.
 
6. Validate Boarding Gate
Gate format:
GATE-
followed by 1 or 2 digits
Valid
GATE-7 
GATE-21
Invalid
gate-7 
GATE-A1
Task
Write regex validation.
 
7. Validate Time Format
Airport timing should be:
HH:MM
24-hour format.
Valid
09:45 
23:59
Invalid
25:00 
9:30
Task
Write regex.
 
8. Extract Suspicious Bag Tags
Bag tags start with:
SB-
followed by 5 digits.
Sample
"Detected tags: SB-12345, BG-99999, SB-67890"
Task
Extract only suspicious tags using re.findall().
 
9. Validate Runway Code
Runway code format:
RWY
hyphen
2 digits
uppercase letter
Valid
RWY-27A 
RWY-09B
Invalid
RWY27A 
rwy-09B
Task
Write regex validation.
 
10. Mask Credit Card Numbers
Replace middle digits with ****.
Input
"Passenger paid using 4567891234567890"
Expected Output
4567****7890
Task
Use re.sub().
 
Bonus Challenge
Multi Validation Security Check
Validate this complete record:
Passenger: John 
Passport: A1234567 
Flight: AI203 
Gate: GATE-7
Task
Use regex to validate all fields separately.
 
Mini Activity
Create a menu-driven airport security checker:
1. Validate passport 
2. Validate flight 
3. Detect dangerous words 
4. Extract suspicious bag tags 
Use:
re.match()
re.fullmatch()
re.search()
re.findall()
re.sub()
for practice.'''

import re

valid_passenger_id = re.fullmatch(r'PSG\d{4}', 'PSG1234')
print(valid_passenger_id is not None)

valid_flight_number = re.fullmatch(r'[A-Z]{2}\d{3,4}', 'AI203')
print(valid_flight_number is not None)

dangerous_words = re.search(r'\b(bomb|gun|knife)\b', "Passenger carrying a knife in baggage")
print(dangerous_words is not None)

valid_email = re.fullmatch(r'\w+@airport\.com', 'bhagya@airport.com')
print(valid_email is not None)

passport_numbers = re.findall(r'[A-Z]\d{7}', "Passenger passports: A1234567, B7654321")
print(passport_numbers)

valid_boarding_gate = re.fullmatch(r'GATE-\d{1,2}', 'GATE-7')
print(valid_boarding_gate is not None)

valid_time_format = re.fullmatch(r'([0-9]{2}|2[0-3]):[0-5][0-9]', '09:45') 
print(valid_time_format is not None)

suspicious_tags = re.findall(r'SB-\d{5}', "Detected tags: SB-12345, BG-99999, SB-67890")
print(suspicious_tags)

valid_runway_code = re.fullmatch(r'RWY-\d{2}[A-Z]', 'RWY-27A')
print(valid_runway_code is not None)

masked_card = re.sub(r'(\d{4})\d{8}(\d{4})', r'\1****\2', "Passenger paid using 4567891234567890") 
print(masked_card)

#Bonus challenge
record = "Passenger: John Passport: A1234567 Flight: AI203 Gate: GATE-7"
passenger_name = re.search(r'Passenger:\s(\w+)', record)
print(passenger_name.group(1) if passenger_name else None)
passport = re.search(r'Passport:\s([A-Z]\d{7})', record)
print(passport.group(1) if passport else None)
flight = re.search(r'Flight:\s([A-Z]{2}\d{3,4})', record)
print(flight.group(1) if flight else None)
gate = re.search(r'Gate:\s(GATE-\d{1,2})', record)
print(gate.group(1) if gate else None)

#Mini Activity
def validate_passport(passport_number):
    return re.match(r'[A-Z]\d{7}', passport_number) is not None
def validate_flight(flight_number):
    return re.fullmatch(r'[A-Z]{2}\d{3,4}', flight_number) is not None
def detect_dangerous_words(text):
    return re.search(r'\b(bomb|gun|knife)\b', text) is not None
def extract_suspicious_bag_tags(text):
    return re.findall(r'SB-\d{5}', text)
while True:
    print("\nAirport Security Checker")
    print("1. Validate passport")
    print("2. Validate flight")
    print("3. Detect dangerous words")
    print("4. Extract suspicious bag tags")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        passport_number = input("Enter passport number: ")
        if validate_passport(passport_number):
            print("Passport is valid.")
        else:
            print("Invalid passport number.")
    elif choice == '2':
        flight_number = input("Enter flight number: ")
        if validate_flight(flight_number):
            print("Flight number is valid.")
        else:
            print("Invalid flight number.")
    elif choice == '3':
        text = input("Enter text to check for dangerous words: ")
        if detect_dangerous_words(text):
            print("Dangerous words detected!")
        else:
            print("No dangerous words found.")
    elif choice == '4':
        text = input("Enter text to extract suspicious bag tags: ")
        tags = extract_suspicious_bag_tags(text)
        if tags:
            print("Suspicious bag tags found:", tags)
        else:
            print("No suspicious bag tags found.")
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")