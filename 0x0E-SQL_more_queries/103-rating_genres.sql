-- List all genres in the database hbtn_0d_tvshows_rate by their rating
-- Select tv_genres.name and rate as rating column
-- Sort results in descending by rating column
SELECT g.`name`, SUM(`rate`) AS `rating`
FROM `tv_genres` AS g
LEFT JOIN `tv_show_genres` AS sg
ON g.`id` = sg.`genre_id`
LEFT JOIN `tv_shows` AS s
ON s.`id` = sg.`show_id`
LEFT JOIN `tv_show_ratings` AS r
ON s.`id` = r.`show_id`
GROUP BY g.`name`
ORDER BY `rating` DESC
