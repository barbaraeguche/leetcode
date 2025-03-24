-- name: 570. managers with at least 5 direct reports
-- link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports

-- solution --
select name
from Employee
where id in (
	select managerId
	from Employee
	group by managerId
	having count(*) >= 5
)