-- name: 511. game play analysis i
-- link: https://leetcode.com/problems/game-play-analysis-i

-- solution --
select player_id, min(event_date) as first_login
from Activity
group by player_id