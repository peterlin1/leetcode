--Write a SQL query for a report that provides the following information for each person in the Person table, regardless
--if there is an address for each of those people

FirstName, LastName, City, State
SELECT
    p.FirstName,
    p.LastName,
    a.City,
    a.State
FROM
    Person p
    left join Address a on p.PersonId = a.PersonId;