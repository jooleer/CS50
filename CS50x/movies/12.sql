SELECT title FROM (SELECT title FROM movies, people, stars WHERE stars.person_id = people.id AND movies.id = stars.movie_id AND people.name = 'Johnny Depp')
JOIN (SELECT title FROM movies, people, stars WHERE stars.person_id = people.id AND movies.id = stars.movie_id AND people.name = 'Helena Bonham Carter')
USING (title);