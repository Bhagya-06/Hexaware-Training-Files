# C# Code Examples - Ready to Run Programs

Complete, working C# programs demonstrating all the concepts you've learned.

---

## Example 1: Simple Hello World

```csharp
using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
            Console.WriteLine("Welcome to C# Programming!");
            Console.ReadKey();
        }
    }
}
```

**Output:**
```
Hello, World!
Welcome to C# Programming!
```

---

## Example 2: Variables and Data Types

```csharp
using System;

namespace DataTypesDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Integer types
            byte age = 25;
            short yearsSince = 2000;
            int population = 1000000;
            long distance = 999999999;

            // Floating point types
            float height = 5.9f;
            double weight = 75.5;
            decimal salary = 50000.50m;

            // Other types
            bool isStudent = true;
            char grade = 'A';
            string name = "Raj Kumar";

            // Display all values
            Console.WriteLine("=== Personal Information ===");
            Console.WriteLine($"Name: {name}");
            Console.WriteLine($"Age: {age}");
            Console.WriteLine($"Height: {height} feet");
            Console.WriteLine($"Weight: {weight} kg");
            Console.WriteLine($"Grade: {grade}");
            Console.WriteLine($"Salary: ${salary}");
            Console.WriteLine($"Is Student: {isStudent}");
            
            Console.ReadKey();
        }
    }
}
```

**Output:**
```
=== Personal Information ===
Name: Raj Kumar
Age: 25
Height: 5.9 feet
Weight: 75.5 kg
Grade: A
Salary: $50000.50
Is Student: True
```

---

## Example 3: User Input and String Concatenation

```csharp
using System;

namespace UserInput
{
    class Program
    {
        static void Main(string[] args)
        {
            // Get user input
            Console.WriteLine("=== Welcome to User Input Program ===\n");
            
            Console.Write("Enter your first name: ");
            string firstName = Console.ReadLine();
            
            Console.Write("Enter your last name: ");
            string lastName = Console.ReadLine();
            
            Console.Write("Enter your age: ");
            int age = int.Parse(Console.ReadLine());
            
            Console.Write("Enter your favorite subject: ");
            string subject = Console.ReadLine();

            // Process and display
            string fullName = firstName + " " + lastName;
            int nextYear = age + 1;

            Console.WriteLine("\n=== Your Information ===");
            Console.WriteLine($"Full Name: {fullName}");
            Console.WriteLine($"Current Age: {age}");
            Console.WriteLine($"Next Year Age: {nextYear}");
            Console.WriteLine($"Favorite Subject: {subject}");
            
            Console.ReadKey();
        }
    }
}
```

**Sample Run:**
```
=== Welcome to User Input Program ===

Enter your first name: Raj
Enter your last name: Kumar
Enter your age: 20
Enter your favorite subject: Computer Science

=== Your Information ===
Full Name: Raj Kumar
Current Age: 20
Next Year Age: 21
Favorite Subject: Computer Science
```

---

## Example 4: Simple Calculator with if-else

```csharp
using System;

namespace SimpleCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Simple Calculator ===\n");

            // Get two numbers
            Console.Write("Enter first number: ");
            int num1 = int.Parse(Console.ReadLine());
            
            Console.Write("Enter second number: ");
            int num2 = int.Parse(Console.ReadLine());
            
            // Show menu
            Console.WriteLine("\nSelect Operation:");
            Console.WriteLine("1. Add");
            Console.WriteLine("2. Subtract");
            Console.WriteLine("3. Multiply");
            Console.WriteLine("4. Divide");
            Console.Write("Enter your choice (1-4): ");
            int choice = int.Parse(Console.ReadLine());

            int result = 0;

            // Perform operation
            if (choice == 1)
            {
                result = num1 + num2;
                Console.WriteLine($"\n{num1} + {num2} = {result}");
            }
            else if (choice == 2)
            {
                result = num1 - num2;
                Console.WriteLine($"\n{num1} - {num2} = {result}");
            }
            else if (choice == 3)
            {
                result = num1 * num2;
                Console.WriteLine($"\n{num1} * {num2} = {result}");
            }
            else if (choice == 4)
            {
                if (num2 != 0)
                {
                    result = num1 / num2;
                    Console.WriteLine($"\n{num1} / {num2} = {result}");
                }
                else
                {
                    Console.WriteLine("\nError: Cannot divide by zero!");
                }
            }
            else
            {
                Console.WriteLine("\nInvalid choice!");
            }

            Console.ReadKey();
        }
    }
}
```

