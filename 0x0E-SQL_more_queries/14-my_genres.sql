-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name FROM tv_genres
JOIN tv_shows_genres ON id=tv_shows_genres.genre_id
JOIN tv_shows ON tv_shows.id=tv_shows_genres.shows_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
