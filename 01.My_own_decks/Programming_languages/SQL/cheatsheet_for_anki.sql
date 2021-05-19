SQL has three types of statements that developers use:
- Data definition language (DDL) statements, which are used to create and modify
database schemas
- Data manipulation language (DML) statements, which are used to insert, update,
delete, and query data
- Data query language (DQL) statements, which is a single statement: SELECT

A Single-Line Comment
-- one line comment

Multi-Line Comments
/*
Multi-Line
Comments
*/

-- establish an active SSH session on your server
mysql -u root -p my_password

-- create a new test user for practice
CREATE USER ‘username’@’localhost’ 
IDENTIFIED BY ‘password’;

-- delete a user
DROP USER ‘someuser’@’localhost’;

-- set up a new database
CREATE DATABASE db_name

-- view all db
SHOW databases;

-- get rid of a db
DROP DATABASE dbName

-- Essential MySQL Commands
CREATE a New DB
DELETE a MySQL DB
SELECT — choose specific data from your DB
UPDATE — update data in your DB
DELETE — deletes data from your DB
INSERT INTO — inserts new data into a DB
CREATE DATABASE — generate a new DB
ALTER DATABASE — modify an existing DB
CREATE TABLE — create a new table in a DB
ALTER TABLE — change the selected table
DROP TABLE — delete a table
CREATE INDEX — create an index
(search key for all the info stored)
DROP INDEX — delete an index


-- create a new table
CREATE TABLE [IF NOT EXISTS] table_name (
    column_list
    );

CREATE TABLE my_table (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100),
    genre CHAR(20),
    rating TEXT,

    FOREIGN KEY(this_table_field) REFERENCES other_table(field)
    -- Must map to an other table.field!
    );




-- see the columns of your table
DESCRIBE table_name;

-- review the information of the column in your table.
DESCRIBE table_name column_name;

-- get rid of a table
DROP TABLE table_name;

-- add a new column
ALTER TABLE table_name 
ADD [COLUMN] column_name;

-- delete / drop a column
ALTER TABLE table_name 
DROP [COLUMN] column_name;


-- insert a new row
INSERT INTO table_name (field1, field2, ...) 
VALUES (value1, value2, ...)

-- insert new rows
INSERT INTO table_name
  ( Column1, Column2, Column3 )
VALUES
  ('string1', 123, value1),
  ('string2', 456, value2);


-- retrieve all rows
SELECT * FROM table_name;
-- avoid in production

-- select specific columns
SELECT column_name1, column_name2 
FROM table_name;

---------------------
SELECT * FROM movies 
WHERE budget=’1’;

SELECT * FROM movies 
WHERE year=’2020’ AND rating=’9’;

-- delete specific rows with a condition
DELETE FROM table_name 
WHERE field=’value’;

-- update one or more columns
UPDATE table_name
SET column1 = value1,
SET column2 = value2;

-- update specific rows based on a clause
UPDATE table_name
SET column1 = value1,
WHERE other_columns=’val’


-- alter an existing column
ALTER TABLE table_name 
MODIFY COLUMN column_name INT(3)

-- sort entries in a column
SELECT * FROM table_name 
ORDER BY column_name ASC;

SELECT * FROM table_name 
ORDER BY column_name DESC;

-- search for a specific pattern
SELECT * FROM table_name 
WHERE column_name LIKE ‘beginn%’;

SELECT * FROM table_name 
WHERE column_name LIKE ‘%endd’;

-- exclude certain items from search
SELECT * FROM table_name 
WHERE column_name NOT LIKE ‘pattern%’;

-- select a range
SELECT * FROM table_name 
WHERE column_name BETWEEN 8 AND 10;

-- concatenate two columns & alias
SELECT CONCAT(first_name, ‘ ‘, last_name) 
AS ‘Name’, dept FROM users;


-- Data Types can change a little bit between MySQL, SQL server...
-- https://www.w3schools.com/sql/sql_datatypes.asp