---

## Example 5: Grade Calculator with switch

```csharp
using System;

namespace GradeCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Grade Calculator ===\n");

            // Get marks
            Console.Write("Enter your marks (0-100): ");
            int marks = int.Parse(Console.ReadLine());

            string grade = "";
            string feedback = "";

            // Determine grade
            if (marks >= 90)
                grade = "A";
            else if (marks >= 80)
                grade = "B";
            else if (marks >= 70)
                grade = "C";
            else if (marks >= 60)
                grade = "D";
            else
                grade = "F";

            // Provide feedback using switch
            switch (grade)
            {
                case "A":
                    feedback = "Excellent! Outstanding performance!";
                    break;
                case "B":
                    feedback = "Good! Keep up the good work!";
                    break;
                case "C":
                    feedback = "Average. Need more effort!";
                    break;
                case "D":
                    feedback = "Poor. Study harder!";
                    break;
                case "F":
                    feedback = "Failed. Try again!";
                    break;
            }

            // Display result
            Console.WriteLine($"\n=== Results ===");
            Console.WriteLine($"Marks: {marks}/100");
            Console.WriteLine($"Grade: {grade}");
            Console.WriteLine($"Feedback: {feedback}");

            Console.ReadKey();
        }
    }
}
```

---

## Example 6: Loops - Multiplication Table

```csharp
using System;

namespace MultiplicationTable
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Multiplication Table Generator ===\n");

            // Get number from user
            Console.Write("Enter a number: ");
            int number = int.Parse(Console.ReadLine());
            
            Console.Write("Up to which number? (default 10): ");
            string input = Console.ReadLine();
            int upTo = string.IsNullOrEmpty(input) ? 10 : int.Parse(input);

            Console.WriteLine($"\n=== Multiplication Table of {number} ===");

            // Generate table using for loop
            for (int i = 1; i <= upTo; i++)
            {
                int product = number * i;
                Console.WriteLine($"{number} × {i} = {product}");
            }

            Console.ReadKey();
        }
    }
}
```

**Output Example (for number 5):**
```
=== Multiplication Table Generator ===

Enter a number: 5
Up to which number? (default 10): 10

=== Multiplication Table of 5 ===
5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
5 × 4 = 20
5 × 5 = 25
5 × 6 = 30
5 × 7 = 35
5 × 8 = 40
5 × 9 = 45
5 × 10 = 50
```

---

## Example 7: Sum of Numbers Using Loop

```csharp
using System;

namespace SumCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Sum Calculator ===\n");

            Console.Write("Enter how many numbers: ");
            int count = int.Parse(Console.ReadLine());

            int sum = 0;

            // Input numbers and calculate sum
            for (int i = 1; i <= count; i++)
            {
                Console.Write($"Enter number {i}: ");
                int number = int.Parse(Console.ReadLine());
                sum += number;  // Add to sum
            }

            // Calculate average
            double average = (double)sum / count;

            Console.WriteLine($"\n=== Results ===");
            Console.WriteLine($"Total Sum: {sum}");
            Console.WriteLine($"Average: {average:F2}");  // F2 = 2 decimal places

            Console.ReadKey();
        }
    }
}
```

---

## Example 8: Using Methods

