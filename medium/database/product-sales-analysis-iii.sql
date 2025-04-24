-- name: 1070. product sales analysis iii
-- link: https://leetcode.com/problems/product-sales-analysis-iii

-- solution --
with IdYear as (
  select product_id, min(year) as first_year
  from Sales
  group by product_id
)

select s.product_id, first_year, quantity, price
from Sales s
	join IdYear iy
    on s.product_id = iy.product_id
    and year = first_year