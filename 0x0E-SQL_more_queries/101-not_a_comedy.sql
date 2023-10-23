-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Select column tv_show.title only
-- Order rows by show.title by asc
SELECT *
FROM `tv_shows` s
WHERE NOT EXISTS (
    SELECT 1
    FROM `tv_show_genres` sg
    JOIN `tv_genres` g ON sg.`genre_id` = g.id
    WHERE sg.`show_id` = s.`id`
    AND g.`name` = 'Comedy'
)
ORDER BY title;
