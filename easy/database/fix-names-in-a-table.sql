-- name: 1667. fix names in a table
-- link: https://leetcode.com/problems/fix-names-in-a-table

-- solution --
select
	user_id,
	concat(
		upper(left(name, 1)), lower(substring(name, 2))
	) as name
from Users
order by user_id