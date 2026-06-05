# Advanced C# Concepts - Part 1: Memory Management & Data Handling

## Table of Contents
1. [Command Line Arguments in C#](#command-line-arguments-in-c)
2. [Boxing and Unboxing](#boxing-and-unboxing)
3. [Checked and Unchecked Keywords](#checked-and-unchecked-keywords)
4. [Nullable Types in C#](#nullable-types-in-c)
5. [Const vs Readonly Keywords](#const-vs-readonly-keywords)
6. [String Handling in C#](#string-handling-in-c)
7. [Properties in C#](#properties-in-c)
8. [Convert.ToString() vs ToString()](#convertttostring-vs-tostring)
9. [Immutable Types in C#](#immutable-types-in-c)
10. [Dynamic Memory Allocation (new keyword)](#dynamic-memory-allocation-new-keyword)
11. [Implicitly Typed Local Variables (var)](#implicitly-typed-local-variables-var)

---

## 1. Command Line Arguments in C#

### What are Command Line Arguments?

Command line arguments are values passed to a program when it starts from the command line (terminal/console). Think of them as inputs the program receives before Main() executes.

### Why Use Command Line Arguments?

- **Configuration**: Pass settings without hardcoding
- **Input**: Accept user input at startup
- **Automation**: Run programs with different parameters
- **Scripting**: Integrate with batch files or scripts

### How Command Line Arguments Work

**Syntax in Main method:**
```csharp
static void Main(string[] args)
{
    // args contains all command-line arguments
}
```

**The `string[] args` array:**
- Contains all arguments passed when program starts
- Each argument is a separate string
- First argument is at `args[0]`
- Array length is `args.Length`

### Example 1: Simple Command Line Arguments

```csharp
using System;

namespace CommandLineArgsDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Check if arguments were provided
            if (args.Length == 0)
            {
                Console.WriteLine("No arguments provided.");
                return;
            }

            // Display all arguments
            Console.WriteLine("=== Command Line Arguments ===");
            for (int i = 0; i < args.Length; i++)
            {
                Console.WriteLine($"args[{i}] = {args[i]}");
            }
        }
    }
}
```

**Running from Command Line:**
```bash
MyProgram.exe Hello World 123
```

**Output:**
```
=== Command Line Arguments ===
args[0] = Hello
args[1] = World
args[2] = 123
```

### Example 2: Practical Use - Calculate with Arguments

```csharp
using System;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            // Usage: Calculator 10 + 5
            if (args.Length < 3)
            {
                Console.WriteLine("Usage: Calculator <number1> <operator> <number2>");
                Console.WriteLine("Example: Calculator 10 + 5");
                return;
            }

            // Parse arguments
            int num1 = int.Parse(args[0]);
            string op = args[1];
            int num2 = int.Parse(args[2]);

            int result = 0;

            // Perform operation
            switch (op)
            {
                case "+":
                    result = num1 + num2;
                    break;
                case "-":
                    result = num1 - num2;
                    break;
                case "*":
                    result = num1 * num2;
                    break;
                case "/":
                    result = num1 / num2;
                    break;
                default:
                    Console.WriteLine("Invalid operator");
                    return;
            }

            Console.WriteLine($"{num1} {op} {num2} = {result}");
        }
    }
}
```

**Running:**
```bash
MyProgram.exe 10 + 5
```

**Output:**
```
10 + 5 = 15
```

### Example 3: Processing File Names

```csharp
using System;

namespace FileProcessor
{
    class Program
    {
        static void Main(string[] args)
        {
            if (args.Length == 0)
            {
                Console.WriteLine("Please provide file names as arguments.");
                return;
            }

            Console.WriteLine($"Processing {args.Length} files...\n");

            // Process each file
            foreach (string filename in args)
            {
                Console.WriteLine($"File: {filename}");
                Console.WriteLine($"Length: {filename.Length} characters");
                Console.WriteLine($"Uppercase: {filename.ToUpper()}");
                Console.WriteLine("---");
            }
        }
    }
}
```

**Running:**
```bash
MyProgram.exe document.txt image.jpg data.csv
```

**Output:**
```
Processing 3 files...

File: document.txt
Length: 12 characters
Uppercase: DOCUMENT.TXT
---
File: image.jpg
Length: 9 characters
Uppercase: IMAGE.JPG
---
File: data.csv
Length: 8 characters
Uppercase: DATA.CSV
---
```

### Running from Visual Studio

In Visual Studio, set command-line arguments:
1. Right-click project → **Properties**
2. Go to **Debug** tab
3. Enter arguments in **Command line arguments** field
4. Press F5 to run with arguments

### Key Points

- `args[0]` is the first argument (not the program name)
- Arguments are space-separated
- Quote arguments with spaces: `"Hello World"` is one argument
- All arguments come as strings; parse as needed
- Always check `args.Length` before accessing elements

---

## 2. Boxing and Unboxing

### What is Boxing?

Boxing is converting a **value type** to a **reference type** (object). The value is wrapped in an object on the heap.

**Example:**
```csharp
int num = 5;           // Value type on stack
object obj = num;      // Boxing: num is wrapped in object on heap
```

### What is Unboxing?

Unboxing is converting a **reference type** back to a **value type**.

**Example:**
```csharp
object obj = 5;        // Boxed int
int num = (int)obj;    // Unboxing: extract value from object
```

### Why Boxing and Unboxing?

Before C# generics, boxing allowed storing value types in collections with object type:

```csharp
ArrayList list = new ArrayList();
list.Add(5);        // Boxing: 5 wrapped in object
int num = (int)list[0];  // Unboxing: extract int from object
```

**Modern C# avoids this with generics:**
```csharp
List<int> list = new List<int>();
list.Add(5);        // No boxing: int stored directly
int num = list[0];  // No unboxing: direct access
```

### How Boxing Works

**Process:**
1. Allocate memory on heap for object
2. Copy value to heap
3. Return reference to heap object

**Memory visualization:**
```
Stack                          Heap
┌─────────────────┐           ┌─────────────┐
│ int num = 5     │           │  object     │
│                 │           │  [5]        │
└─────────────────┘           └─────────────┘
                              ↑
                         Reference to object
```

### Example 1: Boxing

```csharp
using System;

namespace BoxingDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Boxing Example ===\n");

            // Value type on stack
            int intValue = 100;
            Console.WriteLine($"Original int: {intValue}");

            // Boxing: value type → reference type
            object boxedValue = intValue;
            Console.WriteLine($"Boxed value: {boxedValue}");
            Console.WriteLine($"Type: {boxedValue.GetType()}");

            // Modify original
            intValue = 200;
            Console.WriteLine($"\nAfter changing intValue to 200:");
            Console.WriteLine($"intValue: {intValue}");
            Console.WriteLine($"boxedValue: {boxedValue}");  // Still 100!

            Console.WriteLine("\nExplanation: Boxed value is independent copy");
        }
    }
}
```

**Output:**
```
=== Boxing Example ===

Original int: 100
Boxed value: 100
Type: System.Int32

After changing intValue to 200:
intValue: 200
boxedValue: 100

Explanation: Boxed value is independent copy
```

### Example 2: Unboxing

```csharp
using System;

namespace UnboxingDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Unboxing Example ===\n");

            // Boxing
            double originalValue = 99.99;
            object boxedDouble = originalValue;
            Console.WriteLine($"Boxed value: {boxedDouble}");

            // Unboxing: reference type → value type
            double unboxedValue = (double)boxedDouble;
            Console.WriteLine($"Unboxed value: {unboxedValue}");

            // The unboxed value is independent
            originalValue = 50.50;
            Console.WriteLine($"\nAfter changing original to 50.50:");
            Console.WriteLine($"Original: {originalValue}");
            Console.WriteLine($"Unboxed: {unboxedValue}");  // Still 99.99
        }
    }
}
```

**Output:**
```
=== Unboxing Example ===

Boxed value: 99.99
Unboxed value: 99.99

After changing original to 50.50:
Original: 50.50
Unboxed: 99.99
```

### Example 3: Unboxing Errors

```csharp
using System;

namespace UnboxingErrors
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Unboxing Error Examples ===\n");

            // Error 1: Wrong type
            object boxedInt = 5;  // boxed as int
            
            try
            {
                double d = (double)boxedInt;  // ERROR: int cannot unbox to double
            }
            catch (InvalidCastException ex)
            {
                Console.WriteLine($"Error 1: {ex.Message}");
                Console.WriteLine("You must unbox to original type!\n");
            }

            // Error 2: Unboxing null
            object nullValue = null;
            
            try
            {
                int num = (int)nullValue;  // ERROR: cannot unbox null
            }
            catch (NullReferenceException ex)
            {
                Console.WriteLine($"Error 2: Cannot unbox null value\n");
            }

            // Correct way: use nullable types
            object boxedValue = 10;
            int? nullableInt = (int?)boxedValue;
            Console.WriteLine($"Safe unboxing with nullable: {nullableInt}");
        }
    }
}
```

**Output:**
```
=== Unboxing Error Examples ===

Error 1: Unable to cast object of type 'System.Int32' to type 'System.Double'.
You must unbox to original type!

Error 2: Cannot unbox null value

Safe unboxing with nullable: 10
```

### Performance Implications

**Boxing and unboxing are expensive:**
- Boxing allocates memory on heap
- Memory must be garbage collected later
- Type checking overhead
- Cache misses

**Solution: Use Generics**
```csharp
// ❌ Old way (boxing/unboxing)
ArrayList list = new ArrayList();
list.Add(5);              // Boxing
int num = (int)list[0];   // Unboxing

// ✅ New way (no boxing)
List<int> list = new List<int>();
list.Add(5);              // No boxing
int num = list[0];        // No unboxing
```

### Key Points

- Boxing creates a copy; changes to original don't affect boxed value
- Unboxing must match original type exactly
- Generics eliminate boxing for modern code
- Boxing allocates heap memory; unboxing doesn't

---

## 3. Checked and Unchecked Keywords

### What is Arithmetic Overflow?

Arithmetic overflow occurs when a calculation produces a result too large to fit in the variable's range.

**Example:**
```csharp
byte max = 255;
byte overflow = max + 1;  // Result is 256, but byte max is 255!
```

### Checked vs Unchecked

**Unchecked (default):** Silently wraps around (ignores overflow)
**Checked:** Throws OverflowException on overflow

### Unchecked Behavior (Default)

```csharp
using System;

namespace UncheckedDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Unchecked Overflow (Default) ===\n");

            // byte range: 0 to 255
            byte num = 255;
            Console.WriteLine($"byte max: {num}");

            // Overflow without checking
            num = num + 1;  // 255 + 1 = 256, wraps to 0
            Console.WriteLine($"After adding 1: {num}");  // Output: 0

            Console.WriteLine("\nExplanation: Value wraps around (256 % 256 = 0)");

            // Another example
            Console.WriteLine("\n=== Another Example ===");
            byte min = 0;
            Console.WriteLine($"byte min: {min}");
            
            min = min - 1;  // 0 - 1 = -1, wraps to 255
            Console.WriteLine($"After subtracting 1: {min}");  // Output: 255
        }
    }
}
```

**Output:**
```
=== Unchecked Overflow (Default) ===

byte max: 255
After adding 1: 0

Explanation: Value wraps around (256 % 256 = 0)

=== Another Example ===
byte min: 0
After subtracting 1: 255
```

### Checked Behavior

```csharp
using System;

namespace CheckedDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Checked Overflow ===\n");

            // byte range: 0 to 255
            byte num = 255;
            Console.WriteLine($"byte max: {num}");

            try
            {
                // With checked: overflow throws exception
                checked
                {
                    num = num + 1;  // Throws OverflowException
                }
            }
            catch (OverflowException ex)
            {
                Console.WriteLine($"Caught exception: {ex.Message}");
                Console.WriteLine("Overflow detected and handled!");
            }

            Console.WriteLine($"\nValue remains: {num}");
        }
    }
}
```

**Output:**
```
=== Checked Overflow ===

byte max: 255
Caught exception: Arithmetic operation resulted in an overflow.
Overflow detected and handled!

Value remains: 255
```

### Checked Block vs Checked Statement

**Checked statement (single operation):**
```csharp
checked
{
    int result = num1 + num2;
}
```

**Checked block (multiple operations):**
```csharp
checked
{
    int result1 = num1 + num2;
    int result2 = num3 * num4;
    int result3 = result1 - result2;
}
```

### Example: Real-World Use Case

```csharp
using System;

namespace SafeCalculator
{
    class Program
    {
        // Safe addition with overflow checking
        static int SafeAdd(int a, int b)
        {
            try
            {
                checked
                {
                    return a + b;
                }
            }
            catch (OverflowException)
            {
                Console.WriteLine("Warning: Addition caused overflow!");
                return int.MaxValue;  // Return max value instead
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine("=== Safe Calculator ===\n");

            int num1 = int.MaxValue;  // 2,147,483,647
            int num2 = 100;

            Console.WriteLine($"num1: {num1}");
            Console.WriteLine($"num2: {num2}");

            int result = SafeAdd(num1, num2);
            Console.WriteLine($"Result: {result}");
        }
    }
}
```

**Output:**
```
=== Safe Calculator ===

num1: 2147483647
num2: 100
Warning: Addition caused overflow!
Result: 2147483647
```

### When to Use Checked

- **Financial calculations:** Money must be accurate
- **Critical systems:** Medical, aviation, banking
- **User input validation:** Verify calculations are valid
- **API responses:** Ensure data integrity

### Key Points

- Unchecked is default (silent overflow)
- Checked throws OverflowException
- Use checked for critical calculations
- Performance: checked is slightly slower due to checking

---

## 4. Nullable Types in C#

### What are Nullable Types?

Nullable types allow value types (int, double, bool, etc.) to hold a **null** value, representing "no value" or "unknown".

**Syntax:**
```csharp
int? nullableInt = null;       // int can be null
double? nullableDouble = 99.5;
bool? nullableBool = null;
```

### Why Nullable Types?

Value types normally cannot be null:
```csharp
int age = null;  // ❌ Compiler error
```

But nullable types can:
```csharp
int? age = null;  // ✅ Allowed
```

**Use cases:**
- Database fields that can be NULL
- Optional parameters
- Unknown or missing values
- API responses with optional data

### Declaring Nullable Types

**Syntax:**
```csharp
// Using ? modifier
int? num = 5;
double? price = 99.99;
bool? isActive = null;

// Using Nullable<T> generic
Nullable<int> age = 30;
Nullable<double> salary = 50000.50;
```

**Both are equivalent. The `?` syntax is preferred.**

### Checking if Nullable Has Value

```csharp
using System;

namespace NullableDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Nullable Types ===\n");

            int? age = null;

            // Method 1: Check HasValue property
            if (age.HasValue)
            {
                Console.WriteLine($"Age: {age.Value}");
            }
            else
            {
                Console.WriteLine("Age is not provided");
            }

            // Method 2: Check against null
            if (age != null)
            {
                Console.WriteLine($"Age: {age}");
            }
            else
            {
                Console.WriteLine("Age is null");
            }

            Console.WriteLine("\n--- After Assignment ---");
            age = 25;

            if (age.HasValue)
            {
                Console.WriteLine($"Age: {age.Value}");
            }
            else
            {
                Console.WriteLine("Age is not provided");
            }
        }
    }
}
```

**Output:**
```
=== Nullable Types ===

Age is not provided
Age is null

--- After Assignment ---

Age: 25
```

### Properties of Nullable Types

| Property | Description | Example |
|----------|-------------|---------|
| `HasValue` | Returns true if holds value | `num.HasValue` |
| `Value` | Gets the value (throws if null) | `num.Value` |
| `GetValueOrDefault()` | Returns value or default | `num.GetValueOrDefault()` |

```csharp
int? num = null;

// These are equivalent:
int value1 = num.HasValue ? num.Value : 0;
int value2 = num.GetValueOrDefault();
int value3 = num ?? 0;  // Null coalescing operator
```

### Null Coalescing Operator (??)

The `??` operator returns the first non-null value.

**Syntax:**
```csharp
variable ?? defaultValue
```

**Example:**
```csharp
using System;

namespace NullCoalescingDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Null Coalescing Operator (??) ===\n");

            int? userAge = null;
            int defaultAge = 18;

            // Using ?? operator
            int displayAge = userAge ?? defaultAge;
            Console.WriteLine($"Display age: {displayAge}");  // Output: 18

            // Assign value
            userAge = 25;
            displayAge = userAge ?? defaultAge;
            Console.WriteLine($"Display age: {displayAge}");  // Output: 25

            // Null coalescing assignment (??=)
            string username = null;
            username ??= "Guest";
            Console.WriteLine($"Username: {username}");  // Output: Guest

            username ??= "Admin";
            Console.WriteLine($"Username: {username}");  // Output: Guest (already has value)
        }
    }
}
```

**Output:**
```
=== Null Coalescing Operator (??) ===

Display age: 18
Display age: 25
Username: Guest
Username: Guest
```

### Example: Database-Like Scenario

```csharp
using System;

namespace StudentRecord
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Student Records (with optional grades) ===\n");

            // Student with complete data
            string student1 = "Raj";
            int? grade1 = 95;

            DisplayStudent(student1, grade1);

            // Student without grade yet
            string student2 = "Priya";
            int? grade2 = null;

            DisplayStudent(student2, grade2);
        }

        static void DisplayStudent(string name, int? grade)
        {
            Console.WriteLine($"Student: {name}");
            
            if (grade.HasValue)
            {
                Console.WriteLine($"Grade: {grade.Value}");
                Console.WriteLine($"Status: Graded");
            }
            else
            {
                Console.WriteLine("Grade: Not yet assigned");
                Console.WriteLine("Status: Pending");
            }

            Console.WriteLine("---");
        }
    }
}
```

**Output:**
```
=== Student Records (with optional grades) ===

Student: Raj
Grade: 95
Status: Graded
---
Student: Priya
Grade: Not yet assigned
Status: Pending
---
```

### Operations with Nullable Types

```csharp
int? num1 = 5;
int? num2 = 3;
int? num3 = null;

// Addition with nullable
int? result1 = num1 + num2;    // 8
int? result2 = num1 + num3;    // null (if either is null, result is null)

Console.WriteLine(result1);     // 8
Console.WriteLine(result2);     // (nothing, it's null)

// Safe operation
int? safeResult = num1 + (num3 ?? 0);  // 5
```

### Key Points

- `int?` is shorthand for `Nullable<int>`
- `.HasValue` checks if contains value
- `.Value` gets the value (throws if null)
- `??` operator provides default value
- Operations with null result in null
- Use for optional data and database fields

---

## 5. Const vs Readonly Keywords

### Const Keyword

`const` defines a constant value that **cannot change**. Value is determined at **compile-time**.

**Syntax:**
```csharp
const dataType variableName = value;
```

**Example:**
```csharp
const double PI = 3.14159;
const int MONTHS_PER_YEAR = 12;
const string APP_NAME = "MyApp";
```

**Key Characteristics:**
- Value determined at compile-time
- Must be initialized when declared
- Cannot change after initialization
- Static by default (belongs to class, not instance)
- Value is hardcoded into code

### Readonly Keyword

`readonly` defines a value that **cannot change after initialization**. Value can be set at **runtime**.

**Syntax:**
```csharp
readonly dataType variableName;      // Can be initialized later
readonly dataType variableName = value;  // Or during declaration
```

**Example:**
```csharp
readonly int userId;

public Student(int id)
{
    userId = id;  // Set in constructor
}
```

**Key Characteristics:**
- Value determined at runtime
- Can be initialized in constructor
- Cannot change after initialization
- Can be instance-specific
- Each object can have different value

### Comparison Table

| Feature | const | readonly |
|---------|-------|----------|
| **Initialization** | Compile-time | Compile-time or runtime |
| **Where to init** | At declaration only | Declaration or constructor |
| **Modifiable** | Never | Never (after init) |
| **Static** | Yes (implicit) | No (can be instance) |
| **Performance** | Faster (hardcoded) | Slightly slower |
| **Scope** | Class-level | Class or instance |

### Example 1: Const

```csharp
using System;

namespace ConstDemo
{
    class Program
    {
        // Const values are compile-time constants
        const double PI = 3.14159;
        const int MAX_USERS = 100;
        const string COMPANY = "TechCorp";

        static void Main(string[] args)
        {
            Console.WriteLine("=== Const Keyword ===\n");

            Console.WriteLine($"PI: {PI}");
            Console.WriteLine($"MAX_USERS: {MAX_USERS}");
            Console.WriteLine($"COMPANY: {COMPANY}");

            // Try to modify const (❌ Compiler error)
            // PI = 3.14;  // ERROR: const is read-only

            // Calculate circle area
            double radius = 5;
            double area = PI * radius * radius;
            Console.WriteLine($"\nArea of circle (radius {radius}): {area}");
        }
    }
}
```

**Output:**
```
=== Const Keyword ===

PI: 3.14159
MAX_USERS: 100
COMPANY: TechCorp

Area of circle (radius 5): 78.5395
```

### Example 2: Readonly

```csharp
using System;

namespace ReadonlyDemo
{
    class Student
    {
        readonly int studentId;
        readonly string name;
        readonly DateTime enrollmentDate;

        public Student(int id, string studentName)
        {
            // Initialize in constructor
            studentId = id;
            name = studentName;
            enrollmentDate = DateTime.Now;
        }

        public void DisplayInfo()
        {
            Console.WriteLine($"ID: {studentId}");
            Console.WriteLine($"Name: {name}");
            Console.WriteLine($"Enrolled: {enrollmentDate}");
        }

        // Try to modify readonly (❌ Error)
        public void TryModify()
        {
            // studentId = 200;  // ERROR: cannot modify readonly
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Readonly Keyword ===\n");

            Student student1 = new Student(1, "Raj");
            student1.DisplayInfo();

            Console.WriteLine();

            Student student2 = new Student(2, "Priya");
            student2.DisplayInfo();

            Console.WriteLine("\nEach student has different ID (set in constructor)");
        }
    }
}
```

**Output:**
```
=== Readonly Keyword ===

ID: 1
Name: Raj
Enrolled: 2/4/2026 1:31:00 PM

ID: 2
Name: Priya
Enrolled: 2/4/2026 1:31:01 PM

Each student has different ID (set in constructor)
```

### Example 3: Const vs Readonly Comparison

```csharp
using System;

namespace ConstVsReadonly
{
    class Configuration
    {
        // Const: Same for all, set at compile-time
        const string VERSION = "1.0.0";

        // Readonly: Can vary per instance, set at runtime
        readonly string configPath;
        readonly DateTime createdDate;

        public Configuration(string path)
        {
            configPath = path;
            createdDate = DateTime.Now;
        }

        public void Display()
        {
            Console.WriteLine($"VERSION (const): {VERSION}");
            Console.WriteLine($"Config Path (readonly): {configPath}");
            Console.WriteLine($"Created: {createdDate}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Const vs Readonly ===\n");

            Configuration config1 = new Configuration("C:\\App\\config1.ini");
            config1.Display();

            Console.WriteLine();

            Configuration config2 = new Configuration("D:\\Data\\config2.ini");
            config2.Display();

            Console.WriteLine("\nNote: VERSION is same for both");
            Console.WriteLine("Note: configPath and createdDate are different");
        }
    }
}
```

**Output:**
```
=== Const vs Readonly ===

VERSION (const): 1.0.0
Config Path (readonly): C:\App\config1.ini
Created: 2/4/2026 1:31:00 PM

VERSION (const): 1.0.0
Config Path (readonly): D:\Data\config2.ini
Created: 2/4/2026 1:31:01 PM

Note: VERSION is same for both
Note: configPath and createdDate are different
```

### When to Use Each

**Use `const` for:**
- Mathematical constants (PI, GRAVITY)
- Configuration values (APP_NAME, MAX_CONNECTIONS)
- Values never changing across application lifetime
- Performance-critical code

**Use `readonly` for:**
- Instance-specific data
- Values set in constructor
- Database records (created date, etc.)
- Immutable collections per instance

### Key Points

- `const` is compile-time, `readonly` is runtime
- `const` is implicit static, `readonly` can be instance
- Both prevent modification after initialization
- `const` is faster; `readonly` is more flexible

---

## 6. String Handling in C#

### String Basics

Strings are **immutable** in C#. Once created, they cannot be changed. Operations create new strings.

```csharp
string message = "Hello";
message = message + " World";  // Creates new string, old discarded
```

### Common String Methods

#### 1. **Length Property**
```csharp
string text = "Hello";
int length = text.Length;  // 5
```

#### 2. **Substring()**
Extract portion of string.

```csharp
string text = "Hello World";
string sub1 = text.Substring(0, 5);      // "Hello"
string sub2 = text.Substring(6);         // "World"
```

#### 3. **IndexOf()**
Find position of character or substring.

```csharp
string text = "Hello World";
int pos1 = text.IndexOf('o');            // 4 (first 'o')
int pos2 = text.IndexOf("World");        // 6
int notFound = text.IndexOf('z');        // -1 (not found)
```

#### 4. **Contains()**
Check if string contains substring.

```csharp
string text = "Hello World";
bool has1 = text.Contains("World");      // true
bool has2 = text.Contains("xyz");        // false
```

#### 5. **Split()**
Break string into parts.

```csharp
string csv = "apple,banana,orange";
string[] fruits = csv.Split(',');
// fruits[0] = "apple"
// fruits[1] = "banana"
// fruits[2] = "orange"
```

#### 6. **Replace()**
Replace substring.

```csharp
string text = "Hello World";
string modified = text.Replace("World", "C#");  // "Hello C#"
```

#### 7. **ToUpper() and ToLower()**
Change case.

```csharp
string text = "Hello";
string upper = text.ToUpper();           // "HELLO"
string lower = text.ToLower();           // "hello"
```

#### 8. **Trim(), TrimStart(), TrimEnd()**
Remove whitespace.

```csharp
string text = "  Hello  ";
string trim = text.Trim();               // "Hello"
string trimStart = text.TrimStart();     // "Hello  "
string trimEnd = text.TrimEnd();         // "  Hello"
```

#### 9. **StartsWith() and EndsWith()**
Check beginning or end.

```csharp
string filename = "document.pdf";
bool isPdf = filename.EndsWith(".pdf");          // true
bool isDoc = filename.StartsWith("doc");         // true
```

#### 10. **Compare() and Equals()**
Compare strings.

```csharp
string str1 = "Hello";
string str2 = "hello";

bool equal1 = str1 == str2;              // false (case-sensitive)
bool equal2 = str1.Equals(str2);         // false
bool equal3 = str1.Equals(str2, StringComparison.OrdinalIgnoreCase);  // true
```

### String Concatenation Methods

#### Method 1: Using + Operator
```csharp
string result = "Hello" + " " + "World";
```

#### Method 2: String Interpolation (Recommended)
```csharp
string name = "Raj";
int age = 25;
string message = $"Name: {name}, Age: {age}";
```

#### Method 3: String.Format()
```csharp
string message = String.Format("Name: {0}, Age: {1}", "Raj", 25);
```

#### Method 4: String.Join()
```csharp
string[] words = {"Hello", "World", "C#"};
string joined = String.Join(" ", words);  // "Hello World C#"
```

### Practical Example: String Processing

```csharp
using System;

namespace StringHandling
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== String Handling ===\n");

            string text = "  Welcome to C# Programming!  ";

            // Trim whitespace
            string trimmed = text.Trim();
            Console.WriteLine($"Original: '{text}'");
            Console.WriteLine($"Trimmed: '{trimmed}'");

            // Split by spaces
            string[] words = trimmed.Split(' ');
            Console.WriteLine($"\nWords: {words.Length}");
            foreach (string word in words)
            {
                Console.WriteLine($"  - {word}");
            }

            // Find and replace
            string modified = trimmed.Replace("C#", "C-Sharp");
            Console.WriteLine($"\nReplaced: {modified}");

            // Check properties
            Console.WriteLine($"\nString starts with 'Welcome': {trimmed.StartsWith("Welcome")}");
            Console.WriteLine($"String contains 'Program': {trimmed.Contains("Program")}");
            Console.WriteLine($"String length: {trimmed.Length}");

            // Substring
            string portion = trimmed.Substring(0, 7);
            Console.WriteLine($"First 7 chars: {portion}");

            // Case conversion
            Console.WriteLine($"\nUppercase: {trimmed.ToUpper()}");
            Console.WriteLine($"Lowercase: {trimmed.ToLower()}");
        }
    }
}
```

**Output:**
```
=== String Handling ===

Original: '  Welcome to C# Programming!  '
Trimmed: 'Welcome to C# Programming!'

Words: 4
  - Welcome
  - to
  - C#
  - Programming!

Replaced: Welcome to C-Sharp Programming!

String starts with 'Welcome': True
String contains 'Program': True
String length: 29

First 7 chars: Welcome

Uppercase: WELCOME TO C# PROGRAMMING!
Lowercase: welcome to c# programming!
```

---

## 7. Properties in C#

### What are Properties?

Properties provide **controlled access** to class fields. They act like smart variables with custom logic for getting and setting values.

**Without properties:**
```csharp
public class Student
{
    public int age;  // Direct access - can set to negative!
}

Student s = new Student();
s.age = -5;  // ❌ Invalid but allowed
```

**With properties:**
```csharp
public class Student
{
    private int age;
    
    public int Age
    {
        get { return age; }
        set 
        { 
            if (value >= 0)
                age = value;
        }
    }
}

Student s = new Student();
s.Age = -5;  // ❌ Not allowed - property validates
```

### Types of Properties

#### 1. **Auto-Implemented Properties** (Simplest)

The compiler creates the backing field automatically.

```csharp
public class Student
{
    public string Name { get; set; }           // Can read and write
    public int Age { get; set; }               // Can read and write
    public string Email { get; private set; }  // Only write in class
}

// Usage
Student s = new Student();
s.Name = "Raj";        // Uses setter
s.Age = 25;            // Uses setter
string name = s.Name;  // Uses getter
```

#### 2. **Full Properties** (With Custom Logic)

You control the backing field and add logic.

```csharp
public class Student
{
    private int age;
    
    public int Age
    {
        get
        {
            return age;
        }
        set
        {
            if (value >= 0 && value <= 120)
                age = value;
            else
                Console.WriteLine("Invalid age!");
        }
    }
}

// Usage
Student s = new Student();
s.Age = 25;   // Valid
s.Age = -5;   // Invalid - prints error
```

#### 3. **Read-Only Properties**

Only getter, no setter.

```csharp
public class Student
{
    public DateTime EnrollmentDate { get; }  // Set only in constructor
    
    public Student()
    {
        EnrollmentDate = DateTime.Now;
    }
}

// Usage
Student s = new Student();
// s.EnrollmentDate = DateTime.Now;  // ❌ Error - no setter
Console.WriteLine(s.EnrollmentDate);  // ✅ Can read
```

#### 4. **Write-Only Properties** (Rare)

Only setter, no getter. Uncommon but possible.

```csharp
public class Account
{
    private string password;
    
    public string Password
    {
        set { password = value; }
        // No getter - cannot read password
    }
}
```

### Example: Complete Property Implementation

```csharp
using System;

namespace PropertyDemo
{
    class Student
    {
        private string name;
        private int age;
        private double gpa;

        // Property with validation
        public string Name
        {
            get { return name; }
            set { name = value ?? "Unknown"; }
        }

        // Property with range validation
        public int Age
        {
            get { return age; }
            set
            {
                if (value >= 0 && value <= 150)
                    age = value;
                else
                    throw new ArgumentException("Age must be 0-150");
            }
        }

        // Property with calculation
        public double GPA
        {
            get { return Math.Round(gpa, 2); }  // Always round to 2 decimals
            set { gpa = value; }
        }

        // Read-only property
        public bool IsEligibleForHonors
        {
            get { return gpa >= 3.5; }
        }

        // Auto-property
        public string StudentId { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Properties Demo ===\n");

            Student student = new Student();

            // Using properties
            student.Name = "Raj Kumar";
            student.Age = 20;
            student.GPA = 3.75;
            student.StudentId = "STU001";

            // Reading properties
            Console.WriteLine($"Name: {student.Name}");
            Console.WriteLine($"Age: {student.Age}");
            Console.WriteLine($"GPA: {student.GPA}");
            Console.WriteLine($"ID: {student.StudentId}");
            Console.WriteLine($"Eligible for Honors: {student.IsEligibleForHonors}");

            // Test validation
            Console.WriteLine("\n--- Testing Validation ---");
            try
            {
                student.Age = 200;  // Invalid
            }
            catch (ArgumentException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }
        }
    }
}
```

**Output:**
```
=== Properties Demo ===

Name: Raj Kumar
Age: 20
GPA: 3.75
ID: STU001
Eligible for Honors: True

--- Testing Validation ---
Error: Age must be 0-150
```

### Property Access Modifiers

Control who can get/set a property:

```csharp
public class Account
{
    // Public get, private set (only internal modification)
    public string Username { get; private set; }
    
    // Private get, public set (unusual)
    public string Password { private get; set; }
    
    // Internal get, internal set (within assembly only)
    internal string Notes { get; set; }
}
```

### Key Points

- Properties enable data validation
- Auto-properties simplify getter/setter creation
- Can have different access levels for get/set
- Computed properties calculate values on demand
- Properties are preferred over public fields
- Enable encapsulation and data protection

---

## 8. Convert.ToString() vs ToString()

### ToString() Method

Every object in C# has a `ToString()` method inherited from `System.Object`.

```csharp
int num = 42;
string str = num.ToString();  // "42"

double price = 99.99;
string str2 = price.ToString();  // "99.99"
```

### Convert.ToString() Method

`Convert.ToString()` is a static method in System namespace that safely converts to string.

```csharp
int num = 42;
string str = Convert.ToString(num);  // "42"

object obj = null;
string str2 = Convert.ToString(obj);  // "" (empty string, not error!)
```

### Key Differences

| Feature | ToString() | Convert.ToString() |
|---------|-----------|------------------|
| **Method Type** | Instance method | Static method |
| **Null handling** | Throws NullReferenceException | Returns empty string |
| **Formatting** | Limited options | Supports format strings |
| **Type** | Available on any object | From System namespace |

### Comparison Examples

#### Example 1: Null Handling

```csharp
using System;

namespace ToStringVsConvert
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Null Handling ===\n");

            int? nullableInt = null;

            // ToString() on null - ERROR
            try
            {
                string result1 = nullableInt.ToString();
                Console.WriteLine(result1);
            }
            catch (NullReferenceException ex)
            {
                Console.WriteLine($"ToString() Error: {ex.Message}");
            }

            // Convert.ToString() on null - Safe
            string result2 = Convert.ToString(nullableInt);
            Console.WriteLine($"Convert.ToString() Result: '{result2}'");
        }
    }
}
```

**Output:**
```
=== Null Handling ===

ToString() Error: Object reference not set to an instance of an object.
Convert.ToString() Result: ''
```

#### Example 2: Format Strings

```csharp
using System;

namespace Formatting
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Format Strings ===\n");

            double price = 99.99;
            int count = 42;

            // ToString() with format
            Console.WriteLine("ToString() with format:");
            Console.WriteLine($"Currency: {price.ToString("C")}");      // $99.99
            Console.WriteLine($"Two decimals: {price.ToString("F2")}");  // 99.99
            Console.WriteLine($"Percent: {0.15.ToString("P")}");        // 15.00%

            // Convert.ToString() basic
            Console.WriteLine("\nConvert.ToString():");
            Console.WriteLine($"Basic: {Convert.ToString(price)}");      // 99.99
            Console.WriteLine($"Basic: {Convert.ToString(count)}");      // 42
        }
    }
}
```

**Output:**
```
=== Format Strings ===

ToString() with format:
Currency: $99.99
Two decimals: 99.99
Percent: 15.00%

Convert.ToString()
Basic: 99.99
Basic: 42
```

### When to Use Each

**Use `ToString()`:**
- When value is guaranteed non-null
- Need formatting options
- Inside class implementation
- String interpolation

**Use `Convert.ToString()`:**
- When value might be null
- Safe conversion needed
- Converting from `object` type
- User input that might be null

### Example: Safe Conversion Pattern

```csharp
using System;

namespace SafeConversion
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Safe Conversion ===\n");

            // User input might be null
            object userInput = null;

            // Safe way
            string result = Convert.ToString(userInput) ?? "No input";
            Console.WriteLine($"Result: {result}");

            // With actual value
            userInput = 42;
            result = Convert.ToString(userInput) ?? "No input";
            Console.WriteLine($"Result: {result}");
        }
    }
}
```

**Output:**
```
=== Safe Conversion ===

Result: No input
Result: 42
```

### Key Points

- `ToString()` is instance method, `Convert.ToString()` is static
- `Convert.ToString(null)` returns empty string
- `null.ToString()` throws NullReferenceException
- Use `Convert.ToString()` for safer null handling
- Use `ToString()` for formatting options

---

## 9. Immutable Types in C#

### What are Immutable Types?

Immutable types **cannot be changed** after creation. Every modification creates a new instance.

### Value Types are Immutable by Default

```csharp
int num = 5;
num = 10;  // Creates new int, old value discarded
```

### String is Immutable

```csharp
string message = "Hello";
message = message + " World";  // Creates new string
// Original "Hello" still exists in memory until garbage collected
```

### Immutable Reference Types

You can create immutable classes using `readonly`:

```csharp
public class ImmutablePoint
{
    public readonly int X;
    public readonly int Y;

    public ImmutablePoint(int x, int y)
    {
        X = x;
        Y = y;
    }
    
    // Method returns new instance instead of modifying
    public ImmutablePoint Move(int dx, int dy)
    {
        return new ImmutablePoint(X + dx, Y + dy);
    }
}

// Usage
ImmutablePoint p1 = new ImmutablePoint(0, 0);
ImmutablePoint p2 = p1.Move(5, 5);  // p1 unchanged
```

### record Type (C# 9+) - Simplified Immutable

```csharp
public record Point(int X, int Y);

// All properties are read-only by default
Point p1 = new Point(0, 0);
Point p2 = new Point(5, 5);
// p1 = new Point(10, 10);  // Error: cannot reassign
```

### Example: Immutable Student Class

```csharp
using System;

namespace ImmutableDemo
{
    // Immutable class
    public class ImmutableStudent
    {
        public string Name { get; }
        public int Age { get; }
        public double GPA { get; }

        public ImmutableStudent(string name, int age, double gpa)
        {
            Name = name;
            Age = age;
            GPA = gpa;
        }

        // Methods return new instances
        public ImmutableStudent WithAge(int newAge)
        {
            return new ImmutableStudent(Name, newAge, GPA);
        }

        public ImmutableStudent WithGPA(double newGPA)
        {
            return new ImmutableStudent(Name, Age, newGPA);
        }

        public override string ToString()
        {
            return $"Name: {Name}, Age: {Age}, GPA: {GPA}";
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Immutable Types ===\n");

            ImmutableStudent student1 = new ImmutableStudent("Raj", 20, 3.5);
            Console.WriteLine($"Student 1: {student1}");

            // Update - creates new instance
            ImmutableStudent student2 = student1.WithAge(21);
            Console.WriteLine($"Student 2: {student2}");

            // Original unchanged
            Console.WriteLine($"Student 1 (unchanged): {student1}");

            // Chain updates
            ImmutableStudent student3 = student1
                .WithAge(22)
                .WithGPA(3.8);
            Console.WriteLine($"Student 3: {student3}");

            Console.WriteLine("\nNote: All are different instances");
        }
    }
}
```

**Output:**
```
=== Immutable Types ===

Student 1: Name: Raj, Age: 20, GPA: 3.5
Student 2: Name: Raj, Age: 21, GPA: 3.5
Student 1 (unchanged): Name: Raj, Age: 20, GPA: 3.5
Student 3: Name: Raj, Age: 22, GPA: 3.8

Note: All are different instances
```

### Advantages of Immutable Types

1. **Thread-safe** - No race conditions
2. **Predictable** - Cannot accidentally modify
3. **Easier debugging** - Values don't mysteriously change
4. **Better for collections** - Safe in dictionaries, sets

### Disadvantages

1. **Memory usage** - Creates new instances frequently
2. **Performance** - More garbage collection
3. **More code** - Need "With" methods

### Key Points

- Value types are immutable
- Strings are immutable
- Create immutable classes with `readonly` fields
- Use `record` for simpler immutable types
- Methods return new instances instead of modifying

---

## 10. Dynamic Memory Allocation (new keyword)

### What is the new Keyword?

The `new` keyword allocates memory on the **heap** for reference types and calls the **constructor**.

### Heap vs Stack

**Stack:**
- Stores value types (int, double, bool)
- Fast access
- Auto cleanup
- Limited size

**Heap:**
- Stores reference types (objects, strings)
- Slower access
- Garbage collection cleanup
- Larger size

```csharp
int num = 5;              // Stack: stores value 5
string text = "Hello";    // Heap: stores string, Stack: stores reference
```

### Allocating Objects with new

**Syntax:**
```csharp
ClassName variableName = new ClassName(arguments);
```

**Example:**
```csharp
Student student = new Student("Raj", 20);
List<int> numbers = new List<int>();
string message = new string('a', 5);  // "aaaaa"
```

### What Happens with new

1. **Allocate memory** on heap
2. **Call constructor** to initialize
3. **Return reference** to created object

```csharp
Student student = new Student("Raj", 20);
//      ^          ^     ^
//      |          |     Constructor call
//      |          Memory allocation
//      Reference stored on stack
```

### Example 1: Object Creation

```csharp
using System;

namespace NewKeywordDemo
{
    class Student
    {
        public string Name { get; set; }
        public int Age { get; set; }

        public Student(string name, int age)
        {
            Name = name;
            Age = age;
            Console.WriteLine($"Constructor called: {name}");
        }

        public void Display()
        {
            Console.WriteLine($"Name: {Name}, Age: {Age}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== new Keyword ===\n");

            // Create first object
            Student s1 = new Student("Raj", 20);
            s1.Display();

            Console.WriteLine();

            // Create second object
            Student s2 = new Student("Priya", 21);
            s2.Display();

            Console.WriteLine("\nBoth objects exist independently on heap");
        }
    }
}
```

**Output:**
```
=== new Keyword ===

Constructor called: Raj
Name: Raj, Age: 20

Constructor called: Priya
Name: Priya, Age: 21

Both objects exist independently on heap
```

### Example 2: Arrays with new

```csharp
using System;

namespace ArrayAllocation
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Array Allocation ===\n");

            // Allocate array on heap
            int[] numbers = new int[5];  // Creates array of 5 ints
            
            // Initialize values
            for (int i = 0; i < 5; i++)
            {
                numbers[i] = (i + 1) * 10;
            }

            // Display
            Console.WriteLine("Array contents:");
            foreach (int num in numbers)
            {
                Console.WriteLine(num);
            }

            // With initial values
            string[] fruits = new string[] { "Apple", "Banana", "Orange" };
            Console.WriteLine("\nFruits:");
            foreach (string fruit in fruits)
            {
                Console.WriteLine($"  - {fruit}");
            }
        }
    }
}
```

**Output:**
```
=== Array Allocation ===

Array contents:
10
20
30
40
50

Fruits:
  - Apple
  - Banana
  - Orange
```

### Example 3: Collections with new

```csharp
using System;
using System.Collections.Generic;

namespace CollectionAllocation
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Collection Allocation ===\n");

            // Create List
            List<int> numbers = new List<int>();
            numbers.Add(10);
            numbers.Add(20);
            numbers.Add(30);

            Console.WriteLine("List contents:");
            foreach (int num in numbers)
            {
                Console.WriteLine($"  {num}");
            }

            // Create Dictionary
            Dictionary<string, int> ages = new Dictionary<string, int>();
            ages["Raj"] = 20;
            ages["Priya"] = 21;
            ages["Aman"] = 22;

            Console.WriteLine("\nDictionary contents:");
            foreach (var pair in ages)
            {
                Console.WriteLine($"  {pair.Key}: {pair.Value}");
            }
        }
    }
}
```

**Output:**
```
=== Collection Allocation ===

List contents:
  10
  20
  30

Dictionary contents:
  Raj: 20
  Priya: 21
  Aman: 22
```

### Key Points

- `new` allocates memory on heap
- Calls constructor to initialize
- Returns reference to allocated memory
- Garbage collector cleans up unused objects
- Every time you use `new`, a new object is created

---

## 11. Implicitly Typed Local Variables (var)

### What is var?

`var` is a keyword that lets the **compiler infer the variable type** from the assigned value.

**Syntax:**
```csharp
var variableName = value;
```

**The compiler automatically determines the type.**

### How var Works

```csharp
var num = 5;                    // Compiler infers: int
var price = 99.99;              // Compiler infers: double
var message = "Hello";          // Compiler infers: string
var isActive = true;            // Compiler infers: bool
```

**At compile-time, these become:**
```csharp
int num = 5;
double price = 99.99;
string message = "Hello";
bool isActive = true;
```

### Rules for Using var

1. **Must be initialized** - Compiler needs value to infer type

```csharp
var num = 5;        // ✅ OK - infers int
var value;          // ❌ ERROR - no initial value
```

2. **Type is fixed** - Cannot change type later

```csharp
var num = 5;
num = "Hello";      // ❌ ERROR - num is int, not string
```

3. **Cannot be null** - Without explicit type

```csharp
var value = null;   // ❌ ERROR - cannot infer type from null
var value = (string)null;  // ✅ OK - explicitly typed
```

### Example 1: var with Different Types

```csharp
using System;
using System.Collections.Generic;

namespace VarDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== var Keyword ===\n");

            // Simple types
            var age = 25;                          // int
            var height = 5.9;                      // double
            var name = "Raj";                      // string
            var isStudent = true;                  // bool

            Console.WriteLine($"Age: {age} (type: {age.GetType()})");
            Console.WriteLine($"Height: {height} (type: {height.GetType()})");
            Console.WriteLine($"Name: {name} (type: {name.GetType()})");
            Console.WriteLine($"IsStudent: {isStudent} (type: {isStudent.GetType()})");

            // Complex types
            var numbers = new List<int> { 1, 2, 3 };
            Console.WriteLine($"\nList: {string.Join(", ", numbers)}");

            var dict = new Dictionary<string, int> { {"a", 1}, {"b", 2} };
            Console.WriteLine($"Dictionary count: {dict.Count}");
        }
    }
}
```

**Output:**
```
=== var Keyword ===

Age: 25 (type: System.Int32)
Height: 5.9 (type: System.Double)
Name: Raj (type: System.String)
IsStudent: True (type: System.Boolean)

List: 1, 2, 3
Dictionary count: 2
```

### Example 2: var with LINQ (Best Use Case)

LINQ queries often return complex types where `var` is most useful:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace VarWithLinq
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== var with LINQ ===\n");

            var students = new List<(string Name, int Age)>
            {
                ("Raj", 20),
                ("Priya", 21),
                ("Aman", 22),
                ("Zara", 19)
            };

            // var useful here - return type is complex
            var adults = students
                .Where(s => s.Age >= 20)
                .OrderBy(s => s.Name)
                .Select(s => new { s.Name, s.Age });

            Console.WriteLine("Adults (age >= 20):");
            foreach (var student in adults)
            {
                Console.WriteLine($"  {student.Name}: {student.Age}");
            }
        }
    }
}
```

**Output:**
```
=== var with LINQ ===

Adults (age >= 20):
  Aman: 22
  Priya: 21
  Raj: 20
```

### When to Use var

**Use var when:**
- Type is obvious from assignment
  ```csharp
  var numbers = new List<int>();  // Obviously a List<int>
  ```
- Used with LINQ or complex types
  ```csharp
  var result = students.Where(s => s.Age > 20);
  ```
- Local variables in short scope
  ```csharp
  var temp = CalculateValue();
  ```

**Don't use var when:**
- Type is not obvious
  ```csharp
  var result = GetValue();  // What type is this?
  ```
- Want explicit documentation
  ```csharp
  int age = 25;  // Clearer than var age = 25;
  ```
- Public API or method signatures
  ```csharp
  public int GetAge() { }  // Not var
  ```

### Example 3: var Limitations

```csharp
using System;

namespace VarLimitations
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== var Limitations ===\n");

            // Limitation 1: Cannot infer from null
            // var value = null;  // ERROR

            // Limitation 2: Type is fixed
            var num = 5;
            // num = "Hello";  // ERROR - num is int

            // Limitation 3: Cannot use in method parameters
            // public void Method(var parameter) { }  // ERROR

            // Limitation 4: Cannot use in return type
            // public var GetValue() { }  // ERROR

            Console.WriteLine("var has limitations");
            Console.WriteLine("Not suitable for method parameters/returns");
            Console.WriteLine("Type is inferred and fixed at declaration");
        }
    }
}
```

### Key Points

- `var` infers type from assigned value
- Type is fixed after declaration
- Cannot be null without explicit type
- Useful with LINQ and complex types
- Makes code shorter but less explicit
- Compiler converts to specific type at compile-time

---

## Summary: Memory Management & Data Handling

You've learned:
✅ Command-line arguments for program startup
✅ Boxing/unboxing for value type conversion
✅ Checked/unchecked for overflow handling
✅ Nullable types for optional values
✅ Const vs readonly for constants
✅ String manipulation methods
✅ Properties for data encapsulation
✅ ToString() vs Convert.ToString()
✅ Immutable types for thread-safety
✅ new keyword for memory allocation
✅ var keyword for type inference

These concepts form the foundation for advanced C# programming!

---

## Reference Links

1. **Microsoft Command-Line Arguments**: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/main-command-line
2. **Boxing and Unboxing**: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/types/boxing-and-unboxing
3. **Checked and Unchecked**: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/statements/checked-and-unchecked
4. **Nullable Types**: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types
5. **Const vs Readonly**: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/const
6. **String Methods**: https://learn.microsoft.com/en-us/dotnet/api/system.string
7. **Properties**: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/properties
8. **Implicitly Typed Variables**: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/implicitly-typed-local-variables
