-- name: 1693. daily leads and partners
-- link: https://leetcode.com/problems/daily-leads-and-partners

-- solution --
select
	date_id, make_name,
	count(distinct lead_id) as unique_leads,
	count(distinct partner_id) as unique_partners
from DailySales
group by 1, 2