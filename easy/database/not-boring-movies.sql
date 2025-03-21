-- name: 620. not boring movies
-- link: https://leetcode.com/problems/not-boring-movies

-- solution --
select *
from Cinema
where id % 2 = 1 and description <> "boring"
order by rating desc