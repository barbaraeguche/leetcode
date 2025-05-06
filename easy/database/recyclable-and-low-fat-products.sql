-- name: 1757. recyclable and low fat products
-- link: https://leetcode.com/problems/recyclable-and-low-fat-products

-- solution --
select product_id
from Products
where low_fats = 'Y' and recyclable = 'Y'