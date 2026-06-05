# Complete Guide to C# and .NET Core - From Beginner to First Console Application

## Table of Contents
1. [Introduction to .NET Core Framework](#introduction-to-net-core-framework)
2. [Introduction to C# Programming Language](#introduction-to-c-programming-language)
3. [Setting Up Your Environment](#setting-up-your-environment)
4. [Download and Install Visual Studio 2022](#download-and-install-visual-studio-2022)
5. [Download and Install .NET Core SDK](#download-and-install-net-core-sdk)
6. [.NET Core vs .NET Framework](#net-core-vs-net-framework)
7. [Code Execution Process](#code-execution-process)
8. [Creating Your First Console Application](#creating-your-first-console-application)
9. [Basic Structure of a C# Program](#basic-structure-of-a-c-program)
10. [Console Class Methods and Properties](#console-class-methods-and-properties)
11. [Data Types, Variables, and Literals](#data-types-variables-and-literals)
12. [Type Casting](#type-casting)
13. [Control Flow Statements](#control-flow-statements)
14. [Loop Controls](#loop-controls)
15. [Functions and Methods](#functions-and-methods)

---

## 1. Introduction to .NET Core Framework

### What is .NET Core?

.NET Core is a modern, open-source, cross-platform framework developed by Microsoft for building applications. Unlike the traditional .NET Framework which only runs on Windows, .NET Core can run on Windows, macOS, and Linux.

### Key Characteristics of .NET Core:

- **Cross-Platform**: Write once, run everywhere (Windows, Linux, macOS)
- **Open-Source**: Freely available on GitHub
- **Modular Architecture**: Include only the components you need
- **High Performance**: Optimized for speed and efficiency
- **Cloud-Native**: Perfect for microservices and containerized applications
- **Modern**: Built with contemporary development practices

### What Can You Build with .NET Core?

- Console applications
- Web applications (ASP.NET Core)
- Mobile apps (with Xamarin)
- Desktop applications (WPF, WinForms)
- Games (Unity)
- IoT applications
- Microservices

### .NET Core Versions Timeline:

- **.NET Core 1.0** (2016): Initial release with basic functionality
- **.NET Core 2.0 to 2.2**: Performance improvements and features
- **.NET Core 3.0 to 3.1**: Support for desktop applications
- **.NET 5.0+**: Unified platform combining .NET Core and .NET Framework

---

## 2. Introduction to C# Programming Language

### What is C#?

C# (pronounced "C-sharp") is a modern, object-oriented programming language developed by Microsoft. It runs on the .NET Core runtime and combines the power of C++ with the simplicity of Visual Basic.

### Why Learn C#?

1. **Easy to Learn**: Clean, intuitive syntax similar to C (which you already know)
2. **Strongly Typed**: Catches errors at compile time
3. **Object-Oriented**: Supports classes, inheritance, polymorphism
4. **Rich Library**: Extensive built-in classes and frameworks
5. **Industry Demand**: Used by major companies worldwide
6. **Versatile**: Used for web, desktop, mobile, and game development

### C# vs C - Key Differences:

| Feature | C | C# |
|---------|---|-----|
| Platform | Procedural | Object-Oriented |
| Memory Management | Manual (malloc, free) | Automatic (Garbage Collection) |
| Type Safety | Weak | Strong |
| Built-in Data Structures | Limited | Extensive (List, Dictionary, etc.) |
| Error Handling | Limited | Try-catch-finally |
| Standard Library | Small | Huge (System namespace) |

### Advantages of C# Over C:

- No manual memory management - the garbage collector handles it
- Built-in string support (C# strings are objects)
- Exception handling (try-catch)
- Rich collection classes (List, Dictionary)
- LINQ for database queries
- Automatic type inference with `var` keyword
- Async/await for asynchronous programming

---

## 3. Setting Up Your Environment

### System Requirements for C# and .NET Core Development:

**Minimum:**
- Windows 10/11, macOS 10.15+, or any Linux distribution
- At least 2GB RAM (4GB recommended)
- 5GB free disk space

**Recommended:**
- Windows 10/11 Pro or higher
- 8GB+ RAM
- SSD for faster performance
- Internet connection (for downloading SDKs and packages)

### Installation Steps Overview:

1. Download Visual Studio 2022 Community Edition
2. Download and Install .NET Core SDK
3. Verify installation through command line
4. Create and run your first application

---

## 4. Download and Install Visual Studio 2022

Visual Studio is Microsoft's Integrated Development Environment (IDE) for C# development.

### Step-by-Step Installation:

#### Step 1: Download Visual Studio 2022

1. Visit: https://visualstudio.microsoft.com/downloads/
2. Look for "Visual Studio 2022" section
3. Click "Free download" under "Community Edition"
4. This downloads a small installer file (~1.5 MB)

#### Step 2: Run the Installer

1. Double-click the downloaded `.exe` file
2. The Visual Studio Installer application launches
3. Click "Continue" to proceed

#### Step 3: Select Workloads

The installer asks which development tools you want. For C# development, select:

- **.NET Desktop Development** (essential for C# console/desktop apps)
- **ASP.NET and web development** (if you want web development)
- **Azure development** (optional, for cloud development)

**For beginners, just select "ASP.NET and web development" which includes everything needed.**

#### Step 4: Choose Installation Location

- Default location: `C:\Program Files\Microsoft Visual Studio\2022\Community`
- You can change this if needed
- Ensure you have 10+ GB free space

#### Step 5: Click Install

- Click the "Install" button
- Installation takes 10-30 minutes depending on internet speed
- It will download and install all selected components

#### Step 6: Launch Visual Studio

- After installation completes, click "Launch"
- On first launch, Visual Studio will:
  - Load initial setup (15-30 seconds)
  - Ask you to sign in with Microsoft account (optional but recommended)
  - Configure your development environment

#### Step 7: First Launch Configuration

- Sign in with your Microsoft account or skip (click "Not now")
- Choose your development settings theme (Light/Dark)
- You're ready to start!

### Verifying Installation:

1. Open Visual Studio 2022
2. Go to **Help** → **About Microsoft Visual Studio**
3. You should see version information showing installation was successful

---

## 5. Download and Install .NET Core SDK

The .NET Core SDK includes everything needed to build and run .NET applications from command line.

### Step-by-Step Installation:

#### Step 1: Download .NET SDK

1. Visit: https://dotnet.microsoft.com/en-us/download/dotnet
2. Download the latest .NET SDK (e.g., .NET 8 or newer)
3. Choose your operating system (Windows x64 recommended)
4. Click download

#### Step 2: Run the Installer

1. Double-click the downloaded `.exe` file
2. Follow the installation wizard
3. Accept license terms
4. Click "Install"

#### Step 3: Verify Installation

Open Command Prompt or PowerShell and type:

```bash
dotnet --version
```

You should see output like: `8.0.0` (version number varies)

If you see this, installation was successful!

### Check All Installed SDKs:

```bash
dotnet --list-sdks
```

This shows all .NET versions installed on your machine.

---

## 6. .NET Core vs .NET Framework

### Understanding the Difference:

#### .NET Framework (Older)

- **Platform**: Windows only
- **Architecture**: Single large package
- **Performance**: Slower startup, higher memory usage
- **Development**: Mature, stable, many legacy apps
- **Modern Apps**: Not recommended for new projects
- **Desktop Support**: Yes (WPF, WinForms)
- **Web**: ASP.NET (older version)

#### .NET Core (Modern)

- **Platform**: Windows, Linux, macOS
- **Architecture**: Modular, lightweight
- **Performance**: Fast startup, efficient memory usage
- **Development**: Modern, actively maintained
- **Recommendation**: Use for all new projects
- **Desktop Support**: Limited (but improving)
- **Web**: ASP.NET Core (recommended)

### Comparison Table:

| Aspect | .NET Framework | .NET Core |
|--------|----------------|-----------|
| Cross-Platform | ❌ Windows only | ✅ Windows, Linux, macOS |
| Performance | Slower | Faster |
| Size | Large (~200MB+) | Small, modular |
| Modern Features | Limited | Extensive |
| Cloud-Ready | No | Yes |
| Microservices | Not ideal | Ideal |
| Open Source | Partial | Full |
| Future Updates | Limited | Continuous |

### Which Should You Use?

**Use .NET Core for:**
- New projects
- Cross-platform applications
- Cloud and microservices
- Modern web applications
- Performance-critical apps

**Use .NET Framework for:**
- Maintaining legacy applications
- Projects requiring Windows-only features
- Companies with existing .NET Framework investments

**Recommendation for Beginners: Always start with .NET Core.**

---

## 7. Code Execution Process

Understanding how C# code is executed helps you debug and optimize programs.

### The Journey of Your C# Code:

```
1. Source Code (.cs file)
        ↓
2. C# Compiler (csc.exe)
        ↓
3. Common Intermediate Language (CIL) bytecode (.dll or .exe)
        ↓
4. .NET Runtime (CoreCLR)
        ↓
5. Just-In-Time Compiler (JIT)
        ↓
6. Machine Code (Processor-specific)
        ↓
7. Execution on CPU
```

### Step-by-Step Explanation:

#### Step 1: Source Code
You write C# code in `.cs` files. Example: `Program.cs`

#### Step 2: Compilation
The C# compiler (`csc.exe`) reads your source code and:
- Checks for syntax errors
- Verifies type safety
- Converts code to CIL (Common Intermediate Language)
- Stores in `.dll` (class library) or `.exe` (executable) files

#### Step 3: CIL Bytecode
CIL is platform-independent intermediate code that:
- Is not machine code yet
- Can run on any platform with .NET runtime
- Is similar to Java's bytecode concept

#### Step 4: .NET Runtime (CoreCLR)
When you run the program:
- CoreCLR loads the CIL bytecode
- Initializes the runtime environment
- Manages memory and resources

#### Step 5: Just-In-Time (JIT) Compiler
- Converts CIL to native machine code
- Happens at runtime
- Only code being executed is compiled
- Results are cached for reuse

#### Step 6: Machine Code
Native code specific to:
- Your CPU architecture (x86, x64, ARM)
- Your operating system
- Can be executed directly by the processor

#### Step 7: Execution
The CPU executes machine code and produces results.

### Key Advantage: WORA (Write Once, Run Anywhere)

Because C# compiles to CIL first, the same compiled `.dll` file can run on Windows, Linux, and macOS as long as the .NET runtime is installed.

### Garbage Collection

After execution:
- Automatic garbage collection frees unused memory
- No manual `delete` or `free` like in C
- Makes memory management safer and easier

---

## 8. Creating Your First Console Application

### Method 1: Using Visual Studio (Easiest for Beginners)

#### Step 1: Create New Project

1. Open Visual Studio 2022
2. Click **Create a new project**
3. Search for **Console App** (.NET Core)
4. Select **Console App (.NET Core)** or **Console Application**
5. Click **Next**

#### Step 2: Configure Project

1. **Project name**: Enter `MyFirstApp` (or any name)
2. **Location**: Choose where to save (Documents is fine)
3. **Solution name**: Usually auto-filled, same as project name
4. Click **Next**

#### Step 3: Additional Information

1. **Framework**: Select latest .NET version (8.0 or newer)
2. Click **Create**

#### Step 4: Project Structure Appears

Visual Studio creates:
- `Program.cs` - Your main code file
- `MyFirstApp.csproj` - Project configuration file
- Other metadata files

#### Step 5: Start Coding

Default content in `Program.cs`:

```csharp
using System;

namespace MyFirstApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}
```

#### Step 6: Run Your Program

1. Press **F5** or click the **Play** button (green triangle)
2. A console window appears showing: `Hello, World!`
3. Press any key to close the window

**Congratulations! Your first C# program is running!**

### Method 2: Using .NET CLI (Command Line)

If you prefer command line:

#### Step 1: Open Command Prompt

1. Open Command Prompt or PowerShell
2. Navigate to where you want to create the project: `cd Documents`

#### Step 2: Create Console Application

```bash
dotnet new console -n MyFirstApp
```

This creates:
- A new folder `MyFirstApp`
- `Program.cs` file
- `MyFirstApp.csproj` file

#### Step 3: Navigate to Project

```bash
cd MyFirstApp
```

#### Step 4: Run the Application

```bash
dotnet run
```

Output: `Hello, World!`

#### Step 5: Open in Visual Studio

```bash
start .
```

This opens the folder in File Explorer. Double-click `MyFirstApp.csproj` to open in Visual Studio.

### Method 3: Using Visual Studio Code (Lightweight Alternative)

If you prefer VS Code:

#### Step 1: Install C# Extension

1. Open Visual Studio Code
2. Go to **Extensions** (Ctrl+Shift+X)
3. Search for "C#"
4. Install the official C# extension by Microsoft

#### Step 2: Create and Run

Use the CLI method above, then open the folder in VS Code:

```bash
code .
```

#### Step 3: Run Program

Open terminal in VS Code and type:

```bash
dotnet run
```

---

## 9. Basic Structure of a C# Program

Every C# program has a specific structure. Let's break it down:

### Complete Program Structure:

```csharp
using System;
using System.Collections.Generic;

namespace MyNamespace
{
    class Program
    {
        static void Main(string[] args)
        {
            // Your code here
            Console.WriteLine("Hello, World!");
        }
    }
}
```

### Breakdown of Each Component:

#### 1. **Using Statements**

```csharp
using System;
using System.Collections.Generic;
```

**What it does**: Imports namespaces to access their classes and methods

**Explanation**:
- `using System;` - Imports the System namespace, which contains fundamental classes like `Console`
- Without this, you'd need to write `System.Console.WriteLine()` instead of `Console.WriteLine()`
- Think of it like `#include` in C

**Common using statements**:
- `using System;` - Basic functionality
- `using System.Collections.Generic;` - List, Dictionary, etc.
- `using System.Linq;` - LINQ queries
- `using System.Text;` - String operations

#### 2. **Namespace Declaration**

```csharp
namespace MyNamespace
{
    // Code inside this namespace
}
```

**What it does**: Organizes code into logical groups to avoid naming conflicts

**Why needed**:
- Prevents two classes with same name from conflicting
- Organizes large projects into modules
- Example: `System.Collections` vs `System.IO`

**Real-world example**:
```csharp
namespace BankingApp.Accounts
{
    class AccountHolder { }
}

namespace BankingApp.Transactions
{
    class Transaction { }
}
```

Both can use `Transaction` class without conflict.

#### 3. **Class Declaration**

```csharp
class Program
{
    // Class members go here
}
```

**What it does**: Defines a class (blueprint for objects)

**Key points**:
- Every C# program must have at least one class
- The class name is `Program` by convention
- Can be public or internal (access modifiers)
- Contains data (fields) and behavior (methods)

**Example with multiple classes**:
```csharp
namespace SchoolApp
{
    class Student
    {
        string name;
        int age;
    }

    class Teacher
    {
        string name;
        string subject;
    }
}
```

#### 4. **Main Method**

```csharp
static void Main(string[] args)
{
    // Entry point of program
}
```

**What it does**: Entry point where program execution starts

**Breaking down the syntax**:

- **`static`** - Method belongs to the class, not instances. Called without creating an object.
  ```csharp
  Program.Main();  // Can call directly on class
  ```

- **`void`** - Method returns nothing
  ```csharp
  static int Calculate()  // Returns an integer
  static string GetName() // Returns a string
  static void DoSomething() // Returns nothing
  ```

- **`Main`** - Special method name recognized by .NET as entry point

- **`string[] args`** - Array of command-line arguments passed to program
  ```bash
  MyProgram.exe arg1 arg2 arg3
  // args[0] = "arg1"
  // args[1] = "arg2"
  // args[2] = "arg3"
  ```

#### 5. **Statements**

```csharp
Console.WriteLine("Hello, World!");
```

**What it does**: Executable code inside Main method

**Most common statements**:
- Variable declarations
- Console output
- Calculations
- Control flow (if, loops)
- Method calls

### Simplified Structure (Modern C#):

In recent .NET versions, you can skip the namespace and class:

```csharp
using System;

Console.WriteLine("Hello, World!");
```

**Advantages**:
- Fewer lines for simple programs
- Perfect for beginners
- Called "Top-level statements"

**Disadvantage**:
- Only one file can use top-level statements per project

### Complete Example with Explanations:

```csharp
using System;  // Import System namespace

namespace MyFirstProgram  // Namespace for organization
{
    class Program  // Main class
    {
        static void Main(string[] args)  // Entry point method
        {
            // This is where execution begins
            string name = "Raj";  // Variable declaration
            int age = 20;  // Another variable
            
            Console.WriteLine("Hello, " + name);  // Output
            Console.WriteLine("Your age is: " + age);  // Output
            
            // Program ends here
        }
    }
}
```

**Output**:
```
Hello, Raj
Your age is: 20
```

---

## 10. Console Class Methods and Properties

The `Console` class is used for input/output in console applications. It's in the `System` namespace.

### Main Console Methods:

#### 1. **Console.WriteLine() - Write Line**

```csharp
Console.WriteLine("Hello, World!");
```

**What it does**:
- Prints text to console
- Automatically moves cursor to next line after printing
- Adds a newline character at the end

**Examples**:
```csharp
Console.WriteLine("Hello");  // Output: Hello (cursor moves to next line)
Console.WriteLine("World");  // Output: World (on new line)
```

**Output**:
```
Hello
World
```

#### 2. **Console.Write() - Write (No Line)**

```csharp
Console.Write("Hello");
```

**What it does**:
- Prints text to console
- Does NOT move cursor to next line
- Cursor stays at same position

**Comparison with WriteLine**:
```csharp
Console.Write("Hello ");    // Cursor stays here
Console.Write("World!");    // Continues on same line
```

**Output**:
```
Hello World!
```

Versus with WriteLine:
```csharp
Console.WriteLine("Hello");  // Cursor moves to next line
Console.WriteLine("World!");
```

**Output**:
```
Hello
World!
```

#### 3. **Console.ReadLine() - Read Line of Text**

```csharp
string input = Console.ReadLine();
```

**What it does**:
- Waits for user to type something
- Returns text as a string
- Execution pauses until user presses Enter

**Real example**:
```csharp
Console.Write("Enter your name: ");
string name = Console.ReadLine();
Console.WriteLine("Hello, " + name);
```

**If user types "Raj" and presses Enter**:
```
Enter your name: Raj
Hello, Raj
```

#### 4. **Console.ReadKey() - Read Single Key**

```csharp
ConsoleKeyInfo keyInfo = Console.ReadKey();
```

**What it does**:
- Waits for user to press one key
- Returns a `ConsoleKeyInfo` object with key details
- Can read without showing the character

**Examples**:
```csharp
Console.WriteLine("Press any key to continue...");
Console.ReadKey();  // Waits for key press
Console.WriteLine("You pressed a key!");
```

**Reading specific key**:
```csharp
ConsoleKeyInfo keyInfo = Console.ReadKey();
if (keyInfo.Key == ConsoleKey.Escape)
{
    Console.WriteLine("You pressed Escape!");
}
```

#### 5. **Console.Clear() - Clear Screen**

```csharp
Console.Clear();
```

**What it does**:
- Clears all text from console
- Moves cursor to top-left corner

**Example**:
```csharp
Console.WriteLine("Line 1");
Console.WriteLine("Line 2");
Console.WriteLine("Line 3");
Console.Clear();  // Everything disappears
Console.WriteLine("New start!");
```

### Console Properties:

#### 1. **Console.Title - Set Window Title**

```csharp
Console.Title = "My Application";
```

**What it does**: Sets the console window title bar text

#### 2. **Console.ForegroundColor - Text Color**

```csharp
Console.ForegroundColor = ConsoleColor.Red;
Console.WriteLine("Red text!");
Console.ForegroundColor = ConsoleColor.White;  // Reset
```

**Available colors**:
- Black, White, Red, Green, Blue, Yellow, Cyan, Magenta, Gray, etc.

#### 3. **Console.BackgroundColor - Background Color**

```csharp
Console.BackgroundColor = ConsoleColor.Blue;
Console.WriteLine("Blue background!");
Console.BackgroundColor = ConsoleColor.Black;  // Reset
```

### Practical Example: Complete Input/Output Program

```csharp
using System;

namespace ConsoleDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Set title
            Console.Title = "Welcome Program";
            
            // Output - Get user's name
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("Enter your name: ");
            
            // Reset color and read input
            Console.ForegroundColor = ConsoleColor.White;
            string name = Console.ReadLine();
            
            // Output - Get user's age
            Console.Write("Enter your age: ");
            string ageInput = Console.ReadLine();
            int age = int.Parse(ageInput);  // Convert string to int
            
            // Display information
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("=== User Information ===");
            Console.WriteLine("Name: " + name);
            Console.WriteLine("Age: " + age);
            
            // Wait before closing
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("\nPress any key to exit...");
            Console.ReadKey();
        }
    }
}
```

**Sample Run**:
```
Enter your name: Raj
Enter your age: 20
=== User Information ===
Name: Raj
Age: 20

Press any key to exit...
```

---

## 11. Data Types, Variables, and Literals

### What is a Data Type?

A data type specifies **what kind of data** a variable can hold and **how much memory** it needs.

### What is a Variable?

A variable is a **named container** that stores a value. Think of it like a labeled box where you can put things.

### What is a Literal?

A literal is the **actual value** you assign to a variable. It's hard-coded and doesn't change.

### Example Showing All Three:

```csharp
int age = 20;
//  ^   ^    ^
//  |   |    |
//  |   |    Literal (actual value: 20)
//  |   Variable name (named container)
//  Data type (integer, 4 bytes)
```

---

### Primitive Data Types in C#

#### **Integer Types** (Whole Numbers)

| Type | Size | Range | Usage |
|------|------|-------|-------|
| `byte` | 1 byte | 0 to 255 | Small counts |
| `short` | 2 bytes | -32,768 to 32,767 | Smaller integers |
| `int` | 4 bytes | -2.1B to 2.1B | Default for integers |
| `long` | 8 bytes | -9.2Q to 9.2Q | Very large numbers |

**Example**:
```csharp
byte studentCount = 50;           // 1 byte
short salary = 50000;             // 2 bytes
int population = 1000000000;      // 4 bytes (most common)
long distance = 9223372036854775807;  // 8 bytes
```

#### **Floating-Point Types** (Decimal Numbers)

| Type | Size | Precision | Usage |
|------|------|-----------|-------|
| `float` | 4 bytes | ~7 digits | Single precision |
| `double` | 8 bytes | ~15 digits | Default for decimals |
| `decimal` | 16 bytes | ~28 digits | Financial calculations |

**Example**:
```csharp
float height = 5.9f;              // Note: 'f' suffix for float
double price = 99.99;             // Default decimal type
decimal salary = 50000.50m;       // 'm' suffix for decimal
```

**When to use each**:
- `float` - Graphics, games (precision not critical)
- `double` - Most calculations (balance of precision and speed)
- `decimal` - Money, financial apps (highest precision)

#### **Boolean Type**

```csharp
bool isStudent = true;
bool hasPassed = false;

if (isStudent)
{
    Console.WriteLine("You are a student");
}
```

#### **Character Type**

```csharp
char grade = 'A';           // Single character in single quotes
char symbol = '*';
char digit = '5';

Console.WriteLine(grade);   // Output: A
```

#### **String Type**

```csharp
string name = "Raj Kumar";  // Multiple characters in double quotes
string message = "Hello, World!";
string empty = "";          // Empty string
```

**String operations**:
```csharp
string firstName = "Raj";
string lastName = "Kumar";
string fullName = firstName + " " + lastName;  // Concatenation
Console.WriteLine(fullName);  // Output: Raj Kumar
```

### Declaring and Initializing Variables

#### **Declaration Only** (will be 0 by default)

```csharp
int age;
age = 20;  // Initialization later
```

#### **Declaration and Initialization** (Together)

```csharp
int age = 20;
string name = "Raj";
```

#### **Multiple Variables of Same Type**

```csharp
int x = 5, y = 10, z = 15;
```

### Implicit Type Inference (var keyword)

The `var` keyword lets the compiler determine the type:

```csharp
var age = 20;              // Compiler infers: int
var name = "Raj";          // Compiler infers: string
var price = 99.99;         // Compiler infers: double
```

**Rules**:
- Must be initialized when declared
- Type is determined at declaration and cannot change
- Useful for complex types (List, Dictionary)

### Literals - Practical Examples

```csharp
// Integer literals
int decimal_num = 100;          // Decimal literal
int hex_num = 0xFF;             // Hexadecimal literal
int binary_num = 0b1010;        // Binary literal

// Floating-point literals
float single = 3.14f;           // Float literal
double doubl = 3.14;            // Double literal
decimal money = 99.99m;         // Decimal literal

// String literals
string text = "Hello";          // String literal
string multiline = @"Line1
Line2
Line3";                         // Multiline string

// Character literal
char letter = 'A';              // Character literal

// Boolean literal
bool flag = true;               // Boolean literal (true/false)
```

### Naming Conventions

**Good variable names** follow these rules:

1. **camelCase for variables** (start lowercase, capitalize next words)
   ```csharp
   string firstName = "Raj";        // ✓ Good
   string first_name = "Raj";       // ✗ Not C# style
   string FirstName = "Raj";        // ✗ This is for classes
   ```

2. **Descriptive names** (explain what it stores)
   ```csharp
   int age = 20;                    // ✓ Clear
   int a = 20;                      // ✗ Not descriptive
   ```

3. **Avoid keywords** (reserved words in C#)
   ```csharp
   int class = 5;                   // ✗ ERROR: 'class' is keyword
   int myClass = 5;                 // ✓ OK
   ```

4. **Cannot start with number**
   ```csharp
   int 1age = 20;                   // ✗ ERROR
   int age1 = 20;                   // ✓ OK
   ```

### Real-World Example: Student Information

```csharp
using System;

namespace StudentInfo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declare variables
            string firstName = "Raj";
            string lastName = "Kumar";
            int age = 20;
            double gpa = 3.85;
            bool isActive = true;
            
            // Display information
            Console.WriteLine("Student Information");
            Console.WriteLine("==================");
            Console.WriteLine("Name: " + firstName + " " + lastName);
            Console.WriteLine("Age: " + age);
            Console.WriteLine("GPA: " + gpa);
            Console.WriteLine("Active: " + isActive);
        }
    }
}
```

**Output**:
```
Student Information
==================
Name: Raj Kumar
Age: 20
GPA: 3.85
Active: True
```

---

## 12. Type Casting

Type casting is **converting one data type to another**. Since C# is strongly typed, you sometimes need to convert between types.

### Two Types of Type Casting:

#### 1. **Implicit Casting** (Automatic)

The compiler automatically converts a smaller type to a larger type. **No data loss.**

```csharp
int smallNum = 100;
double largeNum = smallNum;  // Implicit conversion, int → double

Console.WriteLine(smallNum);   // Output: 100
Console.WriteLine(largeNum);   // Output: 100
```

**Why it works**: A double can hold any int value without losing information.

**Hierarchy** (smaller → larger):
```
byte → short → int → long → float → double
```

**Examples**:
```csharp
byte b = 10;
short s = b;           // ✓ OK: byte → short
int i = s;             // ✓ OK: short → int
long l = i;            // ✓ OK: int → long
double d = l;          // ✓ OK: long → double
```

#### 2. **Explicit Casting** (Manual)

You must explicitly tell the compiler to convert. **May cause data loss.**

**Syntax**:
```csharp
(targetType) value
```

```csharp
double largeNum = 99.99;
int smallNum = (int)largeNum;  // Explicit conversion, double → int

Console.WriteLine(largeNum);   // Output: 99.99
Console.WriteLine(smallNum);   // Output: 99 (decimals lost!)
```

**Why you need it**: Converting from double to int loses the decimal part.

**Examples of data loss**:
```csharp
double d = 123.45;
int i = (int)d;        // Output: 123 (loses .45)

long l = 300;
byte b = (byte)l;      // Output: 44 (overflows, wraps around)
```

**Hierarchy** (larger → smaller):
```
double → float → long → int → short → byte
```

### Casting Between Different Types:

#### **Int ↔ String**

**String to Int**:
```csharp
string strNumber = "123";
int number = int.Parse(strNumber);

Console.WriteLine(number + 50);  // Output: 173
```

**Error handling**:
```csharp
string invalidStr = "abc";
int number = int.Parse(invalidStr);  // ✗ ERROR: Cannot parse non-numeric string
```

**Safer method with TryParse**:
```csharp
string strNumber = "123";
if (int.TryParse(strNumber, out int number))
{
    Console.WriteLine("Success: " + number);
}
else
{
    Console.WriteLine("Conversion failed");
}
```

**Int to String**:
```csharp
int number = 123;
string str = number.ToString();

Console.WriteLine(str);  // Output: 123
Console.WriteLine(str.GetType());  // Output: System.String
```

#### **Double ↔ String**

**String to Double**:
```csharp
string strPrice = "99.99";
double price = double.Parse(strPrice);

Console.WriteLine(price);  // Output: 99.99
```

**Double to String**:
```csharp
double price = 99.99;
string str = price.ToString();

Console.WriteLine(str);  // Output: 99.99
```

#### **Boolean ↔ String**

**String to Boolean**:
```csharp
string strBool = "true";
bool flag = bool.Parse(strBool);

Console.WriteLine(flag);  // Output: True
```

**Boolean to String**:
```csharp
bool flag = true;
string str = flag.ToString();

Console.WriteLine(str);  // Output: True
```

### Using Convert Class (Safer Alternative)

```csharp
int number = Convert.ToInt32("123");      // String to int
string str = Convert.ToString(123);        // Int to string
double d = Convert.ToDouble("99.99");      // String to double
bool b = Convert.ToBoolean("true");        // String to bool
```

**Advantages**:
- Returns default value instead of error if conversion fails
- More consistent across types
- Better for nullable types

### Practical Example: User Input and Conversion

```csharp
using System;

namespace TypeConversionDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Get age from user
            Console.Write("Enter your age: ");
            string ageInput = Console.ReadLine();
            int age = int.Parse(ageInput);  // Convert string to int
            
            // Calculate birth year
            int currentYear = 2024;
            int birthYear = currentYear - age;
            
            // Get salary from user
            Console.Write("Enter your salary: ");
            string salaryInput = Console.ReadLine();
            double salary = double.Parse(salaryInput);  // Convert string to double
            
            // Display results
            Console.WriteLine("\n--- Information ---");
            Console.WriteLine("Age: " + age);
            Console.WriteLine("Birth Year: " + birthYear);
            Console.WriteLine("Salary: $" + salary);
        }
    }
}
```

**Sample Run**:
```
Enter your age: 20
Enter your salary: 50000.50

--- Information ---
Age: 20
Birth Year: 2004
Salary: $50000.5
```

---

## 13. Control Flow Statements

Control flow statements allow your program to make decisions and execute different code based on conditions.

### 1. **if Statement**

Execute code only if condition is true.

**Syntax**:
```csharp
if (condition)
{
    // Code executes if condition is true
}
```

**Example**:
```csharp
int age = 18;

if (age >= 18)
{
    Console.WriteLine("You are an adult");
}
```

**Output**:
```
You are an adult
```

### 2. **if-else Statement**

Execute one block if true, another if false.

**Syntax**:
```csharp
if (condition)
{
    // Code executes if true
}
else
{
    // Code executes if false
}
```

**Example**:
```csharp
int age = 15;

if (age >= 18)
{
    Console.WriteLine("You are an adult");
}
else
{
    Console.WriteLine("You are a minor");
}
```

**Output**:
```
You are a minor
```

### 3. **else-if Ladder**

Test multiple conditions in sequence.

**Syntax**:
```csharp
if (condition1)
{
    // Code if condition1 is true
}
else if (condition2)
{
    // Code if condition1 is false and condition2 is true
}
else if (condition3)
{
    // Code if condition1 and condition2 are false, but condition3 is true
}
else
{
    // Code if all conditions are false
}
```

**Example - Grade Calculator**:
```csharp
int marks = 85;
string grade;

if (marks >= 90)
{
    grade = "A";
}
else if (marks >= 80)
{
    grade = "B";
}
else if (marks >= 70)
{
    grade = "C";
}
else if (marks >= 60)
{
    grade = "D";
}
else
{
    grade = "F";
}

Console.WriteLine("Grade: " + grade);  // Output: Grade: B
```

### 4. **Nested if-else**

if-else statements inside other if-else statements.

**Example - Eligibility Check**:
```csharp
int age = 20;
bool hasLicense = true;

if (age >= 18)
{
    if (hasLicense)
    {
        Console.WriteLine("You can drive");
    }
    else
    {
        Console.WriteLine("Get a license first");
    }
}
else
{
    Console.WriteLine("You are too young to drive");
}
```

**Output**:
```
You can drive
```

### 5. **switch Statement**

Cleaner alternative to multiple else-if when checking one variable against many values.

**Syntax**:
```csharp
switch (expression)
{
    case value1:
        // Code if expression == value1
        break;
    case value2:
        // Code if expression == value2
        break;
    default:
        // Code if no case matches
        break;
}
```

**Example - Day of Week**:
```csharp
int day = 3;
string dayName;

switch (day)
{
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    case 3:
        dayName = "Wednesday";
        break;
    case 4:
        dayName = "Thursday";
        break;
    case 5:
        dayName = "Friday";
        break;
    default:
        dayName = "Invalid";
        break;
}

Console.WriteLine(dayName);  // Output: Wednesday
```

**Important Notes about switch**:
- `break;` exits the switch (essential!)
- Without `break`, code "falls through" to next case
- `default` is optional (like `else`)

---

### Loops - Repetition Structures

Loops execute code multiple times.

### 1. **for Loop**

Execute code a specific number of times.

**Syntax**:
```csharp
for (initialization; condition; increment/decrement)
{
    // Code to repeat
}
```

**Parts**:
1. **Initialization**: Create loop variable (runs once)
2. **Condition**: Check if should continue (checked each iteration)
3. **Increment/Decrement**: Update variable (runs after each iteration)

**Example - Print 1 to 5**:
```csharp
for (int i = 1; i <= 5; i++)
{
    Console.WriteLine(i);
}
```

**Output**:
```
1
2
3
4
5
```

**How it works**:
```
1. i = 1           (Initialization)
2. i <= 5? YES     (Condition check)
3. Print 1         (Execute body)
4. i++  → i = 2    (Increment)
5. i <= 5? YES     (Condition check)
6. Print 2         (Execute body)
... continues until i = 6, then i <= 5? NO (loop exits)
```

**Example - Sum of 1 to 10**:
```csharp
int sum = 0;
for (int i = 1; i <= 10; i++)
{
    sum = sum + i;
}
Console.WriteLine("Sum: " + sum);  // Output: Sum: 55
```

### 2. **while Loop**

Execute code while condition is true.

**Syntax**:
```csharp
while (condition)
{
    // Code to repeat
    // Must update something to eventually make condition false
}
```

**Example - Count Down**:
```csharp
int count = 5;

while (count > 0)
{
    Console.WriteLine(count);
    count--;  // IMPORTANT: Must update to exit loop
}

Console.WriteLine("Blast off!");
```

**Output**:
```
5
4
3
2
1
Blast off!
```

**Danger - Infinite Loop**:
```csharp
int count = 5;

while (count > 0)  // Condition always true!
{
    Console.WriteLine(count);
    // Never decrements count, so loop never exits
}
```

This will run forever! Always ensure the condition will eventually become false.

### 3. **do-while Loop**

Like while, but checks condition AFTER first execution.

**Syntax**:
```csharp
do
{
    // Code to repeat
} while (condition);
```

**Key difference**: Code runs at least once, even if condition is false.

**Example**:
```csharp
int count = 5;

do
{
    Console.WriteLine(count);
    count--;
} while (count > 0);
```

**Output**:
```
5
4
3
2
1
```

**Practical use - Menu with validation**:
```csharp
string input;

do
{
    Console.Write("Enter 'yes' or 'no': ");
    input = Console.ReadLine();
} while (input != "yes" && input != "no");

Console.WriteLine("Thank you for your input!");
```

---

## 14. Loop Controls

Loop control statements change the normal flow of loops.

### 1. **break Statement**

Exit loop immediately, regardless of condition.

**Syntax**:
```csharp
for (int i = 1; i <= 10; i++)
{
    if (i == 5)
    {
        break;  // Exit loop when i reaches 5
    }
    Console.WriteLine(i);
}
```

**Output**:
```
1
2
3
4
```

**Example - Search and Exit**:
```csharp
int[] numbers = { 10, 20, 30, 40, 50 };
int search = 30;
bool found = false;

for (int i = 0; i < numbers.Length; i++)
{
    if (numbers[i] == search)
    {
        found = true;
        break;  // Stop searching once found
    }
}

Console.WriteLine(found ? "Found" : "Not found");  // Output: Found
```

### 2. **continue Statement**

Skip current iteration and go to next iteration.

**Syntax**:
```csharp
for (int i = 1; i <= 10; i++)
{
    if (i == 5)
    {
        continue;  // Skip when i is 5
    }
    Console.WriteLine(i);
}
```

**Output**:
```
1
2
3
4
6
7
8
9
10
```

Notice 5 is skipped!

**Example - Print Only Even Numbers**:
```csharp
for (int i = 1; i <= 10; i++)
{
    if (i % 2 != 0)  // If odd
    {
        continue;  // Skip odd numbers
    }
    Console.WriteLine(i);
}
```

**Output**:
```
2
4
6
8
10
```

**Difference Between break and continue**:

| break | continue |
|-------|----------|
| Exits entire loop | Skips current iteration |
| Control goes outside loop | Control goes to next iteration |
| Used to terminate | Used to skip |

### 3. **goto Statement**

Jump to a labeled location in code (rarely used, generally avoided).

**Syntax**:
```csharp
goto label_name;

label_name:
    // Code here
```

**Example (NOT recommended practice)**:
```csharp
for (int i = 1; i <= 5; i++)
{
    if (i == 3)
    {
        goto END;  // Jump to END label
    }
    Console.WriteLine(i);
}

END:
    Console.WriteLine("Program ended");
```

**Output**:
```
1
2
Program ended
```

**Why avoid goto**:
- Makes code hard to follow
- Creates "spaghetti code"
- Better alternatives exist (break, return)
- Use only when absolutely necessary

---

## 15. Functions and Methods

Functions are reusable blocks of code that perform specific tasks.

### What is a Method?

A method is a function that belongs to a class. In C#, every function is a method.

**Terms**:
- **Method Definition**: Where you write the code
- **Method Call**: Where you use the code
- **Parameter**: Input to a method
- **Return Value**: Output from a method

### Method Syntax:

```csharp
[access_modifier] [return_type] MethodName([parameters])
{
    // Method body
    // optional return statement
}
```

### 1. **Method with No Parameters, No Return Value**

```csharp
static void Greet()
{
    Console.WriteLine("Hello, World!");
}
```

**Calling the method**:
```csharp
Greet();  // Output: Hello, World!
```

**Explanation**:
- `static` - Can be called without creating an object
- `void` - Returns nothing
- `()` - No parameters

### 2. **Method with Parameters, No Return Value**

```csharp
static void Greet(string name)
{
    Console.WriteLine("Hello, " + name + "!");
}
```

**Calling the method**:
```csharp
Greet("Raj");      // Output: Hello, Raj!
Greet("Priya");    // Output: Hello, Priya!
```

**Multiple parameters**:
```csharp
static void Add(int a, int b)
{
    int sum = a + b;
    Console.WriteLine("Sum: " + sum);
}
```

**Calling**:
```csharp
Add(5, 10);  // Output: Sum: 15
Add(20, 30); // Output: Sum: 50
```

### 3. **Method with No Parameters, With Return Value**

```csharp
static int GetCurrentYear()
{
    return 2024;
}
```

**Calling the method**:
```csharp
int year = GetCurrentYear();
Console.WriteLine("Year: " + year);  // Output: Year: 2024
```

### 4. **Method with Parameters and Return Value**

```csharp
static int Multiply(int a, int b)
{
    int product = a * b;
    return product;
}
```

**Calling the method**:
```csharp
int result = Multiply(5, 6);
Console.WriteLine("Product: " + result);  // Output: Product: 30
```

**Can simplify to**:
```csharp
static int Multiply(int a, int b)
{
    return a * b;
}
```

### 5. **Method Overloading**

Multiple methods with same name but different parameters.

```csharp
static void Print(int num)
{
    Console.WriteLine("Integer: " + num);
}

static void Print(string text)
{
    Console.WriteLine("String: " + text);
}

static void Print(double num)
{
    Console.WriteLine("Double: " + num);
}
```

**Calling**:
```csharp
Print(5);           // Calls Print(int)
Print("Hello");     // Calls Print(string)
Print(3.14);        // Calls Print(double)
```

**Output**:
```
Integer: 5
String: Hello
Double: 3.14
```

### Call by Value vs Call by Reference

#### **Call by Value** (Default in C#)

A **copy** of the value is passed. Changes inside the method don't affect original.

```csharp
static void Increment(int num)
{
    num++;
    Console.WriteLine("Inside method: " + num);
}

int x = 5;
Increment(x);
Console.WriteLine("Outside method: " + x);
```

**Output**:
```
Inside method: 6
Outside method: 5
```

The `x` remains 5 because a copy was modified.

#### **Call by Reference** (Using `ref` keyword)

The **reference** to the variable is passed. Changes affect the original.

```csharp
static void Increment(ref int num)
{
    num++;
    Console.WriteLine("Inside method: " + num);
}

int x = 5;
Increment(ref x);  // Must use 'ref' when calling too
Console.WriteLine("Outside method: " + x);
```

**Output**:
```
Inside method: 6
Outside method: 6
```

Now `x` becomes 6 because the actual variable was modified!

**When to use call by reference**:
- When method needs to modify the original variable
- Return multiple values from method
- Example: Parsing user input, sorting arrays

### Practical Example: Complete Program with Methods

```csharp
using System;

namespace MethodsDemo
{
    class Program
    {
        // Method 1: Get user's age
        static int GetAge()
        {
            Console.Write("Enter your age: ");
            return int.Parse(Console.ReadLine());
        }

        // Method 2: Check if adult
        static bool IsAdult(int age)
        {
            return age >= 18;
        }

        // Method 3: Calculate eligibility
        static void CheckEligibility(int age)
        {
            if (IsAdult(age))
            {
                Console.WriteLine("You are eligible to vote.");
            }
            else
            {
                int yearsLeft = 18 - age;
                Console.WriteLine($"You can vote in {yearsLeft} years.");
            }
        }

        static void Main(string[] args)
        {
            int age = GetAge();
            CheckEligibility(age);
        }
    }
}
```

**Sample Run**:
```
Enter your age: 20
You are eligible to vote.
```

**Another run**:
```
Enter your age: 15
You can vote in 3 years.
```

---

## Summary: Your C# Learning Path

You've learned:

1. ✅ **.NET Core** - Modern framework for C# development
2. ✅ **C# Language** - Syntax and basics
3. ✅ **Installation** - Visual Studio 2022 and .NET SDK setup
4. ✅ **First Program** - Console application creation
5. ✅ **Program Structure** - Namespaces, classes, methods
6. ✅ **Console I/O** - Read and write to console
7. ✅ **Data Types & Variables** - Storing and managing data
8. ✅ **Type Casting** - Converting between types
9. ✅ **Control Flow** - if-else, switch statements
10. ✅ **Loops** - for, while, do-while
11. ✅ **Loop Controls** - break, continue, goto
12. ✅ **Methods** - Writing reusable code

### Next Steps After This Guide:

1. **Practice Projects**:
   - Calculator application
   - Grade management system
   - Student information system
   - Temperature converter

2. **Learn Object-Oriented Programming (OOP)**:
   - Classes and Objects
   - Inheritance
   - Polymorphism
   - Encapsulation

3. **Advanced Topics**:
   - Collections (List, Dictionary, Array)
   - LINQ queries
   - File I/O
   - Exception handling
   - Async programming

4. **Web Development**:
   - ASP.NET Core
   - REST APIs
   - Entity Framework

### Recommendation:

- **Code daily** - Practice is essential
- **Create projects** - Real-world applications
- **Debug code** - Use Visual Studio debugger
- **Read others' code** - Learn from examples
- **Join communities** - Stack Overflow, GitHub

---

## Reference Links

### Official Resources:

1. **Microsoft Learn - C# Documentation**: https://learn.microsoft.com/en-us/dotnet/csharp/
2. **.NET Core Documentation**: https://learn.microsoft.com/en-us/dotnet/core/
3. **Visual Studio Download**: https://visualstudio.microsoft.com/downloads/
4. **.NET SDK Download**: https://dotnet.microsoft.com/download/dotnet

### Learning Resources:

5. **Microsoft C# Programming Guide**: https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/
6. **TutorialsTeacher C# Tutorials**: https://www.tutorialsteacher.com/csharp
7. **GeeksforGeeks C#**: https://www.geeksforgeeks.org/c-sharp/
8. **Programiz C# Tutorial**: https://www.programiz.com/csharp-programming

### Video Tutorials:

9. **freeCodeCamp C# Beginner Course**: https://www.youtube.com/watch?v=GZ9d9x7NNZM
10. **Traversy Media C# Crash Course**: https://www.youtube.com/watch?v=xLTJ7caHJAY
11. **Code with Mosh C# Tutorial**: https://www.youtube.com/watch?v=gfkTfcpWqAY

### Interactive Learning:

12. **LeetCode** (Practice coding problems): https://leetcode.com
13. **HackerRank C# Track**: https://www.hackerrank.com/domains/tutorials/10-days-of-csharp
14. **Codewars** (Coding challenges): https://www.codewars.com

### Tools and Communities:

15. **Stack Overflow** (Q&A for programming): https://stackoverflow.com
16. **GitHub** (Share and learn code): https://github.com
17. **Reddit r/csharp**: https://www.reddit.com/r/csharp/

### IDE and Tools:

18. **Visual Studio Community**: https://visualstudio.microsoft.com/vs/community/
19. **Visual Studio Code**: https://code.visualstudio.com/
20. **JetBrains Rider**: https://www.jetbrains.com/rider/

---

## Final Tips for Success

1. **Start with console applications** - Easier to focus on language fundamentals
2. **Type out examples** - Don't just copy-paste; understanding comes from typing
3. **Experiment constantly** - Change values, try different approaches
4. **Use meaningful variable names** - Makes code more readable
5. **Comment your code** - Explain what each section does
6. **Don't rush** - Take time to understand each concept
7. **Join communities** - Share code, ask questions, help others
8. **Build projects** - Theory + Practice = Mastery

**Congratulations on starting your C# journey! You now have a solid foundation to build amazing applications.**

---

**Document Version**: 1.0  
**Last Updated**: February 2026  
**Difficulty Level**: Beginner  
**Estimated Reading Time**: 3-4 hours  
**Hands-On Practice Time**: 5-10 hours
