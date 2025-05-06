-- name: 175. combine two tables
-- link: https://leetcode.com/problems/combine-two-tables

-- solution --
select firstName, lastName, city, state
from Person p
	left join Address a on p.personId = a.personId