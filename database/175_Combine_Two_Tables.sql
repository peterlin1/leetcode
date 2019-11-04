/*
Write a SQL query for a report that provides the following information for each person in the Person table, regardless
if there is an address for each of those people

Runtime: 580 ms, faster than 94.41% of Oracle online submissions for Combine Two Tables.
Memory Usage: 0B, less than 100.00% of Oracle online submissions for Combine Two Tables.
*/

SELECT
    p.FirstName,
    p.LastName,
    a.City,
    a.State
FROM
    Person p
    left join Address a on p.PersonId = a.PersonId;