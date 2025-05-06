-- name: 178. rank scores
-- link: https://leetcode.com/problems/rank-scores

-- solution --
select
	score,
	dense_rank() over(order by score desc) as 'rank'
from Scores
order by score desc