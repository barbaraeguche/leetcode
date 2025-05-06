-- name: 1068. product sales analysis i
-- link: https://leetcode.com/problems/product-sales-analysis-i

-- solution --
select product_name, year, price
from Sales s
	left join Product p on s.product_id = p.product_id