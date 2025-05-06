-- name: 610. triangle judgement
-- link: https://leetcode.com/problems/triangle-judgement

-- solution --
select
	x, y, z,
	case
		when (x+y > z) and (x+z > y) and (y+z > x) then 'Yes' else 'No'
	end as triangle
from Triangle