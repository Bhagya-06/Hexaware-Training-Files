# 1. Big Picture: Object-Oriented Programming (OOP)

OOP is a way of organizing code around **objects** instead of just functions.

The four main ideas (often called the “four pillars”) are:

- **Encapsulation** – Keep data and logic that work on that data together, and hide internal details.
- **Abstraction** – Show only what is necessary, hide unnecessary complexity.
- **Inheritance** – Reuse code by creating new classes from existing ones.
- **Polymorphism** – Use a single interface or method name to work differently for different types.[^1]

You’ll see these ideas repeated in almost every topic below.

***

# 2. Classes and Objects in C\#

- A **class** is a blueprint (design).
- An **object** is a real thing created from that blueprint at runtime.

```csharp
public class Person
{
    // Fields / Properties = data
    public string Name { get; set; }
    public int Age { get; set; }

    // Methods = behavior
    public void Introduce()
    {
        Console.WriteLine($"Hi, I am {Name}, {Age} years old.");
    }
}

class Program
{
    static void Main()
    {
        // Creating an object (instance)
        Person p = new Person();
        p.Name = "Raj";
        p.Age = 25;
        p.Introduce();
    }
}
```

Think: **Class = design**, **Object = actual thing in memory**.

***

# 3. Access Specifiers in C\#

Access specifiers (modifiers) control **who can see or use** a class member.

Most commonly used:

- `public` – Accessible from anywhere.
- `private` – Accessible only inside the same class.
- `protected` – Accessible in the same class and in derived classes.
- `internal` – Accessible within the same assembly (project).
- `protected internal` – Protected OR internal (same assembly OR derived).
- `private protected` – Same assembly AND derived only.

Example:

```csharp
public class Example
{
    public int PublicValue;          // Anywhere
    private int PrivateValue;        // Only in Example
    protected int ProtectedValue;    // Example + subclasses
    internal int InternalValue;      // Same assembly
}
```

Access modifiers are the primary tool for **encapsulation**: hide what should not be touched by external code.

***

# 4. Static vs Non-Static Members in C\#

- **Non-static (instance) members**: belong to each individual object.
- **Static members**: belong to the **class itself**, shared by all objects.

```csharp
public class Counter
{
    public static int TotalCount;    // shared
    public int InstanceCount;        // per-object

    public Counter()
    {
        TotalCount++;
        InstanceCount++;
    }
}

class Program
{
    static void Main()
    {
        Counter c1 = new Counter();
        Counter c2 = new Counter();

        Console.WriteLine(Counter.TotalCount); // 2 (shared)
        Console.WriteLine(c1.InstanceCount);   // 1
        Console.WriteLine(c2.InstanceCount);   // 1
    }
}
```

Use static when:

- Value is **global** to the type (like config, counters, caches).
- You want **utility methods** that do not depend on an instance.

***

# 5. Constructors in C\#

A **constructor** is a special method that runs when your object is created. It sets up initial state.

Key rules:

- Same name as the class.
- No return type.
- Runs automatically on `new`.


## 5.1 Why Constructors?

Without constructors:

```csharp
Person p = new Person();
p.Name = "Raj";
p.Age = 25;
```

With constructors:

```csharp
public class Person
{
    public string Name { get; }
    public int Age { get; }

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}

// Usage
Person p = new Person("Raj", 25);
```

This guarantees that a `Person` is **always** created with valid data.

## 5.2 Types of Constructors

### Default (parameterless)

```csharp
public class Person
{
    public string Name;

    public Person()        // default
    {
        Name = "Unknown";
    }
}
```

If you don’t define **any** constructor, C\# creates an empty default one for you.

### Parameterized

```csharp
public class Person
{
    public string Name;
    public int Age;

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}
```


### Copy constructor (custom pattern)

```csharp
public class Person
{
    public string Name;
    public int Age;

    public Person(Person other)
    {
        Name = other.Name;
        Age = other.Age;
    }
}
```


### Constructor overloading

Multiple constructors with different parameter lists:

```csharp
public class Person
{
    public string Name;
    public int Age;

    public Person() : this("Unknown", 0) { }

    public Person(string name) : this(name, 0) { }

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}
```

This is called **constructor chaining** (`: this(...)`).

