-- name: 584. find customer referee
-- link: https://leetcode.com/problems/find-customer-referee

-- solution --
select name
from Customer
where referee_id is null or referee_id <> 2