-- name: 1731. the number of employees which report to each employee
-- link: https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee

-- solution --
select
	e1.employee_id,
	e1.name,
	count(e2.employee_id) as reports_count,
	round(avg(e2.age)) as average_age
from Employees e1
	cross join Employees e2 on e1.employee_id = e2.reports_to
group by e1.employee_id
order by e1.employee_id