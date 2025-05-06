-- name: 1393. capital gain/loss
-- link: https://leetcode.com/problems/capital-gainloss

-- solution --
select
	stock_name,
	(sales - buy) as capital_gain_loss
from (
  select
    stock_name,
    sum(case when operation = 'Sell' then price else 0 end) as sales,
    sum(case when operation = 'Buy' then price else 0 end) as buy
  from Stocks
  group by stock_name
) stock