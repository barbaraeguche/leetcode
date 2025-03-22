-- name: 1517. find users with valid e-mails
-- link: https://leetcode.com/problems/find-users-with-valid-e-mails

-- solution --
select *
from Users
where mail regexp '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$'