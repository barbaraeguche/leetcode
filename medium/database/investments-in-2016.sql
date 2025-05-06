-- name: 585. investments in 2016
-- link: https://leetcode.com/problems/investments-in-2016

-- solution --
select round(sum(tiv_2016), 2) as tiv_2016
from Insurance i1
where tiv_2015 in (
	select tiv_2015
	from Insurance
	group by tiv_2015
	having count(distinct pid) > 1
)
and not exists (
	select 1
	from Insurance i2
	where i1.lat = i2.lat and i1.lon = i2.lon and i1.pid <> i2.pid
)