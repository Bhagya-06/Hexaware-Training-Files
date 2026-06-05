## 1. Introduction to File Handling in C\#

**File handling** is about working with files and folders: creating, reading, writing, copying, moving, and deleting them.

In .NET, most file operations live in the **`System.IO`** namespace.[^1]

Key ideas:

- A **file** is data stored on disk.
- A **directory** (folder) contains files and other directories.
- A **stream** is a sequence of bytes flowing between your program and a data source (file, memory, network, etc).[^2]

Common `System.IO` classes:[^3][^2]

- `File`, `FileInfo` – work with files.
- `Directory`, `DirectoryInfo` – work with folders.
- `FileStream` – low-level read/write bytes.
- `StreamReader`, `StreamWriter` – read/write text.
- `BinaryReader`, `BinaryWriter` – read/write binary data.
- `StringReader`, `StringWriter` – treat strings as streams.

Almost always, you should:

- Use a **`using` block** to automatically close and dispose streams.
- Wrap file operations in **try/catch** to handle errors (file not found, no permission, etc).[^3]

***

## 2. FileStream Class (Low-Level Byte Access)

`FileStream` is the basic class for reading and writing bytes to files. Other readers/writers (like `StreamReader`) usually sit on top of a `FileStream`.[^4][^5]

### Opening a FileStream

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "data.bin";

        // Open or create a file for read/write
        using FileStream fs = new FileStream(
            path,
            FileMode.OpenOrCreate,
            FileAccess.ReadWrite,
            FileShare.None);

        // Use fs.Read(...) and fs.Write(...)
    }
}
```

Key parameters:

- `FileMode` (what to do with the file):
    - `Create`, `CreateNew`, `Open`, `OpenOrCreate`, `Append`, `Truncate`.
- `FileAccess`:
    - `Read`, `Write`, `ReadWrite`.
- `FileShare`:
    - Whether other processes can read/write while this one is open.


### Reading and Writing with FileStream

```csharp
byte[] data = { 1, 2, 3, 4, 5 };
fs.Write(data, 0, data.Length);   // write bytes

fs.Position = 0;                  // go back to start

byte[] buffer = new byte[^5];
int bytesRead = fs.Read(buffer, 0, buffer.Length);
```

Use `FileStream` when:

- You need byte-level control.
- You work with **binary formats** or large files in chunks.

***

## 3. StreamReader and StreamWriter (Text Files)

For **text files** (like `.txt`, `.csv`, `.log`), use `StreamReader` and `StreamWriter`. They wrap a stream (like `FileStream`) and handle **text encoding** and line-based reading/writing.[^5][^3]

### Writing Text: StreamWriter

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "notes.txt";

        // Overwrite file (FileMode.Create)
        using StreamWriter writer = new StreamWriter(path);

        writer.WriteLine("First line");
        writer.WriteLine("Second line");
        // writer.Flush();  // usually not needed, Dispose() will flush
    }
}
```

Appending to a file:

```csharp
using StreamWriter writer = new StreamWriter(path, append: true);
writer.WriteLine("New line at the end.");
```


### Reading Text: StreamReader

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "notes.txt";

        using StreamReader reader = new StreamReader(path);

        string? line;
        while ((line = reader.ReadLine()) != null)
        {
            Console.WriteLine(line);
        }
    }
}
```

You can also read the entire file in one go:

```csharp
string allText = File.ReadAllText("notes.txt");  // shortcut for small files
```

Use `StreamReader`/`StreamWriter` when:

- Working with **human-readable text**.
- Reading/writing **line by line**.

***

## 4. BinaryReader and BinaryWriter (Binary Files)

`BinaryReader` and `BinaryWriter` work with **primitive types** in **binary format** (int, double, bool, string, etc.).[^2][^3]

### Writing Binary Data

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "numbers.bin";

        using FileStream fs = new FileStream(path, FileMode.Create, FileAccess.Write);
        using BinaryWriter writer = new BinaryWriter(fs);

        writer.Write(42);            // int
        writer.Write(3.14);          // double
        writer.Write(true);          // bool
        writer.Write("Hello");       // string
    }
}
```


