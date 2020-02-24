/*
Write a SQL query to get the nth highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

Runtime: 966 ms, faster than 64.78% of Oracle online submissions for Nth Highest Salary.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Nth Highest Salary.

*/

CREATE FUNCTION getNthHighestSalary(N IN NUMBER)
RETURN NUMBER
IS
    result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    SELECT Salary into result
    FROM (
      SELECT distinct Salary,
             dense_rank() over (order by Salary desc) as row_num
      FROM Employee
    )
    WHERE row_num = N;
    RETURN result;
END;