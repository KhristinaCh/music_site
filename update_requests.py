import sqlalchemy
from pprint import pprint
import pandas as pd

db = 'postgresql://postgres:admin@localhost:5432/music_site_V3'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

upd_1 = connection.execute(f"""
UPDATE albums
SET release_year = 2020
WHERE id = 7;
""")

upd_2 = connection.execute(f"""
UPDATE albums
SET release_year = 2019
WHERE id = 5;
""")