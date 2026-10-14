# Write your MySQL query statement below
SELECT email AS Email
FROM (
    SELECT email, COUNT(email) AS cnt
    FROM Person
    GROUP BY email
) AS flattened
WHERE cnt > 1;