/*
Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its
smallest Id.
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Note:

Your output is the whole Person table after executing your sql. Use delete statement.

Runtime: 1195 ms, faster than 8.34% of MySQL online submissions for Delete Duplicate Emails.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.
*/

DELETE p
FROM
    Person p
    INNER JOIN Person p2 on p.email = p2.email
WHERE
    p.Id > p2.Id;