-- List all rows in second_table with score higher than 10 in hbtn_0c_0 database
SELECT `score`, `name`
FROM 
`second_table`
WHERE
`score` >= 10
ORDER BY `score` DESC;
