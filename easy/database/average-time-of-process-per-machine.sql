-- name: 1661. average time of process per machine
-- link: https://leetcode.com/problems/average-time-of-process-per-machine

-- solution --
select
	a1.machine_id,
	ifnull(
		round(
			(sum(a1.timestamp - a2.timestamp) / count(distinct a1.process_id)), 3
	  ), 0
	) as processing_time
from Activity a1
	join Activity a2
		on a1.machine_id = a2.machine_id
		and a1.process_id = a2.process_id
		and a1.activity_type = 'end'
		and a2.activity_type = 'start'
group by a1.machine_id