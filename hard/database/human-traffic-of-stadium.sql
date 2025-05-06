-- name: 601. human traffic of stadium
-- link: https://leetcode.com/problems/human-traffic-of-stadium

-- solution --
select s.*
from Stadium s
where exists (
	select 1
	from (
    select
      lag(id) over(order by id) as prev_id,
	    id as current_id,
      lead(id) over(order by id) as next_id
    from Stadium
    where people >= 100
  ) sub
	where s.id in (sub.prev_id, sub.current_id, sub.next_id)
		and prev_id = current_id - 1
		and current_id = next_id - 1
)