-- name: 185. department top three salaries
-- link: https://leetcode.com/problems/department-top-three-salaries

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
where ranks < 4