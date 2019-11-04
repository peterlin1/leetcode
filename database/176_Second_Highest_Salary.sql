/*
Write a SQL query to get the second highest salary from the Employee table.

Runtime: 696 ms, faster than 58.38% of Oracle online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Second Highest Salary.
*/

SELECT
    max(e.Salary) as SecondHighestSalary
FROM
    Employee e
WHERE
    Salary < (SELECT max(e.salary) FROM Employee e)