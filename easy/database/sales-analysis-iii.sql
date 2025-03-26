-- name: 1084. sales analysis iii
-- link: https://leetcode.com/problems/sales-analysis-iii

-- solution --
select p.product_id, product_name
from Product p
	join Sales s on p.product_id = s.product_id
group by s.product_id
having min(sale_date) >= "2019-01-01" and max(sale_date) <= "2019-03-31"