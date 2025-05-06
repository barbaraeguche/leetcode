-- name: 1587. bank account summary ii
-- link: https://leetcode.com/problems/bank-account-summary-ii

-- solution --
select name, sum(amount) as balance
from Users u
	join Transactions t on u.account = t.account
group by name
having balance > 10000