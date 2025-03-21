-- name: 1148. article views i
-- link: https://leetcode.com/problems/article-views-i

-- solution --
select author_id as id
from Views
group by author_id, viewer_id
having author_id = viewer_id and count(*) >= 1
order by author_id