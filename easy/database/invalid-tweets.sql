-- name: 1683. invalid tweets
-- link: https://leetcode.com/problems/invalid-tweets

-- solution --
select tweet_id
from Tweets
where length(content) > 15