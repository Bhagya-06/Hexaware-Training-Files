CREATE DATABASE fsdtraining
use fsdtraining

/*DDL commands*/
CREATE TABLE mytable ( id int, name varchar(50))
ALTER TABLE mytable ALTER COLUMN id int NOT NULL
DROP TABLE mytable
TRUNCATE TABLE mytable

/*DML commands*/
INSERT INTO mytable (id, name) VALUES (1, 'John Doe'), (2, 'Jane Doe')
UPDATE mytable SET id = 2 WHERE name = 'John Doe'
DELETE FROM mytable WHERE id = 2 and name = 'John Doe'
SELECT * FROM mytable

/*ALIAS*/
SELECT 2+3 'addition', 3-2 AS 'subtraction'

/*KEYWORDS*/
SELECT TOP 3 id from mytable
SELECT DISTINCT name from mytable
SELECT * FROM mytable ORDER BY name ASC

/*FUNCTIONS*/
SELECT COUNT(id) AS 'Total Records', SUM(id) AS 'SUM OF IDs', MAX(id) AS 'MAX ID', MIN(id) AS 'MIN ID', AVG(id) AS 'AVG no of IDs' FROM mytable
SELECT sin(0.5), cos(0.5), tan(0.5), cot(0.5), asin(0.5), acos(0.5), atan(0.5)
SELECT pi(), EXP(1), LOG(10), LOG10(10), POWER(2, 3), SQRT(16)
SELECT datename(year, getdate()), dateadd(day,2, getdate()), datediff(day, '2024-01-01', getdate()), datepart(month, getdate()), getdate()

/*JOINS*/
CREATE TABLE emp (id int, name varchar(50), department_id int)
CREATE TABLE department (id int, name varchar(50))
INSERT INTO emp (id, name, department_id) VALUES (1, 'Alice', 1), (2, 'Bob', 2), (3, 'Charlie', 1), (4, 'David', 4)
INSERT INTO department (id, name) VALUES (1, 'HR'), (2, 'IT'), (3, 'Finance')

SELECT e.name, d.name from emp e, department d where e.department_id = d.id --> inner join without using JOIN keyword
SELECT e.name, d.name FROM emp e INNER JOIN department d ON e.department_id = d.id --> inner join using JOIN keyword
SELECT e.name, d.name FROM emp e LEFT JOIN department d ON e.department_id = d.id --> left outer join or left join
SELECT e.name, d.name FROM emp e RIGHT JOIN department d ON e.department_id = d.id --> right outer join or right join
SELECT e.name, d.name FROM emp e FULL OUTER JOIN department d ON e.department_id = d.id --> full outer join
SELECT e1.name AS EmployeeName, e2.name AS ManagerName FROM emp e1 LEFT JOIN emp e2 ON e1.department_id = e2.department_id -- self join
SELECT e.name, d.name FROM emp e CROSS JOIN department d --> cross join
SELECT e.name, d.name FROM emp e JOIN department d ON e.department_id = d.id --> equi join (uses equality operator in the join condition)
SELECT e.name, d.name FROM emp e JOIN department d ON e.department_id > d.id --> non-equi join (uses other comparison operators in the join condition)

/*SUBQUERIES*/
SELECT name FROM emp WHERE department_id = (SELECT id FROM department WHERE name = 'HR') --> subquery in WHERE clause
SELECT name FROM emp WHERE department_id IN (SELECT id FROM department WHERE name IN ('HR')) --> subquery with IN operator
SELECT name FROM emp WHERE department_id NOT IN (SELECT id FROM department WHERE name IN ('HR')) --> subquery with NOT IN operator
SELECT name FROM emp WHERE department_id > (SELECT AVG(id) FROM department) --> subquery with comparison operator
SELECT name FROM emp WHERE department_id = (SELECT TOP 1 id FROM department) --> subquery with TOP clause
SELECT name FROM emp WHERE department_id = ANY (SELECT id FROM department WHERE name = 'HR') --> subquery with ANY operator
SELECT name FROM emp WHERE department_id = ALL (SELECT id FROM department WHERE name = 'HR') --> subquery with ALL operator

/*STORED PROCEDURES*/

--> with parameters
CREATE PROCEDURE GetEmployeesByDepartment @DepartmentName varchar(50) 
AS BEGIN 
SELECT e.name FROM emp e JOIN department d ON e.department_id = d.id WHERE d.name = @DepartmentName 
END

--> without parameters
CREATE PROCEDURE GetAllEmployees
AS BEGIN
SELECT name FROM emp 
END

EXEC GetAllEmployees