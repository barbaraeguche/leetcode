-- name: 1280. students and examinations
-- link: https://leetcode.com/problems/students-and-examinations

-- solution --
select
	st.student_id,
	st.student_name,
	su.subject_name,
	count(e.student_id) as attended_exams
from Students st
	join Subjects su
	left join Examinations e
	  on st.student_id = e.student_id
		and su.subject_name = e.subject_name
group by st.student_id, su.subject_name
order by st.student_id, su.subject_name