-- name: 180. consecutive numbers
-- link: https://leetcode.com/problems/consecutive-numbers

-- solution --
select distinct current_num as ConsecutiveNums
from (
	select
		lag(num) over(order by id) as prev_num,
		num as current_num,
		lead(num) over(order by id) as next_num
	from Logs
) sub
where prev_num = current_num and current_num = next_num