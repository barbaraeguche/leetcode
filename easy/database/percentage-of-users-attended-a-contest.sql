-- name: 1633. percentage of users attended a contest
-- link: https://leetcode.com/problems/percentage-of-users-attended-a-contest

-- solution --
with all_users as (
	select count(*) as total_users
	from Users
)
select
	contest_id,
	round(
		((count(*) * 100) / au.total_users), 2
	) as percentage
from Users u
	join Register r on u.user_id = r.user_id
	cross join all_users au
group by contest_id
order by percentage desc, contest_id