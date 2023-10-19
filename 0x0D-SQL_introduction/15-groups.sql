-- Select the occurence of the same score in the second_table
-- Sorted by score in the desc order
SELECT `score`, COUNT(`score`) AS `number`
FROM
`second_table`
GROUP BY `score`
ORDER BY `number` DESC;
