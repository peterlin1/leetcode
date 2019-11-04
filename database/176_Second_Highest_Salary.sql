--Write a SQL query to get the second highest salary from the Employee table.

SELECT
    max(e.Salary) as SecondHighestSalary
FROM
    Employee e
WHERE
    Salary < (SELECT max(e.salary) FROM Employee e)