-- List the most common data types
CHAR
VARCHAR
TEXT
BLOB
BIT
BOOLEAN
INTEGER
FLOAT
DATE
DATETIME
TIMESTAMP


CHAR(size)
A FIXED length string (can contain letters, numbers, and special characters).
The size parameter specifies the column length in characters - can be from 0 to 255.

VARCHAR(size)
A VARIABLE length string (can contain letters, numbers, and special characters).
The size parameter specifies the maximum column length in characters - can be from 0 to 65535

TEXT(size)
Holds a string with a maximum length of 65,535 bytes

BLOB(size)
For BLOBs (Binary Large OBjects). Holds up to 65,535 bytes of data

BIT(size)
A bit-value type. The number of bits per value is specified in size. The size parameter can hold a value from 1 to 64. The default value for size is 1.

BOOL or BOOLEAN
Zero is considered as false, nonzero values are considered as true.

INT(size) or INTEGER(size)
A medium integer.
Signed range is from -2147483648 to 2147483647.
Unsigned range is from 0 to 4294967295.
The size parameter specifies the maximum display width (which is 255)

FLOAT(size)
A floating point number.
The total number of digits is specified in size.

DATE
Format: YYYY-MM-DD.

DATETIME(fsp)
Format: YYYY-MM-DD hh:mm:ss.

TIMESTAMP(fsp)
The number of seconds since the Unix epoch ('1970-01-01 00:00:00' UTC).
Format: YYYY-MM-DD hh:mm:ss.

-- What are indexes
Indexes are the core element of your database navigation.
Use them to map the different types of data in your database, so that you don’t need to parse all the records to find a match.

A database index is a data structure that improves the speed of data retrieval operations on a database table at the cost of additional writes and storage space to maintain the index data structure. Indexes are used to quickly locate data without having to search every row in a database table every time a database table is accessed. Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access of ordered records.

An index is a copy of selected columns of data, from a table, that is designed to enable very efficient search. An index normally includes a "key" or direct link to the original row of data from which it was copied, to allow the complete row to be retrieved efficiently. Some databases extend the power of indexing by letting developers create indexes on column values that have been transformed by functions or expressions. For example, an index could be created on upper(last_name), which would only store the upper-case versions of the last_name field in the index. Another option sometimes supported is the use of partial indices, where index entries are created only for those records that satisfy some conditional expression. A further aspect of flexibility is to permit indexing on user-defined functions, as well as expressions formed from an assortment of built-in functions.

-- Best practices regarding indexes
You have to update an index every time you are creating, changing or deleting a record in the table.
Thus, it’s best to create indexes only when you need to and for frequently searched columns.

-- Create an index
CREATE INDEX index_name 
ON table_name (column1, column2, ...);

-- Create a unique index
CREATE UNIQUE INDEX index_name 
ON table_name(index_column_1,index_column_2,...);

-- Delete an index
DROP INDEX index_name;

-- What is a view
A view is a virtual representation of an actual table that you can assemble up to your liking
It contains one or more columns / rows from the real tables
It’s a good way to visualize and review data coming from different tables within a single screen.
or before adding the actual one to your database.

-- Create a new view
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

-- Update a view
CREATE OR REPLACE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

-- Rename a view
RENAME TABLE view_name TO new_view_name;

-- Show all view
SHOW FULL TABLES
WHERE table_type = ‘VIEW’;

-- Delete a view
DROP VIEW [IF EXISTS] view_name;

-- Delete several views
DROP VIEW [IF EXISTS] view1, view2, ...;

-- Logical operators
AND - OR - NOT - BETWEEN - LIKE - IN - SUM
IS NULL - ALL - EXISTS

ALL — compare a value or expression to all other values in a list.
ANY — compare a value or expression to any value in your list according to the specified condition.
EXISTS — test if a certain record exists.

-- What are a aggregate functions
Aggregate functions allow you to run a calculation on a set of values and return a single scalar value.
to find the needed data faster and organize it better using GROUP BY and HAVING clauses

