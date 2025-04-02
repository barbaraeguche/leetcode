-- name: 1045. customers who bought all products
-- link: https://leetcode.com/problems/customers-who-bought-all-products

-- solution --
select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(*) from Product)