```csharp
using System;

namespace MethodsDemo
{
    class Program
    {
        // Method to greet user
        static void Greet(string name)
        {
            Console.WriteLine($"Hello, {name}! Welcome to C#!");
        }

        // Method to check if adult
        static bool IsAdult(int age)
        {
            return age >= 18;
        }

        // Method to calculate area of rectangle
        static double CalculateArea(double length, double width)
        {
            return length * width;
        }

        // Method to calculate sum of two numbers
        static int Add(int a, int b)
        {
            return a + b;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("=== Methods Demo ===\n");

            // Call Greet method
            Greet("Raj");

            // Call IsAdult method
            Console.Write("\nEnter your age: ");
            int age = int.Parse(Console.ReadLine());
            if (IsAdult(age))
                Console.WriteLine("You are eligible to vote.");
            else
                Console.WriteLine("You are too young to vote.");

            // Call CalculateArea method
            Console.Write("\nEnter rectangle length: ");
            double length = double.Parse(Console.ReadLine());
            Console.Write("Enter rectangle width: ");
            double width = double.Parse(Console.ReadLine());
            double area = CalculateArea(length, width);
            Console.WriteLine($"Area: {area}");

            // Call Add method
            int result = Add(10, 20);
            Console.WriteLine($"\n10 + 20 = {result}");

            Console.ReadKey();
        }
    }
}
```

---

## Example 9: Type Casting

```csharp
using System;

namespace TypeCastingDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Type Casting Demo ===\n");

            // Implicit casting (automatic)
            Console.WriteLine("=== Implicit Casting ===");
            int intValue = 100;
            double doubleValue = intValue;  // int automatically converts to double
            Console.WriteLine($"int value: {intValue}");
            Console.WriteLine($"double value: {doubleValue}\n");

            // Explicit casting (manual)
            Console.WriteLine("=== Explicit Casting ===");
            double doubleNum = 99.99;
            int intNum = (int)doubleNum;  // Loses decimal part
            Console.WriteLine($"double: {doubleNum}");
            Console.WriteLine($"int (after casting): {intNum}\n");

            // String to int conversion
            Console.WriteLine("=== String to Int Conversion ===");
            string strNumber = "123";
            int convertedNum = int.Parse(strNumber);
            Console.WriteLine($"String: \"{strNumber}\"");
            Console.WriteLine($"After conversion: {convertedNum}");
            Console.WriteLine($"Double value: {convertedNum * 2}\n");

            // Int to string conversion
            Console.WriteLine("=== Int to String Conversion ===");
            int num = 456;
            string numString = num.ToString();
            Console.WriteLine($"int: {num}");
            Console.WriteLine($"string: \"{numString}\"");
            Console.WriteLine($"string with text: \"Value is {numString}\"\n");

            // Safe conversion using TryParse
            Console.WriteLine("=== Safe Conversion (TryParse) ===");
            string invalidInput = "abc";
            if (int.TryParse(invalidInput, out int result))
            {
                Console.WriteLine($"Conversion successful: {result}");
            }
            else
            {
                Console.WriteLine($"Failed to convert \"{invalidInput}\" to integer");
            }

            Console.ReadKey();
        }
    }
}
```

---

## Example 10: Number Guessing Game

```csharp
using System;

namespace GuessingGame
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Number Guessing Game ===\n");
            Console.WriteLine("I'm thinking of a number between 1 and 100.");
            Console.WriteLine("Can you guess it?\n");

            // Generate random number
            Random random = new Random();
            int secretNumber = random.Next(1, 101);  // 1 to 100
            
            int guess = 0;
            int attempts = 0;

            // Game loop
            while (guess != secretNumber)
            {
                Console.Write("Enter your guess: ");
                guess = int.Parse(Console.ReadLine());
                attempts++;

                if (guess < secretNumber)
                {
                    Console.WriteLine("Too low! Try a higher number.\n");
                }
                else if (guess > secretNumber)
                {
                    Console.WriteLine("Too high! Try a lower number.\n");
                }
                else
                {
                    Console.WriteLine($"\n🎉 Correct! The number was {secretNumber}!");
                    Console.WriteLine($"You guessed it in {attempts} attempts!");
                }
            }

            Console.ReadKey();
        }
    }
}
```

---

## Example 11: Call by Value vs Reference

