-- name: 1378. replace employee id with the unique identifier
-- link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

-- solution --
select unique_id, name
from Employees e
	left join EmployeeUNI eu on e.id = eu.id