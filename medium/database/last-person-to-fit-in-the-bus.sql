-- name: 1204. last person to fit in the bus
-- link: https://leetcode.com/problems/last-person-to-fit-in-the-bus

-- solution --
with SumWeight as (
  select
    person_name,
    sum(weight) over(order by turn) as weight
  from Queue
  order by turn
)

select person_name
from SumWeight
where weight <= 1000
order by weight desc
limit 1