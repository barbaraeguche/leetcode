-- name: 181. employees earning more than their managers
-- link: https://leetcode.com/problems/employees-earning-more-than-their-managers

-- solution --
select e1.name as Employee
from Employee e1
	cross join Employee e2 on e1.managerId = e2.id
where e1.salary > e2.salary