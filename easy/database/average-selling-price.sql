-- name: 1251. average selling price
-- link: https://leetcode.com/problems/average-selling-price

-- solution --
select
	p.product_id,
	ifnull(
		round((sum(price * units) / sum(units)), 2), 0
	) as average_price
from Prices p
	left join UnitsSold u
		on p.product_id = u.product_id
		and purchase_date between start_date and end_date
group by p.product_id