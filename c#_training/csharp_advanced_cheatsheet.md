# 🚀 Advanced C# Quick Reference Guide

## 1. Advanced Syntax & Features
```

| Feature | Syntax | Example |
| :-- | :-- | :-- |
| **Null-conditional** | `?.` | `customer?.Address?.City` |
| **Null-coalescing** | `??` | `string name = customer?.Name ?? "Unknown"` |
| **String Interpolation** | `$""` | `$"Hello {name}"` |
| **nameof** | `nameof(Property)` | `nameof(Person.Name)` |
| **Pattern Matching** | `is`, `switch` | `if (obj is string s)` |
| **Tuples** | `(int, string)` | `var result = (count: 5, message: "OK")` |
| **Records** | `record Person(string Name)` | Immutable by default |
| **Top-level Statements** | No `class Program` | Direct code in `.cs` file |

## 2. LINQ One-Liners

```
```csharp
// Filter
var adults = people.Where(p => p.Age >= 18);

// Select/Transform
var names = people.Select(p => p.Name);

// Sort
var sorted = people.OrderBy(p => p.Age);

// Group
var byCity = people.GroupBy(p => p.City);

// Aggregate
var avgAge = people.Average(p => p.Age);
var total = people.Sum(p => p.Salary);

// Join
var result = people.Join(orders, p => p.Id, o => o.PersonId, (p,o) => new {p.Name, o.Amount});

// Any/All
bool hasAdults = people.Any(p => p.Age >= 18);
bool allActive = people.All(p => p.IsActive);
```

```

## 3. OOP - Four Pillars Summary
```

| Principle | Keyword | Purpose |
| :-- | :-- | :-- |
| **Encapsulation** | `private`, Properties | Hide data, controlled access |
| **Inheritance** | `:` | `class Dog : Animal` |
| **Polymorphism** | `virtual`/`override` | Same method, different behavior |
| **Abstraction** | `abstract`, Interfaces | Hide implementation details |

**Access Modifiers:**

```
public  → Everywhere
private → Same class
protected → Class + derived
internal → Same assembly
```


## 4. Constructors \& Destructors

```
**Types of Constructors:**
```csharp
public Student() { }                           // Default
public Student(string name) { }                // Parameterized  
public Student(Student other) { }              // Copy
static Student() { }                          // Static (runs once)
private Student(string name) { }              // Factory pattern
```

**Constructor Chaining:**

```csharp
public Student() : this("Unknown", 0) { }     // Calls other constructor
```

**Destructor (Finalizer):**

```csharp
~Student() { /* cleanup */ }  // Called by GC, NOT guaranteed timing
```

```

## 5. Delegates & Events - Fast Reference
```

**Delegate Declaration:**

```csharp
public delegate void MyDelegate(string message);
```

**Event Declaration:**

```csharp
public event EventHandler<string> MyEvent;
```

**Lambda Usage:**

```csharp
button.Click += (sender, e) => Console.WriteLine("Clicked!");
```

**Async Event Handler:**

```csharp
public async Task HandleAsync(object sender, EventArgs e)
{
    await DoWorkAsync();
}
```

```

## 6. Async/Await Patterns
```

**Basic Pattern:**

```csharp
public async Task<int> GetDataAsync()
{
    await Task.Delay(1000);
    return 42;
}

// Calling
int result = await GetDataAsync();
```

**ConfigureAwait(false):**

```csharp
await GetDataAsync().ConfigureAwait(false);  // Don't capture context
```

**Common Patterns:**

```
- `Task.Run()` → CPU-bound work
- `HttpClient.GetStringAsync()` → I/O
- `ConfigureAwait(false)` → Library code
```

```

## 7. Exception Handling Best Practices
```

```csharp
try { /* code */ }
catch (ArgumentException ex) when (ex.ParamName == "id") { /* specific */ }
catch (Exception ex) 
{ 
    logger.LogError(ex, "Error occurred");
    throw;  // Re-throw
}
finally { /* cleanup */ }
```

```

## 8. Generics Quick Reference
```

**Generic Class:**

```csharp
public class Repository<T> where T : class, new()
{
    public List<T> Items { get; set; } = new();
    
    public T Create() => new T();
}
```

**Constraints:**

```
`where T : class` → Reference type
`where T : struct` → Value type  
`where T : new()` → Must have parameterless ctor
`where T : IEntity` → Must implement interface
```

```

## 9. Memory Management Checklist
```

✅ Use `using` for IDisposable
✅ `IDisposable` pattern for resources
✅ Unsubscribe events to avoid leaks
✅ `GC.Collect()` → Only for testing
✅ `WeakReference<T>` for cache
✅ Object pooling for frequent allocation

```

## 10. Common Patterns (One-Liners)
```

**Factory Pattern:**

```csharp
public static T Create<T>() where T : new() => new T();
```

**Singleton:**

```csharp
public class Singleton 
{ 
    private static readonly Lazy<Singleton> instance = new(() => new());
    public static Singleton Instance => instance.Value;
}
```

**Builder Pattern:**

```csharp
var car = new CarBuilder()
    .WithEngine("V8")
    .WithColor("Red")
    .Build();
```

```

## 11. Performance Tips
```

**StringBuilder** → Concat in loops
**String Interpolation** → Single strings
**ArrayPool<T>.Shared** → Frequent arrays
**Span<T>** → Stack-only memory
**ReadOnlySpan<char>** → String substrings
**List<T>.Capacity** → Pre-allocate

```

## 12. LINQ Performance (Avoid These)
```

❌ `ToList()` then `Where()`
✅ `Where().ToList()`

❌ Multiple `Count()` calls
✅ Cache `Any()` / `Count()`

❌ `Select()` then `ToList()` then access by index
✅ Use `ElementAt()` or arrays

```

---

# 📱 Copy-Paste Ready Code Snippets

## Complete Async Example
```csharp
public class DataService
{
    public async Task<List<User>> GetUsersAsync()
    {
        using HttpClient client = new();
        string json = await client.GetStringAsync("https://api.example.com/users");
        return JsonSerializer.Deserialize<List<User>>(json)!;
    }
}
```


## Event Pattern

```csharp
public class Publisher 
{
    public event EventHandler<DataEventArgs> OnDataReady;
    
    public void ProcessData()
    {
        var args = new DataEventArgs { Data = "Ready" };
        OnDataReady?.Invoke(this, args);
    }
}
```


## Generic Repository

```csharp
public interface IRepository<T> where T : class
{
    Task<T> GetAsync(int id);
    Task<List<T>> GetAllAsync();
    Task AddAsync(T entity);
}
