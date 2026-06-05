# C# and .NET Core - Quick Reference & Cheat Sheet

## 1. Installation Checklist

- [ ] Download Visual Studio 2022 Community Edition from visualstudio.microsoft.com
- [ ] Run installer and select "ASP.NET and web development" workload
- [ ] Download .NET SDK from dotnet.microsoft.com
- [ ] Verify installation: Open Command Prompt and type `dotnet --version`
- [ ] Open Visual Studio and create first Console App

## 2. Your First Program - Template

```csharp
using System;

namespace MyFirstApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            Console.ReadKey();  // Pause before closing
        }
    }
}
```

## 3. Data Types Quick Reference

| Type | Size | Range | Example |
|------|------|-------|---------|
| `byte` | 1 byte | 0 - 255 | `byte age = 25;` |
| `short` | 2 bytes | -32K - 32K | `short count = 100;` |
| `int` | 4 bytes | -2B - 2B | `int population = 1000000;` |
| `long` | 8 bytes | Very large | `long distance = 999999999L;` |
| `float` | 4 bytes | ~7 digits | `float height = 5.9f;` |
| `double` | 8 bytes | ~15 digits | `double price = 99.99;` |
| `decimal` | 16 bytes | ~28 digits | `decimal salary = 50000.50m;` |
| `bool` | 1 byte | true/false | `bool isStudent = true;` |
| `char` | 2 bytes | Any character | `char grade = 'A';` |
| `string` | variable | Text | `string name = "Raj";` |

## 4. Console I/O Quick Reference

```csharp
// Output
Console.WriteLine("Text");      // Prints with newline
Console.Write("Text");          // Prints without newline

// Input
string input = Console.ReadLine();     // Read entire line
Console.ReadKey();                     // Wait for key press

// Formatting
Console.WriteLine("Value: " + value);
Console.WriteLine($"Value: {value}");  // String interpolation (preferred)
```

## 5. Control Flow Quick Reference

```csharp
// if-else
if (condition)
{
    // Do something
}
else if (otherCondition)
{
    // Do something else
}
else
{
    // Default case
}

// switch
switch (variable)
{
    case value1:
        // Code
        break;
    case value2:
        // Code
        break;
    default:
        // Code
        break;
}
```

## 6. Loops Quick Reference

```csharp
// for loop - specific number of iterations
for (int i = 0; i < 10; i++)
{
    Console.WriteLine(i);
}

// while loop - continues while condition is true
int count = 0;
while (count < 10)
{
    Console.WriteLine(count);
    count++;
}

// do-while - executes at least once
int num = 0;
do
{
    Console.WriteLine(num);
    num++;
} while (num < 10);

// foreach - iterate through collection
int[] numbers = { 1, 2, 3, 4, 5 };
foreach (int num in numbers)
{
    Console.WriteLine(num);
}
```

## 7. Loop Controls

```csharp
// break - exit loop
for (int i = 0; i < 10; i++)
{
    if (i == 5)
        break;  // Exit when i equals 5
    Console.WriteLine(i);
}

// continue - skip to next iteration
for (int i = 0; i < 10; i++)
{
    if (i == 5)
        continue;  // Skip 5
    Console.WriteLine(i);
}
```

## 8. Methods/Functions Quick Reference

```csharp
// Method with no parameters, no return
static void Greet()
{
    Console.WriteLine("Hello!");
}

// Method with parameters, no return
static void Greet(string name)
{
    Console.WriteLine("Hello, " + name);
}

// Method with no parameters, with return
static int GetNumber()
{
    return 42;
}

// Method with parameters and return
static int Add(int a, int b)
{
    return a + b;
}

// Calling methods
Greet();
Greet("Raj");
int num = GetNumber();
int sum = Add(5, 10);
```

## 9. Type Casting Examples

```csharp
// Implicit (automatic, safe)
int num = 100;
double d = num;  // int fits in double

// Explicit (manual, may lose data)
double d = 99.99;
int num = (int)d;  // d becomes 99 (loses .99)

// String conversion
string str = "123";
int num = int.Parse(str);      // Convert string to int
string numStr = num.ToString(); // Convert int to string

// Safer conversion
if (int.TryParse(str, out int result))
{
    // Conversion successful
}
```

## 10. Call by Value vs Reference

```csharp
// Call by Value (copy is passed)
static void Modify(int x)
{
    x = 100;  // Changes local copy, not original
}

int num = 5;
Modify(num);
Console.WriteLine(num);  // Still 5

// Call by Reference (original is passed)
static void Modify(ref int x)
{
    x = 100;  // Changes original variable
}

int num = 5;
Modify(ref num);
Console.WriteLine(num);  // Now 100
```

## 11. Code Execution Flow

```
C# Source Code (.cs)
        ↓
C# Compiler (csc.exe)
        ↓
CIL Bytecode (.exe/.dll)
        ↓
.NET Runtime (CoreCLR)
        ↓
JIT Compiler
        ↓
Native Machine Code
        ↓
CPU Execution
```

## 12. Common CLI Commands

