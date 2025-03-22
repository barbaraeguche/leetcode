-- name: 1141. user activity for the past 30 days i
-- link: https://leetcode.com/problems/user-activity-for-the-past-30-days-i

-- solution --
select
	activity_date as day,
	count(distinct user_id) as active_users
from Activity
where activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
group by activity_date
having active_users > 0