### Reading Binary Data

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string path = "numbers.bin";

        using FileStream fs = new FileStream(path, FileMode.Open, FileAccess.Read);
        using BinaryReader reader = new BinaryReader(fs);

        int i = reader.ReadInt32();
        double d = reader.ReadDouble();
        bool b = reader.ReadBoolean();
        string s = reader.ReadString();

        Console.WriteLine($"{i}, {d}, {b}, {s}");
    }
}
```

Important:

- You must **read in the same order and type** as you wrote, or you’ll get corrupt data or exceptions.

Use binary readers/writers for:

- Custom binary formats.
- More compact and faster storage than text.

***

## 5. File and Directory Operations (File, FileInfo, Directory, DirectoryInfo)

You can manage files and folders either using **static** helper classes (`File`, `Directory`) or **object-oriented** classes (`FileInfo`, `DirectoryInfo`).[^3][^2]

### File and FileInfo

#### Basic operations with `File` (static):

```csharp
string path = "data.txt";

bool exists = File.Exists(path);
File.WriteAllText(path, "Hello");        // create/overwrite
string content = File.ReadAllText(path); // read all
File.Copy(path, "data_copy.txt", overwrite: true);
File.Delete(path);
```


#### Using `FileInfo` (instance):

```csharp
using System.IO;

FileInfo fi = new FileInfo("data_copy.txt");

Console.WriteLine(fi.Name);
Console.WriteLine(fi.Length);
Console.WriteLine(fi.CreationTime);

fi.Delete();
```

`FileInfo` is nicer when you need to work with the **same file** several times (metadata + operations).

### Directory and DirectoryInfo

#### Using `Directory` (static):

```csharp
string dir = "Logs";

if (!Directory.Exists(dir))
    Directory.CreateDirectory(dir);

string[] files = Directory.GetFiles(dir, "*.txt");
string[] subDirs = Directory.GetDirectories(dir);
```


#### Using `DirectoryInfo`:

```csharp
DirectoryInfo di = new DirectoryInfo("Logs");

foreach (FileInfo file in di.GetFiles("*.txt"))
{
    Console.WriteLine($"{file.Name} - {file.Length} bytes");
}
```

Use `File/Directory` when you need **quick, one-off operations**.
Use `FileInfo/DirectoryInfo` when you want **rich object info and repeated access**.

***

## 6. StringReader and StringWriter

Sometimes you want to work with a **string** as if it were a file (a stream). `StringReader` and `StringWriter` let you do that.[^6][^7]

### StringWriter – write into a string

```csharp
using System;
using System.IO;
using System.Text;

class Program
{
    static void Main()
    {
        StringBuilder sb = new StringBuilder();

        using StringWriter writer = new StringWriter(sb);
        writer.WriteLine("Line 1");
        writer.WriteLine("Line 2");

        string result = sb.ToString();
        Console.WriteLine(result);
    }
}
```


### StringReader – read from a string

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        string text = "Line 1\nLine 2\nLine 3";

        using StringReader reader = new StringReader(text);
        string? line;
        while ((line = reader.ReadLine()) != null)
        {
            Console.WriteLine(line);
        }
    }
}
```

Use these when:

- You reuse code that expects a `TextReader`/`TextWriter`.
- You want to test code that works with streams using in-memory strings.

***

## 7. Export and Import Excel Data in C\#

.NET doesn’t have a super-friendly built-in Excel API; you usually use a **third-party library**. Popular ones include:

- **ClosedXML**
- **EPPlus**
- **Open XML SDK**

For learning and simple apps, **ClosedXML** is very handy.[^8][^9]

> Install via NuGet: `Install-Package ClosedXML`

### 7.1 Export a List to Excel (ClosedXML)

```csharp
using System;
using System.Collections.Generic;
using ClosedXML.Excel;

public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
}

class Program
{
    static void Main()
    {
        var people = new List<Person>
        {
            new Person { Name = "Raj", Age = 25 },
            new Person { Name = "Priya", Age = 30 }
        };

        using var wb = new XLWorkbook();
        var ws = wb.Worksheets.Add("People");

        // Header
        ws.Cell("A1").Value = "Name";
        ws.Cell("B1").Value = "Age";

        // Data
        int row = 2;
        foreach (var p in people)
        {
            ws.Cell(row, 1).Value = p.Name;
            ws.Cell(row, 2).Value = p.Age;
            row++;
        }

        wb.SaveAs("people.xlsx");
    }
}
```


### 7.2 Import Data from Excel (ClosedXML)

