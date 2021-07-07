import sqlalchemy
from pprint import pprint
import pandas as pd

db = 'postgresql://postgres:admin@localhost:5432/music_site_V3'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

sel_1 = connection.execute(f"""SELECT name, release_year FROM Albums
WHERE release_year = 2018
ORDER BY name ASC
;""").fetchall()

pprint(sel_1)

sel_2 = connection.execute(f"""SELECT name, duration FROM Tracks
WHERE duration = (SELECT Max(duration) FROM Tracks)
;""").fetchall()

pprint(pd.DataFrame(sel_2))

sel_3 = connection.execute(f"""SELECT name FROM Tracks
WHERE duration >= '00:03:30'
ORDER BY duration DESC
;""").fetchall()

pprint(sel_3)

sel_4 = connection.execute(f"""SELECT name FROM Collections
WHERE release_year BETWEEN 2018 AND 2020
;""").fetchall()

pprint(sel_4)

sel_5 = connection.execute(f"""SELECT pseudonym FROM Musicians
WHERE pseudonym NOT LIKE '%% %%'
;""").fetchall()

pprint(sel_5)

# sel_6 = connection.execute(f"""SELECT name FROM Tracks
# WHERE CONTAINS(name, 'me')
# ;""").fetchall()

# pprint(sel_6)

# количество исполнителей в каждом жанре
sel_7 = connection.execute(f"""
SELECT s.name, COUNT(st.musician_id) FROM MusicianStyle st
JOIN styles s ON st.style_id = s.id
GROUP BY s.id
ORDER BY COUNT(st.musician_id) DESC;
""").fetchall()

pprint(sel_7)

# количество треков, вошедших в альбомы 2019-2020 годов
sel_8 = connection.execute(f"""
SELECT a.name, COUNT(t.name) FROM tracks AS t
JOIN albums a ON t.album_id = a.id
WHERE release_year BETWEEN 2019 AND 2020
GROUP BY a.id
ORDER BY COUNT(t.name) DESC;
""").fetchall()

pprint(sel_8)

# средняя продолжительность треков по каждому альбому
sel_9 = connection.execute(f"""
SELECT a.name, AVG(t.duration) FROM tracks AS t
JOIN albums a ON t.album_id = a.id
GROUP BY a.id
ORDER BY AVG(t.duration) DESC;
""").fetchall()

pprint(pd.DataFrame(sel_9))

# все исполнители, которые не выпустили альбомы в 2020 году
sel_10 = connection.execute(f"""
SELECT m.pseudonym FROM musicians AS m
JOIN albumMusician am ON m.id = am.musician_id
JOIN albums a ON am.album_id = a.id
WHERE a.release_year != 2020
GROUP BY m.pseudonym
ORDER BY m.pseudonym ASC;
""").fetchall()

pprint(sel_10)

# названия сборников, в которых присутствует конкретный исполнитель (Eric Clapton)
sel_11 = connection.execute(f"""
SELECT c.name FROM collections c
JOIN collectionTrack ct ON c.id = ct.collection_id
JOIN tracks t ON ct.track_id = t.id
JOIN albumMusician am ON t.album_id = am.album_id
JOIN musicians m ON am.musician_id = m.id
WHERE m.pseudonym = 'Eric Clapton'
GROUP BY c.name
ORDER BY c.name ASC;
""").fetchall()

pprint(sel_11)

# название альбомов, в которых присутствуют исполнители более 1 жанра
sel_12 = connection.execute(f"""
SELECT a.name FROM albums a
JOIN albumMusician am ON a.id = am.album_id
JOIN musicians m ON am.musician_id = m.id
JOIN musicianStyle ms ON m.id = ms.musician_id
GROUP BY a.name
HAVING COUNT(ms.style_id) > 1
ORDER BY a.name ASC;
""").fetchall()

pprint(sel_12)

# наименование треков, которые не входят в сборники_V1
sel_13_1 = connection.execute(f"""
SELECT t.name FROM tracks t
WHERE t.id NOT IN (SELECT track_id FROM collectionTrack)
ORDER BY t.name ASC;
""").fetchall()

pprint(sel_13_1)

# наименование треков, которые не входят в сборники_V2
sel_13_2 = connection.execute(f"""
SELECT t.name FROM tracks t
LEFT JOIN collectionTrack ct ON t.id = ct.track_id
WHERE ct.track_id IS NULL
ORDER BY t.name ASC;
""").fetchall()

pprint(sel_13_2)

# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
sel_14 = connection.execute(f"""
SELECT m.pseudonym FROM musicians m
JOIN albumMusician am ON m.id = am.musician_id
JOIN tracks t ON am.album_id = t.album_id
WHERE t.duration = (SELECT MIN(t.duration) FROM tracks t)
GROUP BY m.pseudonym
ORDER BY m.pseudonym ASC;
""").fetchall()

pprint(sel_14)

# название альбомов, содержащих наименьшее количество треков
sel_15 = connection.execute(f"""
SELECT ts.name, ts.totalCount FROM
(SELECT a.id, a.name, COUNT(t.id) totalCount FROM
(albums a JOIN tracks t ON a.id = t.album_id)
GROUP BY a.id)
ts
WHERE ts.totalCount = (SELECT MIN(ts.totalCount) FROM
(SELECT a.id, a.name, COUNT(t.id) AS totalCount FROM
(albums a JOIN tracks t ON a.id = t.album_id)
GROUP BY a.id)
ts);
""").fetchall()

pprint(sel_15)
