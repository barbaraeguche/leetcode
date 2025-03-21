-- name: 1978. employees whose manager left the company
-- link: https://leetcode.com/problems/employees-whose-manager-left-the-company

-- solution --
select employee_id
from Employees e1
where e1.salary < 30000 and e1.manager_id not in (
	select employee_id
	from Employees e2
)
order by employee_id