```csharp
using System;
using System.Collections.Generic;
using ClosedXML.Excel;

class Program
{
    static void Main()
    {
        var people = new List<Person>();

        using var wb = new XLWorkbook("people.xlsx");
        var ws = wb.Worksheet("People");

        // Assuming header in first row
        foreach (var row in ws.RowsUsed().Skip(1))
        {
            var person = new Person
            {
                Name = row.Cell(1).GetString(),
                Age = row.Cell(2).GetValue<int>()
            };
            people.Add(person);
        }

        // Check loaded data
        foreach (var p in people)
            Console.WriteLine($"{p.Name} - {p.Age}");
    }
}
```

For **huge Excel files**, reading row by row, as shown, is better than trying to load everything into big in-memory structures.

***

## 8. Working with JSON Files

JSON is a very common format for configuration and data exchange. In modern .NET, use `System.Text.Json` (built-in).[^10][^11]

### 8.1 Model Class

```csharp
public class Product
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public decimal Price { get; set; }
}
```


### 8.2 Write JSON to File

```csharp
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        var products = new List<Product>
        {
            new Product { Id = 1, Name = "Laptop", Price = 800 },
            new Product { Id = 2, Name = "Phone", Price = 500 }
        };

        string path = "products.json";

        var options = new JsonSerializerOptions { WriteIndented = true };
        string json = JsonSerializer.Serialize(products, options);

        await File.WriteAllTextAsync(path, json);
    }
}
```


### 8.3 Read JSON from File

```csharp
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        string path = "products.json";
        string json = await File.ReadAllTextAsync(path);

        List<Product>? products =
            JsonSerializer.Deserialize<List<Product>>(json);

        if (products != null)
        {
            foreach (var p in products)
                Console.WriteLine($"{p.Id}: {p.Name} - {p.Price}");
        }
    }
}
```

For large JSON files, prefer:

- `FileStream` + `JsonSerializer.DeserializeAsync` to **stream** instead of `ReadAllText`.
- Or JSON readers for incremental parsing.

***

## 9. Working with XML Files (XDocument)

For XML, the modern, easy API is **LINQ to XML**, using `XDocument`, `XElement`, etc. from `System.Xml.Linq`.[^12][^13]

### 9.1 Create and Save XML

```csharp
using System;
using System.Xml.Linq;

class Program
{
    static void Main()
    {
        XDocument doc = new XDocument(
            new XElement("Products",
                new XElement("Product",
                    new XElement("Id", 1),
                    new XElement("Name", "Laptop"),
                    new XElement("Price", 800)
                ),
                new XElement("Product",
                    new XElement("Id", 2),
                    new XElement("Name", "Phone"),
                    new XElement("Price", 500)
                )
            )
        );

        doc.Save("products.xml");
    }
}
```


### 9.2 Load and Read XML

```csharp
using System;
using System.Linq;
using System.Xml.Linq;

class Program
{
    static void Main()
    {
        XDocument doc = XDocument.Load("products.xml");

        var products = doc.Root!.Elements("Product")
            .Select(x => new
            {
                Id = (int)x.Element("Id")!,
                Name = (string?)x.Element("Name"),
                Price = (decimal)x.Element("Price")!
            });

        foreach (var p in products)
            Console.WriteLine($"{p.Id}: {p.Name} - {p.Price}");
    }
}
```

You can also modify, add, or remove elements, then call `doc.Save("products.xml")` again.

***

## 10. MemoryMappedFiles

**Memory-mapped files** let you map a file (or part of it) directly into memory. You can then treat it like a big array of bytes. This can be useful for:

- Very large files.
- Random access.
- Sharing data between processes.[^14][^15]

Namespace: `System.IO.MemoryMappedFiles`.

### Simple MemoryMappedFile Example

```csharp
using System;
using System.IO;
using System.IO.MemoryMappedFiles;
using System.Text;

class Program
{
    static void Main()
    {
        string path = "mmf_example.bin";

        // Create or open file
        using var fs = new FileStream(path, FileMode.OpenOrCreate, FileAccess.ReadWrite);

        // Ensure size
        if (fs.Length < 1024)
            fs.SetLength(1024);

        // Create memory-mapped file over it
        using var mmf = MemoryMappedFile.CreateFromFile(
            fs, null, fs.Length, MemoryMappedFileAccess.ReadWrite, HandleInheritability.None, false);

        // Create a view accessor (a window into the file)
        using var accessor = mmf.CreateViewAccessor();

        // Write a string at position 0
        string text = "Hello MMF";
        byte[] bytes = Encoding.UTF8.GetBytes(text);
        accessor.WriteArray(0, bytes, 0, bytes.Length);

        // Read back
        byte[] buffer = new byte[bytes.Length];
        accessor.ReadArray(0, buffer, 0, buffer.Length);
        string readText = Encoding.UTF8.GetString(buffer);

        Console.WriteLine(readText);
    }
}
```

