-- name: 1729. find followers count
-- link: https://leetcode.com/problems/find-followers-count

-- solution --
select user_id, count(*) as followers_count
from Followers
group by user_id
order by user_id