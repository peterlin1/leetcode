/*
Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous
(yesterday's) dates.

+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
For example, return the following Ids for the above Weather table:

+----+
| Id |
+----+
|  2 |
|  4 |
+----+

Runtime: 919 ms, faster than 64.13% of Oracle online submissions for Rising Temperature.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Rising Temperature.

*/

SELECT
    w.Id
FROM
    Weather w
    inner join Weather w2 on w.RecordDate = (w2.RecordDate + 1)
WHERE
    w.Temperature > w2.Temperature