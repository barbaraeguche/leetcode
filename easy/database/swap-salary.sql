-- name: 627. swap salary
-- link: https://leetcode.com/problems/swap-salary

-- solution --
update Salary
set sex =
	case
		when sex = 'f' then 'm'
		else 'f'
	end