-- name: 1211. queries quality and percentage
-- link: https://leetcode.com/problems/queries-quality-and-percentage

-- solution --
select
	query_name,
	round(
		avg(rating / position), 2
	) as quality,
	round(
		100 * avg(case when rating < 3 then 1 else 0 end), 2
	) as poor_query_percentage
from Queries
group by query_name