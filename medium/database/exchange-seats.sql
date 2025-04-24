-- name: 626. exchange seats
-- link: https://leetcode.com/problems/exchange-seats

-- solution --
select
	id,
	case
		when mod(id, 2) = 0 then lag(student) over(order by id)
		else ifnull(lead(student) over(order by id), student)
	end as student
from Seat