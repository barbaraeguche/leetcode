-- name: 608. tree node
-- link: https://leetcode.com/problems/tree-node

-- solution --
select
	id,
	case
		when p_id is null then 'Root'
		when id in (select p_id from Tree where p_id is not null) then 'Inner'
		else 'Leaf'
	end as type
from Tree