-- List all aggregate functions
AVG returns the average of a list
COUNT returns the number of elements of a list
SUM returns the total of a list
MAX returns the maximum value in a list
MIN returns the minimum value in a list


-- Arithmetic, Bitwise, Comparison, and Compound Operators


-- Query distinct rows from a table
SELECT DISTINCT column_name 
FROM table_name
WHERE condition;

-- Filter groups
SELECT c1, aggregate(c2)
FROM t
GROUP BY c1
HAVING condition;

-- Inner join t1 and t2
SELECT c1, c2
FROM t1
INNER JOIN t2 ON condition;

-- Left join t1 and t1
SELECT c1, c2
FROM t1
LEFT JOIN t2 ON condition;

-- Right join t1 and t2
SELECT c1, c2
FROM t1
RIGHT JOIN t2 ON condition;

-- Perform full outer join
SELECT c1, c2
FROM t1
FULL OUTER JOIN t2 ON condition;

-- Produce a Cartesian product of rows in tables
SELECT c1, c2
FROM t1
CROSS JOIN t2;

-- Join t1 to itself using INNER JOIN clause
SELECT c1, c2
FROM t1 A
INNER JOIN t2 BON condition;

-- Combine rows from two queries
SELECT c1, c2 FROM t1
UNION [ALL]
SELECT c1, c2 FROM t2;

-- Return the intersection of two queries
SELECT c1, c2 FROM t1
INTERSECT
SELECT c1, c2 FROM t2;

-- Subtract a result set from another result set
SELECT c1, c2 FROM t1
MINUS
SELECT c1, c2 FROM t2;

-- Query rows in a list
SELECT c1, c2 FROM t
WHERE c1 [NOT] IN value_list;

-- Query rows between two values
SELECT c1, c2 FROM t
WHERE c1 BETWEEN low AND high;

-- Check if values in a table is NULL or not
SELECT c1, c2 FROM t
WHERE c1 IS [NOT] NULL;

-- specify the max nb of rows the result must have
SELECT column_name(s)
FROM table_name
LIMIT number;

-- round a column values
SELECT ROUND(column_name, integer)
FROM table_name;


-- multiple conditions
SELECT * FROM table_name
WHERE column1 != 'expression'
    AND column3 LIKE '%xzy%'
LIMIT 10;

-- correct keyword order without group
1. SELECT
2. FROM
3. WHERE
4. ORDER BY
5. LIMIT


-- What alias are used for ?
You can rename columns, tables, subqueries, anything.


-- SQL alias
SELECT column1, COUNT(column2) AS number_of_values 
FROM table_name
GROUP BY column1;


-- correct keyword order with group / join
1. SELECT
2. FROM
3. JOIN (ON)
4. WHERE
5. GROUP BY
6. HAVING
7. ORDER BY
8. LIMIT

-- What are subqueries used for ?
To use the result of one query as an input value of another query.


-- A subquery may occur in ?
- A SELECT clause
- A FROM clause
- A WHERE clause

-- Example of a subquery
SELECT COUNT(*) FROM (
    SELECT column1, COUNT(column2) AS inner_nb_of_val
    FROM table_name
    GROUP BY column1
    ) AS inner_query
WHERE inner_number_of_values > 100;

-- https://dataschool.com/how-to-teach-people-sql/sql-join-types-explained-visually/

INNER joins
keep rows with keys that exist in the left AND right datasets

OUTER joins
keep rows with keys in either the left OR right datasets

LEFT OUTER joins
keep rows with keys in the left dataset

RIGHT OUTER joins
keep rows with keys in the right dataset

LEFT SEMI joins
keep the rows in the left, and only the left, dataset where the key appears in the right dataset

LEFT ANTI joins
keep the rows in the left, and only the left, dataset where they do not appear in the right dataset

CROSS (or CARTESIAN) joins
match every row in the left dataset with every row in the right dataset
Beware of the nb of rows !
