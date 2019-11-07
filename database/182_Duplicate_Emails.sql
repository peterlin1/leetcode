/*
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.

Runtime: 925 ms, faster than 55.93% of Oracle online submissions for Duplicate Emails.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Duplicate Emails.

*/

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1