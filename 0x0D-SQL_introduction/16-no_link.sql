-- Select rows where name is not null from second_table
SELECT `score`, `name`
FROM
`second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
