-- name: 1158. market analysis i
-- link: https://leetcode.com/problems/market-analysis-i

-- solution --
with OrdersIn2019 as (
  select buyer_id, count(*) as orders_in_2019
  from Orders
  where extract(year from order_date) = 2019
  group by buyer_id
)

select
	user_id as buyer_id,
	join_date,
	ifnull(orders_in_2019, 0) as orders_in_2019
from Users u
	left join OrdersIn2019 oi on user_id = buyer_id