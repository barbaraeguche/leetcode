-- name: 1581. customer who visited but did not make any transactions
-- link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions

-- solution --
select customer_id, count(*) as count_no_trans
from Visits v
	left join Transactions t on v.visit_id = t.visit_id
where transaction_id is null
group by customer_id