## 5.3 Static vs Non-Static Constructors

### Instance constructor

Runs each time you create a new object.

```csharp
public class Example
{
    public Example()
    {
        Console.WriteLine("Instance constructor");
    }
}
```


### Static constructor

- Declared with `static`.
- No access modifier, no parameters.
- Runs **once per type**, before the first use (first `new` or first static member access).[^1]

```csharp
public class Example
{
    public static int Value;

    static Example()
    {
        Console.WriteLine("Static constructor");
        Value = 10;
    }
}
```

Use static constructors to:

- Initialize static fields.
- Perform one-time setup.


## 5.4 Private Constructors

A **private constructor** cannot be called from outside the class. Common uses:

1. **Factory pattern**: force creation through static methods.
2. **Singleton**: only one instance allowed.
```csharp
public class Logger
{
    private Logger() { }

    public static Logger Create()
    {
        return new Logger();
    }
}
```

Or singleton:

```csharp
public sealed class Singleton
{
    private static readonly Singleton _instance = new Singleton();
    public static Singleton Instance => _instance;

    private Singleton() { }
}
```


***

# 6. Destructors, Garbage Collection, Finalize and Dispose

## 6.1 Garbage Collection in .NET

.NET uses a **Garbage Collector (GC)** to automatically free memory for objects that are no longer used.[^2]

- You create objects on the **heap** with `new`.
- When no references to an object remain, it becomes **eligible for collection**.
- The GC runs occasionally, finds unused objects, and frees their memory.

You don’t usually free memory manually. But you **must** properly free **unmanaged resources** (files, DB connections, sockets, etc.), which is where `Dispose` and `Finalize` come in.

## 6.2 Destructors (`~ClassName`)

A **destructor** is C\# syntax that the compiler turns into an override of `Finalize()`.

```csharp
public class MyClass
{
    ~MyClass()
    {
        // cleanup code (rarely used)
    }
}
```

Key points:

- You cannot control **when** it runs (GC decides).
- It is **slow** and should be used only when absolutely necessary.
- It’s mainly for cleaning unmanaged resources as a last resort.[^3]

In modern C\#, destructors are rarely written. Preferred way is `IDisposable`.

## 6.3 `Finalize` vs `Dispose` vs Destructor

- **Finalize**:
    - Method called by GC before an object is destroyed (if class has finalizer).[^4]
    - Non-deterministic (you don’t know when it runs).
- **Destructor (`~ClassName`)**:
    - C\# syntax that compiles to `Finalize` override.
- **Dispose (IDisposable)**:
    - Called **manually** or via `using`.
    - Deterministic: it runs exactly when your code calls it.
    - Used to free unmanaged resources.


### Classic `IDisposable` pattern

```csharp
public class ResourceHolder : IDisposable
{
    private bool _disposed;

    // Public Dispose
    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this); // GC skips finalizer for this object[cite:126]
    }

    protected virtual void Dispose(bool disposing)
    {
        if (_disposed) return;

        if (disposing)
        {
            // free managed resources here
        }

        // free unmanaged resources here

        _disposed = true;
    }

    ~ResourceHolder()
    {
        // finalizer calls Dispose with false
        Dispose(false);
    }
}
```


### Using block (syntactic sugar)

```csharp
using (var file = new FileStream("data.txt", FileMode.Open))
{
    // use file
} // `Dispose()` automatically called here
```

**Rule of thumb:**

- If your class holds **unmanaged resources**, implement `IDisposable` and optionally a finalizer for safety.
- If it only uses managed memory (normal objects), you usually don’t need `Dispose` or destructors at all.

***

# 7. Encapsulation, Abstraction, Inheritance, Generalization/Specialization

## 7.1 Encapsulation

Putting data + behavior together and hiding internal details.

```csharp
public class BankAccount
{
    private decimal _balance;  // hidden field

    public void Deposit(decimal amount)
    {
        if (amount <= 0) throw new ArgumentException();
        _balance += amount;
    }

    public decimal GetBalance()
    {
        return _balance;
    }
}
```

You prevent external code from directly touching `_balance`.

## 7.2 Abstraction

Focusing on **what** an object does, not **how** it does it.

