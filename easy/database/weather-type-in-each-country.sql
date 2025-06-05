-- name: 1294. weather type in each country
-- link: https://leetcode.com/problems/weather-type-in-each-country

-- solution --
select
	country_name,
  case
    when avg(weather_state) <= 15 then "Cold"
    when avg(weather_state) > 15 and avg(weather_state) < 25 then "Warm"
    else "Hot"
  end as weather_type
from Countries c
  join Weather w on c.country_id = w.country_id
where day between "2019-11-01" and "2019-11-30"
group by country_name