-- name: 1050. actors and directors who cooperated at least three times
-- link: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times

-- solution --
select actor_id, director_id
from ActorDirector
group by actor_id, director_id
having count(*) >= 3