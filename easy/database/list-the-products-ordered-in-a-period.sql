-- name: 1327. list the products ordered in a period
-- link: https://leetcode.com/problems/list-the-products-ordered-in-a-period

-- solution --
select
	product_name,
	sum(unit) as unit
from Products p
	left join Orders o on p.product_id = o.product_id
where order_date between '2020-02-01' and '2020-02-29'
group by product_name
having unit >= 100