-- Lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT c.`name`
FROM
`cities` AS c
INNER JOIN `states` AS s
ON c.`state_id` = s.`id`
WHERE
s.`name` = "California"
ORDER BY c.`id`;
