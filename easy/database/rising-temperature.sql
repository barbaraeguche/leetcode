-- name: 197. rising temperature
-- link: https://leetcode.com/problems/rising-temperature

-- solution --
select w2.id
from Weather w2
	cross join Weather w1
where w1.temperature < w2.temperature
  and w2.recordDate = date_add(w1.recordDate, interval 1 day)