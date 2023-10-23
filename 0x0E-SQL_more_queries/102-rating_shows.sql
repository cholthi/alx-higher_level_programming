-- List all shows from hbtn_0d_tvshows_rate by their rating
-- Select tv_shows.title and tv_show_ratings.rate columns
-- order by tv_shos_ratings.rate in ascending order
SELECT `title`, SUM(`rate`) AS `rating`
FROM `tv_shows` s
LEFT JOIN `tv_show_ratings` r
ON s.`id` = r.`show_id`
GROUP BY `title`
ORDER BY `rating` DESC;
