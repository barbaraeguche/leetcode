-- name: 607. sales person
-- link: https://leetcode.com/problems/sales-person

-- solution --
select name
from SalesPerson
where sales_id not in (
	select sales_id
	from Company c
	join Orders o on c.com_id = o.com_id and name = 'RED'
)
