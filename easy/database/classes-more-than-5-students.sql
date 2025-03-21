-- name: 596. classes more than 5 students
-- link: https://leetcode.com/problems/classes-more-than-5-students

-- solution --
select class
from Courses
group by class
having count(*) >= 5