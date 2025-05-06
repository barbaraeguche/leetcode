-- name: 184. department highest salary
-- link: https://leetcode.com/problems/department-highest-salary

-- solution --
select Department, Employee, Salary
from (
	select
		d.name as Department,
		e.name as Employee,
		salary as Salary,
		dense_rank() over(partition by d.name order by salary desc) as ranks
	from Department d
		join Employee e on d.id = e.departmentId
) sub
where ranks = 1