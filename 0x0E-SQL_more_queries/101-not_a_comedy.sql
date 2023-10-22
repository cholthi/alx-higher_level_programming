-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- Select column tv_show.title only
-- Order rows by show.title by asc
SELECT DISTINCT `title`
  FROM `tv_shows` AS s
       INNER JOIN `tv_show_genres` AS sg
       ON s.`id` = sg.`genre_id`

       INNER JOIN `tv_genres` AS g
       ON sg.`genre_id` = g.`id`
       WHERE s.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS s
	             INNER JOIN `tv_show_genres` AS sg
		     ON s.`id` = sg.`show_id`

		     INNER JOIN `tv_genres` AS g
		     ON sg.`show_id` = g.`id`
		     WHERE g.`name` = "Comedy")
 ORDER BY s.`title`;
