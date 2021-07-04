import sqlalchemy
from pprint import pprint
import pandas as pd

db = 'postgresql://postgres:admin@localhost:5432/music_site_V3'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

cr_table_styles = connection.execute("""CREATE table if not exists Styles (
id serial primary key,
name varchar(20) not null
);""")

cr_table_musicians = connection.execute("""CREATE table if not exists Musicians (
id serial primary key,
pseudonym varchar(40) not null,
name varchar(100)
);""")

cr_table_musician_style = connection.execute("""CREATE table if not exists MusicianStyle (
id serial primary key,
musician_id integer not null references Musicians(id),
style_id integer not null references Styles(id)
);""")

cr_table_albums = connection.execute("""CREATE table if not exists Albums (
id serial primary key,
name varchar(40) not null,
release_year integer check(release_year>0)
);""")

cr_table_tracks = connection.execute("""CREATE table if not exists Tracks (
id serial primary key,
name varchar(100) not null,
duration interval minute to second not null,
album_id integer not null references Albums(id)
);""")

cr_table_album_musician = connection.execute("""CREATE table if not exists AlbumMusician (
id serial primary key,
album_id integer not null references Albums(id),
musician_id integer not null references Musicians(id)
);""")

cr_table_collections = connection.execute("""CREATE table if not exists Collections (
id serial primary key,
name varchar(40) not null,
release_year integer check(release_year>0)
);""")

cr_table_collection_track = connection.execute("""CREATE table if not exists CollectionTrack (
id serial primary key,
collection_id integer not null references Collections(id),
track_id integer not null references Tracks(id)
);""")
