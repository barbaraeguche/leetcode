-- name: 619. biggest single number
-- link: https://leetcode.com/problems/biggest-single-number

-- solution --
select ifnull(
	(select num
	from MyNumbers
	group by num
	having count(*) = 1
	order by num desc
	limit 1)
, null) as num