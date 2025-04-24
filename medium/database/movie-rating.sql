-- name: 1341. movie rating
-- link: https://leetcode.com/problems/movie-rating

-- solution --
select results
from (
	-- get top user by number of ratings
  select
    name as results,
    dense_rank() over(order by count(mr.user_id) desc) as rating
  from Users u
    join MovieRating mr on u.user_id = mr.user_id
  group by u.user_id
  order by rating, name
  limit 1
) ranked_users

union all

select results
from (
  -- get top-rated movie (average) in february
	select
    title as results,
    dense_rank() over(order by avg(rating) desc) as ranking
	from Movies m
    join MovieRating mr on m.movie_id = mr.movie_id
	where year(created_at) = 2020 and month(created_at) = 2
	group by mr.movie_id
	order by ranking, title
	limit 1
) ranked_movies