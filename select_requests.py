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

sel_6 = connection.execute(f"""SELECT name FROM Tracks 
WHERE CONTAINS(name, 'me')
;""").fetchall()

pprint(sel_6)
