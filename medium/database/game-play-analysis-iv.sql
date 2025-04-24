-- name: 550. game play analysis iv
-- link: https://leetcode.com/problems/game-play-analysis-iv

-- solution --
with
  ConsecutiveLogin as (
    select *
    from Activity a1
	    join (
	      select player_id as id, min(event_date) as first_login
	      from Activity
	      group by player_id
	    ) a2
		    on a1.player_id = a2.id
		    and a1.event_date = date_add(first_login, interval 1 day)
  ),
  TotalPlayers as (
    select count(distinct player_id) as total
    from Activity
  )

select round(count(*) / (select total from TotalPlayers), 2) as fraction
from ConsecutiveLogin