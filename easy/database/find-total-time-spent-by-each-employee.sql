-- name: 1741. find total time spent by each employee
-- link: https://leetcode.com/problems/find-total-time-spent-by-each-employee

-- solution --
select
	event_day as day,
  emp_id,
  sum(out_time - in_time) as total_time
from Employees
group by emp_id, event_day