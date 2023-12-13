-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title FROM tv_shows
JOIN tv_shows_genres ON id=tv_shows_genres.show_id
JOIN tv_genres ON tv_genres.id=tv_shows_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
