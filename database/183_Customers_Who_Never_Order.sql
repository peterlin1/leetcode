/*
Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all
customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

Runtime: 1458 ms, faster than 27.30% of Oracle online submissions for Customers Who Never Order.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Customers Who Never Order.

*/

SELECT
    c.Name as Customers
FROM
    Customers c
    left join Orders o on c.Id = o.CustomerId
WHERE
    o.Id is Null;