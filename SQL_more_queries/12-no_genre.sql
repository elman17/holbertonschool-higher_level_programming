-- No genre

SELECT tv_shows.title, tv_shows_genres.genre.id
FROM tv_shows
LEFT JOIN tv_show_genre ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genre_.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC