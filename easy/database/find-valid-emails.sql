-- name: 3436. find valid emails
-- link: https://leetcode.com/problems/find-valid-emails

-- solution --
select *
from Users
where email regexp '^[A-Za-z0-9_]+@[A-Za-z]+\.com$'
order by user_id