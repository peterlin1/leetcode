/*
There is a table courses with columns: student and class

Please list out all classes which have more than or equal to 5 students.

For example, the table:

+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
Should output:

+---------+
| class   |
+---------+
| Math    |
+---------+


Note:
The students should not be counted duplicate in each course.

Runtime: 519 ms, faster than 93.31% of Oracle online submissions for Classes More Than 5 Students.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Classes More Than 5 Students.

*/

SELECT
    class
FROM
    courses
GROUP BY
    courses.class
HAVING
    COUNT(DISTINCT courses.student) > 4