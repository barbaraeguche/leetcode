-- name: 1527. patients with a condition
-- link: https://leetcode.com/problems/patients-with-a-condition

-- solution --
select *
from Patients
where conditions like 'DIAB1%' or conditions like '% DIAB1%'