```bash
# Create new console project
dotnet new console -n ProjectName

# Create project in specific directory
dotnet new console -n ProjectName -o C:\Projects

# Build project
dotnet build

# Run project
dotnet run

# Create and run in one command
dotnet new console && dotnet run

# List installed SDKs
dotnet --list-sdks
```

## 13. Variable Naming Conventions

```csharp
✓ Good Examples:
int age = 20;
string firstName = "Raj";
double averageScore = 85.5;
bool isStudent = true;

✗ Avoid:
int a = 20;              // Not descriptive
string fname = "Raj";    // Ambiguous abbreviation
int Age = 20;            // Wrong case (use for classes)
string first-name = "";  // Invalid character
int 1st = 0;             // Cannot start with number
```

## 14. Operators Quick Reference

```csharp
// Arithmetic
int sum = 5 + 3;        // 8
int diff = 5 - 3;       // 2
int product = 5 * 3;    // 15
int quotient = 5 / 3;   // 1 (integer division)
int remainder = 5 % 3;  // 2 (modulo)

// Comparison
5 > 3      // true
5 < 3      // false
5 >= 5     // true
5 <= 3     // false
5 == 5     // true (equal)
5 != 3     // true (not equal)

// Logical
true && true    // true (AND)
true || false   // true (OR)
!true           // false (NOT)

// String concatenation
"Hello" + " " + "World"  // "Hello World"
```

## 15. Debugging Tips

```csharp
// Print debugging
Console.WriteLine("Variable value: " + myVar);

// Breakpoints (in Visual Studio)
// Click on left margin to set breakpoint
// Press F5 to run with debugger
// Press F10 to step through code

// Try-catch for error handling
try
{
    int num = int.Parse("abc");  // Will throw error
}
catch (Exception ex)
{
    Console.WriteLine("Error: " + ex.Message);
}
```

## 16. Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax Error | Missing semicolon or bracket | Check all statements end with `;` and brackets match |
| Type Mismatch | Assigning wrong type to variable | Ensure types match or use explicit casting |
| NullReferenceException | Using null variable | Check if variable is initialized before use |
| Format Exception | Invalid type conversion | Use `TryParse` instead of `Parse` for safety |
| Index Out of Range | Accessing array beyond size | Ensure index < array.Length |

## 17. Project Structure

```
MyProject/
├── MyProject.csproj          # Project configuration
├── Program.cs                 # Main program file
├── bin/                       # Compiled output
│   └── Debug/
│       └── MyProject.dll
└── obj/                       # Build intermediate files
```

## 18. .NET vs .NET Framework Comparison

| Feature | .NET Core | .NET Framework |
|---------|-----------|----------------|
| Platform | Windows, Linux, macOS | Windows only |
| Performance | Faster | Slower |
| New Projects | ✓ Use this | ✗ Don't use |
| Legacy Apps | ✗ Not suitable | ✓ Use this |
| Open Source | ✓ Yes | Partial |
| Cloud Ready | ✓ Yes | ✗ No |
| Microservices | ✓ Yes | ✗ No |

## 19. VS Code Setup for C# (Alternative to Visual Studio)

1. Install VS Code from code.visualstudio.com
2. Install C# extension (by Microsoft)
3. Create project: `dotnet new console -n ProjectName`
4. Open folder in VS Code
5. Run: `dotnet run` in terminal

## 20. Important Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| F5 | Run program with debugger |
| Ctrl+F5 | Run without debugger |
| F10 | Step over (debugging) |
| F11 | Step into (debugging) |
| Shift+F11 | Step out (debugging) |
| Ctrl+G | Go to line |
| Ctrl+/ | Comment/uncomment |
| Ctrl+K+D | Format document |
| Ctrl+Shift+B | Build project |

---

## Practice Exercises

### Exercise 1: Simple Calculator
Create a program that:
- Takes two numbers as input from user
- Displays menu: Add, Subtract, Multiply, Divide
- Performs selected operation
- Shows result

### Exercise 2: Grade Calculator
Create a program that:
- Takes marks from 0-100
- Assigns grade: A(90+), B(80-89), C(70-79), D(60-69), F(<60)
- Shows feedback for each grade

### Exercise 3: Multiplication Table
Create a program that:
- Takes a number from user
- Prints multiplication table (1-10)
- Uses a loop

### Exercise 4: Number Guessing Game
Create a program that:
- Generates random number 1-100
- Lets user guess
- Gives hints (too high, too low)
- Counts attempts
- Congratulates when correct

### Exercise 5: Student Management
Create a program that:
- Stores student name, age, GPA
- Displays all information
- Calculates if eligible for honors (GPA >= 3.5)

---

## Resources Summary

- **Official Documentation**: learn.microsoft.com
- **Video Tutorials**: YouTube (search "C# for beginners")
- **Interactive Learning**: LeetCode, HackerRank
- **Community Help**: Stack Overflow, Reddit r/csharp
- **Open Source Code**: GitHub

---

**Pro Tips for Success:**
1. Code every day, even for 15 minutes
2. Don't just read - actually type the code
3. Break problems into smaller pieces
4. Test your code frequently
5. Read error messages carefully
6. Join programmer communities
7. Build real projects

**You've got this! Happy coding! 🚀**
