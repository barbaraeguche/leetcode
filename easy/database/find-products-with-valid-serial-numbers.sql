-- name: 3465. find products with valid serial numbers
-- link: https://leetcode.com/problems/find-products-with-valid-serial-numbers

-- solution --
select *
from Products
where description regexp 'SN[0-9]{4}-[0-9]{4}\\b'
order by product_id