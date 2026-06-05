\---------------------------- DAY 1 -----------------------------------



### **SQL SERVER**



DDL - Data definition language which allows us to create drop alter and truncate



DML - Data manipulation language which allows us to insert update delete



**PROJECT : QUITQ - Ecom**



Alias (as) - *select 2+3 'addition', 3-2 as 'subtraction'* --> can give names even without as like given above for addition.



**Clauses:**

1. where
2. top - *select top 3 id from mytable*
3. distinct - *select distinct name from mytable*
4. order by - *select \* from mytable order by name asc*
5. group by - *select count(name) from employees group by manager* (must be used with atleast one aggregate func)



**Aggregate Functions:**

1. Avg()
2. Count()
3. Min()
4. Max()
5. Sum()



**Mathematical Functions:**

1. sin(), cos(), tan(), cot(), asin(), acos(), atan()
2. pi(), power(), exp(), sqrt(), square(), log(), log10()



**Datetime Functions:**

1. GETDATE()
2. DATEADD()
3. DATENAME()
4. DATEDIFF()



**String functions:**

1. ascii()
2. len()
3. left(), right()
4. upper(), lower()
5. reverse()
6. trim(), ltrim(), rtrim()
7. replicate()



**MERGE COMMAND:**
*MERGE Employees AS T USING Employees\_new AS S ON T.EmpID = S.EmpID*



*WHEN MATCHED THEN*

*UPDATE SET T.Name = S.Name, T.Salary = S.Salary*



*WHEN NOT MATCHED BY TARGET THEN*

*INSERT (EmpID,Name,Salary) VALUES (S.EmpID,S.Name,S.Salary)*



*WHEN NOT MATCHED BY SOURCE THEN*

*DELETE*



\---------------------------- DAY 2 -----------------------------------



**JOINS:**

[JOINS DIAGRAM](https://www.reddit.com/r/programming/comments/1xlqeu/sql_joins_explained_xpost_rsql/)
Inner join - only data which matches in both tables

Outer join - all data in both tables with NULL for not matching rows

Left join - all data in left table and matched data in right table

Right join - all data in right table and matched data in left table

Self join - table matching with itself

Cross join - all possible combinations (cartesian product)

Equi join - uses only equality operator in join condition

Non Equi join - uses other relational operator in join condition



**SUBQUERIES:**

Using Where, in, not in , any, all, comparison operators



**STORED PROCEDURES:**

Set of commands combined together

* with parameters
* without parameters



TRIGGERS, INDEXES, FUNCTIONS (SYSTEM, UDFs)



\---------------------------- DAY 3 -----------------------------------



### **C#**



* **namespace** -> logical container used to organize and group related code elements, such as classes, structs, interfaces etc
* **class** --> blueprint for creating objects
* **Main()** function is the entry point of C# console
* ***using System;*** is important for basic i/o functions
* **print** --> *Console.Write()* or *Console.WriteLine()*
* **read input** --> *Console.ReadLine()*
* **operators** --> arithmetic, logical, comparison, assignment, ternary
* **conditional statements** --> if , if else, nested if, switch
* variables
* matrices
* arrays
* polymorphism
* inheritance
* diff types of methods
* loops



\---------------------------- DAY 4 -----------------------------------



* abstraction



\---------------------------- DAY 5 -----------------------------------



**Singleton Class**



public class Singleton

{

&#x20;   private static Singleton instance;

&#x20;   private Singleton()

&#x20;   {



&#x20;   }

&#x20;   public static Singleton Instance

&#x20;   {

&#x20;       get

&#x20;       {

&#x20;           if (instance == null)

&#x20;           {

&#x20;               instance = new Singleton();

&#x20;           }

&#x20;           return instance;

&#x20;       }

&#x20;   }

}

static void Main()

{    Singleton s1 = Singleton.Instance;

&#x20;   Singleton s2 = Singleton.Instance;



&#x20;   if (s1 != s2) Console.WriteLine("Not a singleton");

&#x20;   else Console.WriteLine("Singleton works");

}



\---------------------------- DAY 8 -----------------------------------



# **ASP .NET CORE MVC**



**Models**: Think of these as the "What." It’s the data and the rules for that data (like "a username must be 5 characters").

**Views**: These are the "Where." The actual HTML/CSS pages where the data lives.

**Controllers**: These are the "How." They take the user's click, grab the right info from the Model, and "hand" it to the View.

* Note: The Model is usually the definition of the data in your code, while the Database is where that data lives permanently. The Model acts as the bridge between the two.



**Razor Syntaxes (.cshtml)**

* Comments - *@\*...\*@*
* Inline razor syntax - *<h2> @DateTime.Now.ToShortDateString() </h2>*
* Multiline razor syntax -

&#x09;*@{*

&#x09;	*var date = DateTime.Now.ToShortDateString();*

&#x09;	*var message = "Hello World";*

&#x09;*}*

&#x09;*<h2> Today's date is @date </h2>*

&#x09;*<h3> @message </h3>*

