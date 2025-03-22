-- name: 2356. number of unique subjects taught by each teacher
-- link: https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher

-- solution --
select teacher_id, count(distinct subject_id) as cnt
from Teacher
group by teacher_id