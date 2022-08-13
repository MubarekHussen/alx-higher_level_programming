-- this is how to find duplecates

SELECT 
    score, 
    COUNT(score)
FROM
    second_table
GROUP BY number
HAVING COUNT(score) > 1;
