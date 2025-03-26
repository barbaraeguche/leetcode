-- name: 1965. employees with missing information
-- link: https://leetcode.com/problems/employees-with-missing-information

-- solution --
select employee_id from Employees
where employee_id not in ( select employee_id from Salaries )
union
select employee_id from Salaries
where employee_id not in ( select employee_id from Employees )
order by employee_id