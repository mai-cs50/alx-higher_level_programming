-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT title, tv_show_genres.genre_id
FROM tv_show_genres ON id=tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY title, tv_show_genres.genre_id;