Notes:

- You can create multiple views to work on different regions of a huge file.
- For many scenarios, **plain `FileStream` is enough and often simpler/faster**; memory-mapped files add overhead and complexity and should be used only when there is a clear need.[^16][^17]

***

## 11. Handling Large Files Efficiently

When files are large (hundreds of MB or GB), the main rule is: **do not load everything into memory at once**.

### 11.1 Stream Instead of ReadAll

Bad for large files:

```csharp
string all = File.ReadAllText("huge.txt");  // may exhaust memory
```

Better:

```csharp
using StreamReader reader = new StreamReader("huge.txt");
string? line;
while ((line = reader.ReadLine()) != null)
{
    // process one line at a time
}
```

Or use `File.ReadLines` which is already streaming:

```csharp
foreach (string line in File.ReadLines("huge.txt"))
{
    // process each line
}
```


### 11.2 Use Buffers for Binary Data

```csharp
byte[] buffer = new byte[^8192]; // 8 KB buffer
int bytesRead;

using FileStream fs = new FileStream("big.bin", FileMode.Open, FileAccess.Read);
while ((bytesRead = fs.Read(buffer, 0, buffer.Length)) > 0)
{
    // process buffer[0..bytesRead-1]
}
```


### 11.3 Use Async I/O for Responsiveness

```csharp
using FileStream fs = new FileStream(
    "big.bin",
    FileMode.Open,
    FileAccess.Read,
    FileShare.Read,
    bufferSize: 8192,
    useAsync: true);

byte[] buffer = new byte[^8192];
int bytesRead;
while ((bytesRead = await fs.ReadAsync(buffer, 0, buffer.Length)) > 0)
{
    // process chunk
}
```

Async I/O is especially useful in **GUI** and **web** apps to avoid blocking threads.

### 11.4 Dispose Resources Quickly

Large file operations can lock files and hold system resources. Always:

- Use `using` or `await using`.
- Dispose Excel workbooks, JSON/XML streams, etc.

```csharp
using (var reader = new StreamReader("huge.txt"))
{
    // ...
}
```


### 11.5 When to Consider MemoryMappedFile

Consider `MemoryMappedFile` if:

- You need **random access** to many parts of a very large file.
- Multiple processes must share the same data.
- You’re doing advanced scenarios and are comfortable with low-level details.[^15][^14]

For most CRUD or ETL tasks, **simple streaming with `FileStream` + `StreamReader`/`BinaryReader` is enough** and easier to reason about.[^16]

### 11.6 Large Excel / JSON / XML

- For **Excel**, read row by row (as in the ClosedXML example), don’t convert entire sheet to huge lists if not needed.
- For **JSON**, consider `JsonSerializer.DeserializeAsync` over a `FileStream` instead of `ReadAllText`.
- For **XML**, use `XmlReader` for streaming when files are very large, instead of loading entire `XDocument` into memory.

***

## 12. Summary – When to Use What

- **File \& Directory / FileInfo \& DirectoryInfo**
    - Creating, copying, moving, deleting files and folders.
    - Getting metadata (size, creation time, etc.).[^2][^3]
- **FileStream**
    - Low-level byte access, binary formats, custom protocols.
- **StreamReader / StreamWriter**
    - Text files, logs, CSV, reading/writing lines.
- **BinaryReader / BinaryWriter**
    - Efficient binary formats, primitive types in compact form.
- **StringReader / StringWriter**
    - Work with strings as streams (good for testing or in-memory transformations).[^7][^6]
- **Excel (ClosedXML / EPPlus / OpenXML)**
    - Export and import structured tabular data.
- **JSON (System.Text.Json)**
    - Modern configuration, APIs, lightweight data storage.[^11][^10]
- **XML (XDocument / LINQ to XML)**
    - Hierarchical data, interoperable config, and documents.[^13][^12]
- **MemoryMappedFile**
    - Advanced scenarios for very large files and inter-process sharing.
- **Large files (any format)**
    - Always **stream** in chunks or lines.
    - Use async I/O for responsiveness.
    - Dispose everything properly.
