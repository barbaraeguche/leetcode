-- name: 1789. primary department for each employee
-- link: https://leetcode.com/problems/primary-department-for-each-employee

-- solution --
select employee_id, department_id
from Employee
where primary_flag = 'Y' or employee_id in (
	select employee_id
	from Employee
	group by employee_id
	having count(department_id) = 1
)