```csharp
public abstract class Shape
{
    public abstract double GetArea(); // abstraction
}
```

Clients just call `GetArea()`; they don’t care how the shape calculates it.

## 7.3 Inheritance and Types of Inheritance

Inheritance lets you create a class from another class.

```csharp
public class Animal
{
    public void Eat() { }
}

public class Dog : Animal
{
    public void Bark() { }
}
```

- `Dog` **inherits** from `Animal`.
- This is **single inheritance** (one base class per class).

C\# supports:

- **Single inheritance** for classes: `class B : A`
- **Multiple inheritance for interfaces**: `interface IChild : IOne, ITwo`

Types you’ll hear in theory (UML / general OOP):

- Single inheritance, multilevel, hierarchical, multiple, hybrid.
- In C\#, **class multiple inheritance is not allowed**, but interfaces can be multiple.


## 7.4 Is-A vs Has-A

- **Is-A (inheritance)**: `Dog is an Animal`.
    - Use `:` for inheritance.
- **Has-A (composition/aggregation)**: `Car has an Engine`.

```csharp
public class Engine { }

public class Car    // Car has an Engine
{
    private Engine _engine = new Engine();
}
```

Prefer **Has-A (composition)** over Is-A if the relationship is not truly “is a special kind of”.

## 7.5 Generalization and Specialization

- **Generalization**: Going from specific to more general.
    - Example: `Car`, `Bike` → generalize to `Vehicle`.
- **Specialization**: Going from general to more specific.
    - Example: `Vehicle` → specialize to `Car`, `Truck`.

In C\#:

```csharp
public class Vehicle  // generalized class
{
    public int Wheels { get; set; }
}

public class Car : Vehicle // specialized version of Vehicle
{
    public bool HasSunroof { get; set; }
}
```


***

# 8. Abstract Classes and Interfaces

## 8.1 Abstract Class

- Cannot be instantiated.
- Can have **implemented methods** and **abstract methods**.
- Represents a **base concept** with partial implementation.

```csharp
public abstract class Animal
{
    public void Eat()          // normal method
    {
        Console.WriteLine("Eating");
    }

    public abstract void MakeSound(); // must be implemented by derived classes
}

public class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Woof");
    }
}
```

Use abstract classes when:

- You want to share code (common implementation) + enforce a contract.


## 8.2 Interface

