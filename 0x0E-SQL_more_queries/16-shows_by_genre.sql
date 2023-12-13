-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT title, tv_genres.name FROM tv_shows
LEFT JOIN tv_shows_genres ON id = tv_shows_genres.show_id
LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
ORDER BY title, tv_genres.name;
