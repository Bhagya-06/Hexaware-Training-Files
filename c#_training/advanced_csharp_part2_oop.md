# Advanced C# Concepts - Part 2: Object-Oriented Programming (OOP)

## Table of Contents
1. [Object-Oriented Programming Principles](#object-oriented-programming-principles)
2. [Classes and Objects](#classes-and-objects)
3. [Constructors in C#](#constructors-in-c)
4. [Destructors in C#](#destructors-in-c)
5. [Garbage Collection in .NET](#garbage-collection-in-net)

---

## 1. Object-Oriented Programming Principles

### What is OOP?

Object-Oriented Programming is a programming paradigm based on the concept of **objects and classes**. It provides a structured way to organize code and data.

### The Four Pillars of OOP

#### 1. **Encapsulation**

Bundling data (fields) and methods (behavior) together, and hiding internal details.

**Benefits:**
- Data protection
- Controlled access
- Implementation hiding

**Example:**
```csharp
public class BankAccount
{
    private decimal balance;  // Hidden from outside
    
    public void Deposit(decimal amount)
    {
        if (amount > 0)
            balance += amount;
    }
    
    public decimal GetBalance()
    {
        return balance;
    }
}
```

#### 2. **Inheritance**

Creating new classes based on existing classes, inheriting their properties and methods.

**Benefits:**
- Code reuse
- Logical hierarchy
- Polymorphism

**Example:**
```csharp
public class Animal
{
    public void Eat() { }
}

public class Dog : Animal  // Dog inherits from Animal
{
    public void Bark() { }
}

Dog dog = new Dog();
dog.Eat();   // Inherited method
dog.Bark();  // Own method
```

#### 3. **Polymorphism**

Objects can take multiple forms. Same method call produces different results based on object type.

**Benefits:**
- Flexible code
- Loose coupling
- Extensibility

**Example:**
```csharp
public class Animal
{
    public virtual void MakeSound() { }
}

public class Dog : Animal
{
    public override void MakeSound() { Console.WriteLine("Woof!"); }
}

public class Cat : Animal
{
    public override void MakeSound() { Console.WriteLine("Meow!"); }
}

Animal dog = new Dog();
Animal cat = new Cat();

dog.MakeSound();  // Output: Woof!
cat.MakeSound();  // Output: Meow!
```

#### 4. **Abstraction**

Hiding complex implementation details and exposing only necessary functionality.

**Benefits:**
- Simplified interface
- Reduced complexity
- Focus on "what" not "how"

**Example:**
```csharp
public abstract class Shape
{
    public abstract double GetArea();  // What to do, not how
}

public class Circle : Shape
{
    private double radius;
    
    public override double GetArea()  // How to do it
    {
        return Math.PI * radius * radius;
    }
}
```

### Summary of OOP Principles

| Principle | Purpose | Example |
|-----------|---------|---------|
| Encapsulation | Hide internal details | Private fields, public properties |
| Inheritance | Reuse code | Dog inherits from Animal |
| Polymorphism | Different behavior | Dog.MakeSound() vs Cat.MakeSound() |
| Abstraction | Simplify interface | Shape.GetArea() abstract method |

---

## 2. Classes and Objects

### What is a Class?

A **class** is a **blueprint** for creating objects. It defines the structure (data) and behavior (methods).

### What is an Object?

An **object** is an **instance** of a class. A concrete entity created from the blueprint.

**Analogy:**
- Class = Cookie cutter (blueprint)
- Object = Cookie (actual thing)

### Declaring a Class

```csharp
public class Student
{
    // Fields (data)
    public string name;
    public int age;
    
    // Methods (behavior)
    public void Study()
    {
        Console.WriteLine($"{name} is studying");
    }
}
```

### Creating Objects

**Syntax:**
```csharp
ClassName objectName = new ClassName();
```

**Example:**
```csharp
Student student1 = new Student();
Student student2 = new Student();

// Both are independent objects
student1.name = "Raj";
student2.name = "Priya";
```

### Access Modifiers

Control visibility of class members:

| Modifier | Visibility | Usage |
|----------|-----------|-------|
| `public` | Everywhere | External code can access |
| `private` | Same class only | Internal use only |
| `protected` | Same class + derived | For inheritance |
| `internal` | Same assembly | Within project |

**Example:**
```csharp
public class Student
{
    public string Name { get; set; }           // Anyone can access
    private int studentId;                     // Only this class
    protected DateTime enrollmentDate;         // This class + derived
    internal string SchoolName { get; set; }  // Within assembly
}
```

### Example 1: Complete Class Definition

```csharp
using System;

namespace ClassDemo
{
    public class Car
    {
        // Fields (data)
        private string make;
        private string model;
        private int year;
        private double speed;

        // Properties
        public string Make
        {
            get { return make; }
            set { make = value; }
        }

        public string Model
        {
            get { return model; }
            set { model = value; }
        }

        public int Year
        {
            get { return year; }
            set { year = value; }
        }

        public double Speed
        {
            get { return speed; }
        }

        // Methods
        public void Accelerate(double amount)
        {
            speed += amount;
            Console.WriteLine($"Speed increased to {speed} km/h");
        }

        public void Brake(double amount)
        {
            speed -= amount;
            if (speed < 0) speed = 0;
            Console.WriteLine($"Speed reduced to {speed} km/h");
        }

        public void DisplayInfo()
        {
            Console.WriteLine($"{year} {make} {model} - Speed: {speed} km/h");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Classes and Objects ===\n");

            // Create objects
            Car car1 = new Car();
            car1.Make = "Toyota";
            car1.Model = "Camry";
            car1.Year = 2023;

            Car car2 = new Car();
            car2.Make = "Honda";
            car2.Model = "Civic";
            car2.Year = 2022;

            // Use objects
            Console.WriteLine("Car 1:");
            car1.DisplayInfo();
            car1.Accelerate(50);
            car1.Accelerate(30);
            car1.Brake(20);

            Console.WriteLine("\nCar 2:");
            car2.DisplayInfo();
            car2.Accelerate(60);
            car2.Brake(40);
        }
    }
}
```

**Output:**
```
=== Classes and Objects ===

Car 1:
2023 Toyota Camry - Speed: 0 km/h
Speed increased to 50 km/h
Speed increased to 80 km/h
Speed reduced to 60 km/h

Car 2:
2022 Honda Civic - Speed: 0 km/h
Speed increased to 60 km/h
Speed reduced to 20 km/h
```

### Example 2: Student Class with Methods

```csharp
using System;

namespace StudentClass
{
    public class Student
    {
        // Private fields
        private string name;
        private int age;
        private double[] grades;

        // Properties
        public string Name
        {
            get { return name; }
            set { name = value; }
        }

        public int Age
        {
            get { return age; }
            set 
            { 
                if (value > 0)
                    age = value;
            }
        }

        // Constructor
        public Student(string studentName, int studentAge)
        {
            name = studentName;
            age = studentAge;
            grades = new double[5];
        }

        // Methods
        public void AddGrade(int index, double grade)
        {
            if (index >= 0 && index < grades.Length)
                grades[index] = grade;
        }

        public double CalculateAverage()
        {
            if (grades.Length == 0)
                return 0;

            double sum = 0;
            foreach (double grade in grades)
                sum += grade;

            return sum / grades.Length;
        }

        public void DisplayInfo()
        {
            Console.WriteLine($"Name: {name}");
            Console.WriteLine($"Age: {age}");
            Console.WriteLine($"Average Grade: {CalculateAverage():F2}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Student Class ===\n");

            Student student = new Student("Raj", 20);

            // Add grades
            student.AddGrade(0, 95);
            student.AddGrade(1, 87);
            student.AddGrade(2, 92);
            student.AddGrade(3, 88);
            student.AddGrade(4, 90);

            student.DisplayInfo();
        }
    }
}
```

**Output:**
```
=== Student Class ===

Name: Raj
Age: 20
Average Grade: 90.40
```

### Key Points about Classes and Objects

- Classes are blueprints; objects are instances
- Access modifiers control visibility
- Properties provide controlled access to fields
- Methods define behavior
- Objects are independent - changes to one don't affect others

---

## 3. Constructors in C#

### What is a Constructor?

A **constructor** is a special method that **initializes objects**. It runs automatically when an object is created.

**Key characteristics:**
- Same name as class
- No return type
- Called automatically with `new`
- Used to set initial values

### Why Constructors?

```csharp
// Without constructor - manual initialization
Student s = new Student();
s.name = "Raj";
s.age = 20;

// With constructor - automatic initialization
Student s = new Student("Raj", 20);
```

### Types of Constructors

#### 1. **Default Constructor** (Parameterless)

```csharp
public class Student
{
    public Student()
    {
        Console.WriteLine("Default constructor called");
    }
}

Student s = new Student();  // Calls default constructor
```

**Compiler provides default constructor if you don't define one:**
```csharp
public class Student
{
    // No constructor defined - compiler creates default
}

Student s = new Student();  // Uses compiler-generated default
```

#### 2. **Parameterized Constructor**

Takes parameters to initialize fields with provided values.

```csharp
public class Student
{
    public string Name { get; set; }
    public int Age { get; set; }

    public Student(string name, int age)
    {
        Name = name;
        Age = age;
        Console.WriteLine($"Constructor called: {name}");
    }
}

Student s = new Student("Raj", 20);
```

#### 3. **Copy Constructor**

Creates object as copy of another object.

```csharp
public class Student
{
    public string Name { get; set; }
    public int Age { get; set; }

    // Regular constructor
    public Student(string name, int age)
    {
        Name = name;
        Age = age;
    }

    // Copy constructor
    public Student(Student other)
    {
        Name = other.Name;
        Age = other.Age;
    }
}

Student s1 = new Student("Raj", 20);
Student s2 = new Student(s1);  // Copy of s1
```

#### 4. **Multiple Constructors (Overloading)**

Different constructors for different scenarios.

```csharp
public class Student
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Grade { get; set; }

    // Constructor 1: No parameters
    public Student()
    {
        Name = "Unknown";
        Age = 0;
        Grade = "N/A";
    }

    // Constructor 2: Name and Age
    public Student(string name, int age)
    {
        Name = name;
        Age = age;
        Grade = "N/A";
    }

    // Constructor 3: All parameters
    public Student(string name, int age, string grade)
    {
        Name = name;
        Age = age;
        Grade = grade;
    }
}

Student s1 = new Student();                    // Uses constructor 1
Student s2 = new Student("Raj", 20);          // Uses constructor 2
Student s3 = new Student("Raj", 20, "A");     // Uses constructor 3
```

### Static vs Non-Static Constructors

#### Non-Static (Instance) Constructor

Runs when an object is created. Can access instance members.

```csharp
public class Student
{
    public string Name { get; set; }

    public Student(string name)  // Non-static
    {
        Name = name;
    }
}

Student s = new Student("Raj");  // Calls instance constructor
```

#### Static Constructor

Runs once when class is first used. Cannot have parameters.

```csharp
public class Student
{
    public static int TotalStudents { get; set; }

    static Student()  // Static constructor
    {
        TotalStudents = 0;
        Console.WriteLine("Static constructor called");
    }

    public Student(string name)
    {
        TotalStudents++;
    }
}

// Static constructor called on first use
Student s1 = new Student("Raj");    // Static constructor runs here
Student s2 = new Student("Priya");  // Static constructor doesn't run again
```

### Private Constructors

Prevent objects from being created from outside (used for factory patterns).

```csharp
public class Student
{
    public string Name { get; set; }

    private Student(string name)  // Private - cannot create from outside
    {
        Name = name;
    }

    // Factory method to create instances
    public static Student Create(string name)
    {
        return new Student(name);
    }
}

// Student s = new Student("Raj");  // ❌ ERROR - private constructor

Student s = Student.Create("Raj");  // ✅ OK - use factory method
```

### Constructor Chaining (this keyword)

Using one constructor to call another.

```csharp
public class Student
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Grade { get; set; }

    public Student() : this("Unknown", 0, "N/A")
    {
    }

    public Student(string name) : this(name, 0, "N/A")
    {
    }

    public Student(string name, int age, string grade)
    {
        Name = name;
        Age = age;
        Grade = grade;
    }
}

Student s1 = new Student();                   // Chains to full constructor
Student s2 = new Student("Raj");              // Chains to full constructor
Student s3 = new Student("Raj", 20, "A");    // Full constructor
```

### Complete Constructor Example

```csharp
using System;

namespace ConstructorDemo
{
    public class BankAccount
    {
        public string AccountHolder { get; set; }
        public decimal Balance { get; private set; }
        private string accountNumber;

        // Instance counter
        public static int TotalAccounts { get; private set; }

        // Static constructor
        static BankAccount()
        {
            TotalAccounts = 0;
            Console.WriteLine("[Static] Initializing BankAccount class");
        }

        // Default constructor
        public BankAccount()
        {
            AccountHolder = "Unknown";
            Balance = 0;
            accountNumber = GenerateAccountNumber();
            TotalAccounts++;
        }

        // Parameterized constructor
        public BankAccount(string holder, decimal initialBalance)
        {
            if (string.IsNullOrEmpty(holder))
                throw new ArgumentException("Holder name required");
            if (initialBalance < 0)
                throw new ArgumentException("Balance cannot be negative");

            AccountHolder = holder;
            Balance = initialBalance;
            accountNumber = GenerateAccountNumber();
            TotalAccounts++;
        }

        // Copy constructor
        public BankAccount(BankAccount other)
        {
            AccountHolder = other.AccountHolder;
            Balance = other.Balance;
            accountNumber = GenerateAccountNumber();
            TotalAccounts++;
        }

        // Private helper method
        private string GenerateAccountNumber()
        {
            return "ACC" + DateTime.Now.Ticks;
        }

        // Public method
        public void Deposit(decimal amount)
        {
            if (amount > 0)
                Balance += amount;
        }

        public void DisplayInfo()
        {
            Console.WriteLine($"Account: {accountNumber}");
            Console.WriteLine($"Holder: {AccountHolder}");
            Console.WriteLine($"Balance: {Balance:C}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Constructor Types ===\n");

            // Default constructor
            BankAccount acc1 = new BankAccount();
            acc1.DisplayInfo();

            Console.WriteLine();

            // Parameterized constructor
            BankAccount acc2 = new BankAccount("Raj", 5000);
            acc2.Deposit(1000);
            acc2.DisplayInfo();

            Console.WriteLine();

            // Copy constructor
            BankAccount acc3 = new BankAccount(acc2);
            acc3.DisplayInfo();

            Console.WriteLine($"\nTotal Accounts: {BankAccount.TotalAccounts}");
        }
    }
}
```

**Output:**
```
=== Constructor Types ===

[Static] Initializing BankAccount class
Account: ACC638420654321000000
Holder: Unknown
Balance: $0.00

Account: ACC638420654321123456
Holder: Raj
Balance: $6,000.00

Account: ACC638420654321234567
Holder: Raj
Balance: $6,000.00

Total Accounts: 3
```

### Key Points about Constructors

- Runs automatically when object is created
- Same name as class, no return type
- Can be overloaded with different parameters
- Static constructor runs once for class
- Private constructor prevents external instantiation
- Use `this` for constructor chaining
- Initializes fields to valid state

---

## 4. Destructors in C#

### What is a Destructor?

A **destructor** is a special method that **cleans up resources** when an object is destroyed. It runs automatically when object is garbage collected.

**Key characteristics:**
- Same name as class with `~` prefix
- No parameters, no return type
- Called automatically by garbage collector
- Used for cleanup (files, connections, etc.)

### Syntax

```csharp
~ClassName()
{
    // Cleanup code
}
```

### Example Destructor

```csharp
public class FileHandler
{
    private string fileName;

    public FileHandler(string file)
    {
        fileName = file;
        Console.WriteLine($"Opening file: {fileName}");
    }

    ~FileHandler()  // Destructor
    {
        Console.WriteLine($"Closing file: {fileName}");
    }
}

FileHandler handler = new FileHandler("data.txt");
// When handler goes out of scope, destructor is called
```

### Destructors vs Garbage Collection

**Important:** Destructors are NOT called immediately. They rely on garbage collector.

```csharp
public class Example
{
    public string Data { get; set; }

    public Example(string data)
    {
        Data = data;
        Console.WriteLine($"Constructor: {data}");
    }

    ~Example()
    {
        Console.WriteLine($"Destructor: {Data}");
    }
}

Example obj = new Example("Test");
obj = null;  // Object eligible for garbage collection
// Destructor may not run immediately!

GC.Collect();  // Force garbage collection (not recommended)
// Now destructor runs
```

### IDisposable Pattern (Preferred)

For immediate resource cleanup, use `IDisposable` instead of destructors.

```csharp
using System;

public class Resource : IDisposable
{
    private bool disposed = false;

    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this);  // Don't call destructor
    }

    protected virtual void Dispose(bool disposing)
    {
        if (!disposed)
        {
            if (disposing)
            {
                // Cleanup managed resources
                Console.WriteLine("Releasing resources");
            }
            disposed = true;
        }
    }

    ~Resource()
    {
        Dispose(false);
    }
}

// Usage
using (Resource res = new Resource())
{
    // Use resource
}  // Dispose called immediately
```

### Using Statement (Automatic Cleanup)

```csharp
public class FileHandler : IDisposable
{
    private string fileName;

    public FileHandler(string file)
    {
        fileName = file;
        Console.WriteLine($"File opened: {fileName}");
    }

    public void Dispose()
    {
        Console.WriteLine($"File closed: {fileName}");
    }
}

// Automatic cleanup
using (FileHandler handler = new FileHandler("data.txt"))
{
    // Use file handler
}  // Dispose called automatically
```

### Example: Destructor with Resource Cleanup

```csharp
using System;

namespace DestructorDemo
{
    public class DatabaseConnection
    {
        private string connectionString;
        private bool isConnected;

        public DatabaseConnection(string connStr)
        {
            connectionString = connStr;
            Connect();
        }

        private void Connect()
        {
            isConnected = true;
            Console.WriteLine($"Connected to: {connectionString}");
        }

        private void Disconnect()
        {
            isConnected = false;
            Console.WriteLine("Connection closed");
        }

        ~DatabaseConnection()
        {
            if (isConnected)
            {
                Disconnect();
            }
        }

        public void ExecuteQuery(string query)
        {
            if (isConnected)
            {
                Console.WriteLine($"Executing: {query}");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Destructors ===\n");

            DatabaseConnection db = new DatabaseConnection("Server=localhost");
            db.ExecuteQuery("SELECT * FROM Users");

            Console.WriteLine("Exiting program...");
            // Destructor will call when object is garbage collected
        }
    }
}
```

**Output:**
```
=== Destructors ===

Connected to: Server=localhost
Executing: SELECT * FROM Users
Exiting program...
Connection closed
```

### Key Points about Destructors

- Not called immediately - depends on garbage collector
- Use IDisposable for guaranteed cleanup
- Use `using` statement for automatic Dispose
- Rarely needed in modern C#
- Performance: destructors can slow down garbage collection
- Prefer IDisposable pattern for resource management

---

## 5. Garbage Collection in .NET

### What is Garbage Collection?

**Garbage Collection (GC)** is an automatic memory management system that frees memory used by objects no longer needed.

### Memory in .NET

#### Stack
- Stores value types (int, double, struct)
- Auto-cleaned when variable goes out of scope
- Fast access
- Limited size

#### Heap
- Stores reference types (objects, strings)
- Managed by garbage collector
- Slower access
- Larger size

```csharp
int num = 5;              // Stack: value stored directly
string text = "Hello";    // Heap: object stored, Stack: reference
Student student = new Student();  // Heap: object, Stack: reference
```

### How Garbage Collection Works

#### Step 1: Objects Become Unreachable

When no references point to an object, it's eligible for collection.

```csharp
Student student = new Student("Raj");
student = null;  // Object is now unreachable
// Garbage collector can clean it up
```

#### Step 2: GC Marks Unreachable Objects

The garbage collector identifies objects with no references.

#### Step 3: GC Compacts Memory

After removing unused objects, GC compacts remaining objects to free continuous memory blocks.

### Generations in GC

.NET uses generational garbage collection for efficiency:

**Generation 0:** Recently created objects
- Collected frequently
- Most objects die here

**Generation 1:** Objects that survived one collection
- Collected less frequently

**Generation 2:** Long-lived objects
- Collected rarely
- More efficient to keep

### GC Behavior Example

```csharp
using System;

namespace GarbageCollectionDemo
{
    public class Example
    {
        public string Name { get; set; }

        public Example(string name)
        {
            Name = name;
            Console.WriteLine($"Created: {name}");
        }

        ~Example()
        {
            Console.WriteLine($"Garbage collected: {Name}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Garbage Collection ===\n");

            // Create objects
            Example obj1 = new Example("Object 1");
            Example obj2 = new Example("Object 2");
            Example obj3 = new Example("Object 3");

            // Make objects unreachable
            obj1 = null;
            obj2 = null;

            Console.WriteLine("\nForcing garbage collection...");
            GC.Collect();  // Request GC (may not run immediately)
            GC.WaitForPendingFinalizers();  // Wait for finalizers

            Console.WriteLine("Done");
        }
    }
}
```

**Output:**
```
=== Garbage Collection ===

Created: Object 1
Created: Object 2
Created: Object 3

Forcing garbage collection...
Garbage collected: Object 1
Garbage collected: Object 2
Done
```

### Preventing Memory Leaks

#### Problem: Strong References

```csharp
public class EventRaiser
{
    public event EventHandler OnEvent;

    public void RaiseEvent()
    {
        OnEvent?.Invoke(this, EventArgs.Empty);
    }
}

public class Listener
{
    private EventRaiser raiser;

    public Listener(EventRaiser eventRaiser)
    {
        raiser = eventRaiser;
        raiser.OnEvent += Handler;  // Strong reference
    }

    private void Handler(object sender, EventArgs e)
    {
        Console.WriteLine("Event handled");
    }

    ~Listener()
    {
        Console.WriteLine("Listener garbage collected");
    }
}
```

#### Solution: Unsubscribe Events

```csharp
public class Listener : IDisposable
{
    private EventRaiser raiser;

    public Listener(EventRaiser eventRaiser)
    {
        raiser = eventRaiser;
        raiser.OnEvent += Handler;
    }

    private void Handler(object sender, EventArgs e)
    {
        Console.WriteLine("Event handled");
    }

    public void Dispose()
    {
        raiser.OnEvent -= Handler;  // Unsubscribe
    }
}
```

### GC Performance Considerations

**What slows down GC:**
- Creating many temporary objects
- Holding references to unused objects
- Large objects on heap

**Optimization tips:**
- Minimize object creation
- Release references promptly
- Use object pooling for frequently created objects
- Use IDisposable for resources

### Checking GC Statistics

```csharp
using System;

namespace GCStatistics
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== GC Statistics ===\n");

            // Get memory before
            long memBefore = GC.GetTotalMemory(false);
            Console.WriteLine($"Memory before: {memBefore} bytes");

            // Create many objects
            for (int i = 0; i < 10000; i++)
            {
                string temp = new string('a', 1000);
            }

            // Get memory after
            long memAfter = GC.GetTotalMemory(false);
            Console.WriteLine($"Memory after: {memAfter} bytes");

            // Force collection
            GC.Collect();
            long memFinal = GC.GetTotalMemory(false);
            Console.WriteLine($"Memory after GC: {memFinal} bytes");

            // Check generation counts
            Console.WriteLine($"\nGen 0 collections: {GC.CollectionCount(0)}");
            Console.WriteLine($"Gen 1 collections: {GC.CollectionCount(1)}");
            Console.WriteLine($"Gen 2 collections: {GC.CollectionCount(2)}");
        }
    }
}
```

### Best Practices for Memory Management

1. **Use IDisposable for resources**
```csharp
using (FileStream file = new FileStream("data.txt", FileMode.Open))
{
    // Use file
}  // Automatically disposed
```

2. **Release references**
```csharp
List<object> collection = GetLargeCollection();
DoSomething(collection);
collection = null;  // Release reference
```

3. **Avoid circular references**
```csharp
// ❌ Bad
class A { public B b; }
class B { public A a; }

// ✅ Good
class A { public WeakReference<B> b; }
```

4. **Don't call Finalize manually**
```csharp
// ❌ Bad
obj.Finalize();

// ✅ Good - Let GC handle it
obj = null;
```

### Example: Complete Memory Management

```csharp
using System;

namespace MemoryManagement
{
    public class Resource : IDisposable
    {
        private bool disposed = false;

        public Resource(string name)
        {
            Console.WriteLine($"Resource created: {name}");
        }

        public void Dispose()
        {
            Dispose(true);
            GC.SuppressFinalize(this);
        }

        protected virtual void Dispose(bool disposing)
        {
            if (!disposed)
            {
                if (disposing)
                {
                    Console.WriteLine("Managed resources released");
                }
                Console.WriteLine("Unmanaged resources released");
                disposed = true;
            }
        }

        ~Resource()
        {
            Dispose(false);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Complete Memory Management ===\n");

            // Proper resource management
            using (Resource res = new Resource("Important Data"))
            {
                // Use resource
            }  // Dispose called automatically

            Console.WriteLine("\nResource cleaned up successfully");

            GC.Collect();  // Force GC
        }
    }
}
```

**Output:**
```
=== Complete Memory Management ===

Resource created: Important Data
Managed resources released
Unmanaged resources released

Resource cleaned up successfully
```

### Key Points about Garbage Collection

- Automatic memory management
- Objects become eligible when unreachable
- Generational approach for efficiency
- Use IDisposable for immediate cleanup
- Avoid memory leaks with proper reference management
- Don't rely on finalizers/destructors alone

---

## Summary: OOP and Advanced Concepts

You've learned:
✅ Four pillars of OOP (Encapsulation, Inheritance, Polymorphism, Abstraction)
✅ Classes as blueprints and objects as instances
✅ Access modifiers for data protection
✅ Constructor types and their purposes
✅ Static vs instance constructors
✅ Private constructors for factory patterns
✅ Destructors and IDisposable pattern
✅ Garbage collection and memory management
✅ Best practices for memory safety

---

## Reference Links

1. **Object-Oriented Programming**: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/tutorials/oop
2. **Classes and Objects**: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/classes
3. **Constructors**: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/using-constructors
4. **Destructors and Finalizers**: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/finalizers
5. **IDisposable Pattern**: https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose
6. **Garbage Collection**: https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/
7. **Memory Management**: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/memory-and-pointers/
