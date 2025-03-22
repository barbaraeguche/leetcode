-- name: 176. second highest salary
-- link: https://leetcode.com/problems/second-highest-salary

-- solution --
select ifnull(
	(select distinct salary
	from Employee
	order by salary desc
	limit 1 offset 1)
, null) as SecondHighestSalary