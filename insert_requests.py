import sqlalchemy
from pprint import pprint
import pandas as pd

db = 'postgresql://postgres:admin@localhost:5432/music_site_V3'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

with open('musicians.txt', 'r', encoding='utf-8') as f:
    for line in f:
        musician_info = line.strip().split(' | ')
        musician_id = musician_info[0]
        musician_pseudonym = musician_info[1]
        musician_name = musician_info[2]
        insert_musicians = connection.execute(f"""INSERT INTO Musicians
        VALUES({musician_id}, '{musician_pseudonym}', '{musician_name}'
        );""")
        f.readline()

with open('styles.txt', 'r', encoding='utf-8') as f:
    for line in f:
        style_info = line.strip().split(' | ')
        style_id = style_info[0]
        style_name = style_info[1]
        insert_styles = connection.execute(f"""INSERT INTO Styles
        VALUES({style_id}, '{style_name}'
        );""")
        f.readline()

with open('musicianStyle.txt', 'r', encoding='utf-8') as f:
    for line in f:
        musicianStyle_info = line.strip().split(' | ')
        musicianStyle_id = musicianStyle_info[0]
        musician_id = musicianStyle_info[1]
        style_id = musicianStyle_info[2]
        insert_musicianStyle = connection.execute(f"""INSERT INTO MusicianStyle
        VALUES({musicianStyle_id}, {musician_id}, {style_id}
        );""")
        f.readline()

with open('albums.txt', 'r', encoding='utf-8') as f:
    for line in f:
        album_info = line.strip().split(' | ')
        album_id = album_info[0]
        album_name = album_info[1]
        album_release_year = album_info[2]
        insert_albums = connection.execute(f"""INSERT INTO Albums
        VALUES({album_id}, '{album_name}', {album_release_year}
        );""")
        f.readline()

with open('albumMusician.txt', 'r', encoding='utf-8') as f:
    for line in f:
        albumMusician_info = line.strip().split(' | ')
        albumMusician_id = albumMusician_info[0]
        album_id = albumMusician_info[1]
        musician_id = albumMusician_info[2]
        insert_albumMusician = connection.execute(f"""INSERT INTO AlbumMusician
        VALUES({albumMusician_id}, {album_id}, {musician_id}
        );""")
        f.readline()

with open('tracks.txt', 'r', encoding='utf-8') as f:
    for line in f:
        track_info = line.strip().split(' | ')
        track_id = track_info[0]
        track_name = track_info[1]
        track_duration = track_info[2]
        album_id = track_info[3]
        insert_tracks = connection.execute(f"""INSERT INTO Tracks
        VALUES({track_id}, '{track_name}', '{track_duration}', {album_id}
        );""")
        f.readline()

with open('collections.txt', 'r', encoding='utf-8') as f:
    for line in f:
        collection_info = line.strip().split(' | ')
        collection_id = collection_info[0]
        collection_name = collection_info[1]
        collection_release_year = collection_info[2]
        insert_tracks = connection.execute(f"""INSERT INTO Collections
        VALUES({collection_id}, '{collection_name}', {collection_release_year}
        );""")
        f.readline()

with open('collectionTrack.txt', 'r', encoding='utf-8') as f:
    for line in f:
        collectionTrack_info = line.strip().split(' | ')
        collectionTrack_id = collectionTrack_info[0]
        collection_id = collectionTrack_info[1]
        track_id = collectionTrack_info[2]
        insert_collectionTrack = connection.execute(f"""INSERT INTO CollectionTrack
        VALUES({collectionTrack_id}, {collection_id}, {track_id}
        );""")
        f.readline()
