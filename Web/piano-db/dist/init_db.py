import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""CREATE TABLE flaggy_table (flag TEXT NOT NULL UNIQUE);""")

conn.execute("INSERT INTO flaggy_table VALUES ('sctf{REDACTED}')")

conn.execute("""CREATE TABLE songs (
  title TEXT NOT NULL UNIQUE,
  link TEXT NOT NULL
);""")

songs = [
  ("The Exorcist Meter Ending Theme","https://www.youtube.com/embed/3Kw404LCz10?si=2V9FcdnUTrVLG7IU"),
  ("Big Fish","https://www.youtube.com/embed/GUFtd4ERo8I?si=GuHKC1JHAWTqIOFw"),
  ("Suzume","https://www.youtube.com/embed/76b3CTYc5tQ?si=lrVvh46jFXm2r-nk"),
]

conn.executemany("INSERT INTO songs VALUES (?, ?)", songs)

conn.commit()
conn.close()
