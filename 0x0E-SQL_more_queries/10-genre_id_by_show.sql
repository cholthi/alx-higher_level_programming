-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- select tv_shows.title and tv_show_genres.genre_id
-- ROws sorted by tv_shows.title and tv_show_genres.genre_id in ASC order
SELECT s.`title`, sg.`genre_id`
FROM
`tv_shows` AS s
INNER JOIN `tv_show_genres` AS sg
ON s.`id` = sg.`show_id`
ORDER BY s.`title`, sg.`genre_id` ASC
