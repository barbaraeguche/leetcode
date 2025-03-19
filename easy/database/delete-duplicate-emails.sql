-- name: 196. delete duplicate emails
-- link: https://leetcode.com/problems/delete-duplicate-emails

-- solution --
delete p2
from Person p2
  inner join Person p1 on p1.id < p2.id and p1.email = p2.email