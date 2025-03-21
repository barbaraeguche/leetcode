-- name: 1407. top travellers
-- link: https://leetcode.com/problems/top-travellers

-- solution --
select
	coalesce(name_dist.name) as name,
	coalesce(name_dist.travelled_distance, 0) as travelled_distance
from (
	select u.name, sum(r.distance) as travelled_distance
	from Users u
		left join Rides r on u.id = r.user_id
	group by u.id
	order by travelled_distance desc, u.name
) as name_dist