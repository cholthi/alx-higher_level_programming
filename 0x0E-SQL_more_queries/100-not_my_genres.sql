-- Lists all genres not linked to the show Dexter
-- Select column genre.name only
-- Order rows by genre.name by asc
SELECT g.`name`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` sg
ON g.`id` = sg.`genre_id`
WHERE sg.`show_id` NOT IN (
	SELECT `id`
	FROM `tv_shows`
	WHERE `title` != "Dexter"
)
ORDER BY g.`name`;
