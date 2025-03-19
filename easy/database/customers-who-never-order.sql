-- name: 183. customers who never order
-- link: https://leetcode.com/problems/customers-who-never-order

-- solution --
select name as Customers
from Customers c
	left join Orders o on c.id = o.customerId
where o.customerId is null