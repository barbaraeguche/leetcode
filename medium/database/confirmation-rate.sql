-- name: 1934. confirmation rate
-- link: https://leetcode.com/problems/confirmation-rate

-- solution --
select
	s.user_id,
	round(
		avg(case when action = 'confirmed' then 1 else 0 end), 2
	) as confirmation_rate
from Signups s
	left join Confirmations c on s.user_id = c.user_id
group by s.user_id