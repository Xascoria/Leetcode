/* Write your PL/SQL query statement below */

SELECT e.name AS Employee
FROM Employee e JOIN
Employee e2 ON e.managerId = e2.id
WHERE e.salary > e2.salary;