- Pure **contract**: what members a class must have.
- No implementation (until default interface methods in newer C\#, but conceptually: no state, no fields).

```csharp
public interface ILogger
{
    void Log(string message);
}

public class ConsoleLogger : ILogger
{
    public void Log(string message)
    {
        Console.WriteLine(message);
    }
}
```

Use interfaces when:

- You want to define capabilities.
- You need multiple types to follow the same contract.
- You need **multiple inheritance** of behavior (via interfaces).


### Multiple Inheritance via Interfaces

```csharp
public interface IPrinter
{
    void Print();
}

public interface IScanner
{
    void Scan();
}

public class MultiFunctionMachine : IPrinter, IScanner
{
    public void Print() { /* ... */ }
    public void Scan() { /* ... */ }
}
```

Class can implement many interfaces, but inherit from only one base class.

***

# 9. Polymorphism

Polymorphism = “many forms”.

In C\# you mainly see three kinds:

1. **Method overloading** (compile-time).
2. **Method overriding** (runtime).
3. **Operator overloading**.

## 9.1 Method Overloading

Same method name, different parameter list.

```csharp
public class Calculator
{
    public int Add(int a, int b) => a + b;
    public double Add(double a, double b) => a + b;
    public int Add(int a, int b, int c) => a + b + c;
}
```

The compiler decides **at compile time** which method to call based on argument types.

## 9.2 Method Overriding (runtime polymorphism)

Use `virtual` in base class and `override` in derived class.

```csharp
public class Animal
{
    public virtual void MakeSound()
    {
        Console.WriteLine("Some sound");
    }
}

public class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Woof");
    }
}

class Program
{
    static void Main()
    {
        Animal a = new Dog();  // reference type: Animal, object type: Dog
        a.MakeSound();         // Woof  (runtime decision)
    }
}
```

Key rules:

- Base class method must be `virtual`, `abstract`, or `override`.
- Derived class method must use `override`.
- Which method is called is decided **at runtime** based on the actual object type.


## 9.3 Operator Overloading

You can define how operators like `+`, `-`, `==` work for your class.

```csharp
public struct Point
{
    public int X;
    public int Y;

    public Point(int x, int y) { X = x; Y = y; }

    public static Point operator +(Point a, Point b)
        => new Point(a.X + b.X, a.Y + b.Y);
}

class Program
{
    static void Main()
    {
        Point p1 = new Point(1, 2);
        Point p2 = new Point(3, 4);
        Point p3 = p1 + p2;  // uses operator +
    }
}
```

Use operator overloading only when it makes code **more natural** and not confusing.

***

# 10. Method Hiding (`new`) vs Method Overriding – With Emphasis

This is one of the most confusing areas, so let’s slow down.

### 10.1 Overriding (correct polymorphism)

```csharp
public class Base
{
    public virtual void Show()
    {
        Console.WriteLine("Base.Show");
    }
}

public class Derived : Base
{
    public override void Show()
    {
        Console.WriteLine("Derived.Show");
    }
}

class Program
{
    static void Main()
    {
        Base b = new Base();
        Base dAsBase = new Derived();
        Derived d = new Derived();

        b.Show();         // Base.Show
        d.Show();         // Derived.Show
        dAsBase.Show();   // Derived.Show  <-- important
    }
}
```

Because `Show` is `virtual` and overridden, **the runtime chooses** the correct method based on the actual object type (`Derived`).

### 10.2 Hiding (using `new`)

```csharp
public class Base
{
    public void Show()
    {
        Console.WriteLine("Base.Show");
    }
}

public class Derived : Base
{
    public new void Show()  // hiding, not overriding
    {
        Console.WriteLine("Derived.Show");
    }
}

class Program
{
    static void Main()
    {
        Base b = new Base();
        Base dAsBase = new Derived();
        Derived d = new Derived();

        b.Show();         // Base.Show
        d.Show();         // Derived.Show
        dAsBase.Show();   // Base.Show  <-- surprise for many!
    }
}
```

Here:

- `Base.Show` is **not virtual**.
- `Derived.Show` with `new` defines a **different method** that only applies when the **reference type** is `Derived`.

**Important difference:**

- **Overriding**: Behavior depends on **object type** at runtime. (`virtual` / `override`)
- **Hiding**: Behavior depends on **reference type** at compile time. (`new`)


### 10.3 When to use what?

- Use **overriding** when you want proper polymorphism.
- Avoid `new` unless:
    - You intentionally want to change behavior for derived references only.
    - You’re forced (e.g., you cannot modify base class, but it defines a method you want to hide).

If the compiler warns “hides inherited member, use new keyword”, that means you’re doing hiding. Usually, you should reconsider and prefer `virtual` + `override` if you control the base.

***

# 11. Sealed Class and Sealed Methods

- `sealed class` – cannot be inherited.
- `sealed` method – cannot be overridden further.

```csharp
public sealed class FinalLogger
{
    // cannot derive from FinalLogger
}

public class Base
{
    public virtual void Show() { }
}

public class Derived : Base
{
    public sealed override void Show()
    {
        // override allowed here
    }
}

public class MoreDerived : Derived
{
    // public override void Show() { }  // ERROR: Show is sealed
}
```

Use `sealed` when:

- You want to **stop inheritance** for safety or design reasons.
- You want to allow one level of override but no more.

***

# 12. Extension Methods in C\#

Extension methods let you “add” methods to existing types **without** modifying their source.

Rules:

- Define in a `static` class.
- Method is `static`.
- First parameter has `this TypeName paramName`.

```csharp
public static class StringExtensions
{
    public static bool IsNullOrEmptyOrWhiteSpace(this string value)
    {
        return string.IsNullOrWhiteSpace(value);
    }
}

class Program
{
    static void Main()
    {
        string s = "  ";
        bool result = s.IsNullOrEmptyOrWhiteSpace(); // feels like instance method
    }
}
```

C\# just treats it as: `StringExtensions.IsNullOrEmptyOrWhiteSpace(s);`

Great for:

- Utility helpers for BCL types.
- Fluent APIs.
- Adding helpers to interfaces.

***

# 13. Partial Classes and Partial Methods

## 13.1 Partial Classes

You can split one class into multiple files using the `partial` keyword.

```csharp
// File1.cs
public partial class Person
{
    public string Name { get; set; }
}

// File2.cs
public partial class Person
{
    public int Age { get; set; }
}
```

The compiler combines them into a single class.

Common uses:

- Designer-generated code (WinForms, WPF).
- Large classes where you want logical separation.


## 13.2 Partial Methods

Declared with `partial`. They allow you to declare a method in one part and optionally implement it in another.

```csharp
public partial class Person
{
    partial void OnCreated();
    
    public Person()
    {
        OnCreated();
    }
}

// In another file
public partial class Person
{
    partial void OnCreated()
    {
        Console.WriteLine("Person created");
    }
}
```

If you **don’t** implement the partial method, the compiler **removes** the calls—no overhead.

***

# 14. Static Classes in C\#

A `static` class:

- Cannot be instantiated.
- Only contains `static` members.

```csharp
public static class MathHelper
{
    public static int Square(int x) => x * x;
}

class Program
{
    static void Main()
    {
        int result = MathHelper.Square(5);
    }
}
```

Use static classes for:

- Utility/helper functions.
- Grouping related static methods.

***

# 15. Object Initializers

Object initializers are syntactic sugar to set properties/fields during creation.

Without initializer:

```csharp
Person p = new Person();
p.Name = "Raj";
p.Age = 25;
```

With object initializer:

```csharp
Person p = new Person
{
    Name = "Raj",
    Age = 25
};
```

Works with collections too:

```csharp
var list = new List<Person>
{
    new Person { Name = "A", Age = 20 },
    new Person { Name = "B", Age = 25 }
};
```

Cleaner and more readable, especially when passing parameters to methods.

***

# 16. Covariance and Contravariance (Simple View)

These appear mainly with **interfaces** and **delegates** and help with inheritance hierarchies.[^5][^6]

Think:

- **Covariance** – you can use a **more derived type** where a base type is expected (output).
- **Contravariance** – you can use a **less derived type** where a more derived type is expected (input).


## 16.1 Covariance with interfaces (`out`)

```csharp
IEnumerable<string> strings = new List<string>();
IEnumerable<object> objects = strings; // OK because IEnumerable<out T> is covariant
```

`string` is more derived than `object`. Because `IEnumerable<out T>` is covariant in `T`, you can treat a sequence of `string` as a sequence of `object`s.[^7]

## 16.2 Contravariance with interfaces (`in`)

```csharp
IComparer<object> cmpObj = ...;
IComparer<string> cmpStr = cmpObj; // OK because IComparer<in T> is contravariant
```

Here, `cmpObj` can compare any `object`, so it can also be used where a comparer of `string` is expected.

## 16.3 Simple mental model

- `out T` (covariant) – use when the interface **returns** `T`.
- `in T` (contravariant) – use when the interface **consumes** `T`.

You usually **use** this more than you **declare** it yourself (built-in interfaces already use it).

***

# 17. Final Recap: How It All Fits Together

Here is a mental map tying everything:

- **Classes and Objects** – basic building blocks.
- **Access Specifiers** + **Encapsulation** – control visibility and protect data.
- **Static vs Instance** + **Static Classes** – decide whether data/behavior belongs to the class or each object.
- **Constructors** – how objects start life (initialization).
- **Destructors / GC / Dispose / Finalize** – how resources and memory are cleaned up.
- **Abstraction / Abstract Classes / Interfaces** – define contracts and behaviors without exposing how.
- **Inheritance / Generalization / Specialization / Is-A / Has-A** – organize types in hierarchies and composition.
- **Polymorphism (overloading, overriding, operator overloading)** – same name, different behaviors.
- **Method Hiding vs Overriding** – reference-based vs object-based behavior (very important difference).
- **Sealed** – where you stop extension.
- **Extension Methods** – “add” methods to existing types without inheritance.
- **Partial Classes/Methods** – split implementation across files.
- **Covariance / Contravariance** – work smoothly with collections and delegates in inheritance hierarchies.
- **Object Initializers** – cleaner syntax to construct and configure objects.