```csharp
using System;

namespace CallByValueVsReference
{
    class Program
    {
        // Call by Value - changes don't affect original
        static void ModifyByValue(int num)
        {
            num = 100;
            Console.WriteLine($"Inside method (by value): {num}");
        }

        // Call by Reference - changes affect original
        static void ModifyByReference(ref int num)
        {
            num = 100;
            Console.WriteLine($"Inside method (by reference): {num}");
        }

        static void Main(string[] args)
        {
            Console.WriteLine("=== Call by Value vs Reference ===\n");

            // Call by Value
            Console.WriteLine("--- Call by Value ---");
            int value = 5;
            Console.WriteLine($"Before method: {value}");
            ModifyByValue(value);
            Console.WriteLine($"After method: {value}");  // Still 5

            Console.WriteLine("\n--- Call by Reference ---");
            int refValue = 5;
            Console.WriteLine($"Before method: {refValue}");
            ModifyByReference(ref refValue);
            Console.WriteLine($"After method: {refValue}");  // Now 100

            Console.ReadKey();
        }
    }
}
```

---

## Example 12: Student Information System

```csharp
using System;

namespace StudentManagement
{
    class Program
    {
        // Method to get student info
        static void GetStudentInfo(out string name, out int age, out double gpa)
        {
            Console.Write("Enter student name: ");
            name = Console.ReadLine();
            
            Console.Write("Enter age: ");
            age = int.Parse(Console.ReadLine());
            
            Console.Write("Enter GPA: ");
            gpa = double.Parse(Console.ReadLine());
        }

        // Method to check if eligible for honors
        static bool IsEligibleForHonors(double gpa)
        {
            return gpa >= 3.5;
        }

        // Method to determine category
        static string GetCategory(int age)
        {
            if (age < 18)
                return "Minor";
            else if (age < 25)
                return "Young Adult";
            else
                return "Adult";
        }

        static void Main(string[] args)
        {
            Console.WriteLine("=== Student Information System ===\n");

            // Get student information
            GetStudentInfo(out string name, out int age, out double gpa);

            // Process information
            bool isHonors = IsEligibleForHonors(gpa);
            string category = GetCategory(age);

            // Display information
            Console.WriteLine("\n=== Student Details ===");
            Console.WriteLine($"Name: {name}");
            Console.WriteLine($"Age: {age}");
            Console.WriteLine($"Category: {category}");
            Console.WriteLine($"GPA: {gpa}");
            Console.WriteLine($"Eligible for Honors: {(isHonors ? "Yes" : "No")}");

            Console.ReadKey();
        }
    }
}
```

---

## Example 13: Loop Control - Break and Continue

```csharp
using System;

namespace LoopControls
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Loop Control Statements ===\n");

            // Break example
            Console.WriteLine("--- Break Statement ---");
            Console.WriteLine("Numbers 1 to 10 (stops at 5):");
            for (int i = 1; i <= 10; i++)
            {
                if (i == 6)
                    break;  // Exit loop
                Console.Write(i + " ");
            }
            Console.WriteLine("\n");

            // Continue example
            Console.WriteLine("--- Continue Statement ---");
            Console.WriteLine("Numbers 1 to 10 (skips even):");
            for (int i = 1; i <= 10; i++)
            {
                if (i % 2 == 0)
                    continue;  // Skip even numbers
                Console.Write(i + " ");
            }
            Console.WriteLine("\n");

            // Nested loop with break
            Console.WriteLine("\n--- Nested Loop with Break ---");
            Console.WriteLine("Find 10 in nested loop:");
            bool found = false;
            for (int i = 1; i <= 3 && !found; i++)
            {
                for (int j = 1; j <= 5; j++)
                {
                    if (i * j == 10)
                    {
                        Console.WriteLine($"Found: {i} × {j} = 10");
                        found = true;
                        break;
                    }
                }
            }

            Console.ReadKey();
        }
    }
}
```

---

## How to Use These Examples

1. **Copy the code** into Visual Studio
2. **Create new project**: File → New → Console App
3. **Paste the code** into Program.cs
4. **Run the program**: Press F5 or Ctrl+F5
5. **Experiment**: Modify values and observe results
6. **Debug**: Use F10 to step through code

---

## Exercises Based on These Examples

1. **Modify Example 2**: Add more data types (char array, string methods)
2. **Extend Example 4**: Add more operations (modulo, power)
3. **Enhance Example 6**: Add option to generate table for multiple numbers
4. **Improve Example 10**: Add difficulty levels, hint system
5. **Combine Examples**: Create a program using multiple concepts

---

**Remember**: The best way to learn is by doing. Modify these examples, break them, fix them, and build upon them!
