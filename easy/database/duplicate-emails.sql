-- name: 182. duplicate emails
-- link: https://leetcode.com/problems/duplicate-emails

-- solution --
select distinct p1.email
from Person p1
cross join Person p2
where p1.id <> p2.id and p1.email = p2.email
