from pytube import Channel 
import sqlite3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

conn = sqlite3.connect(os.getenv('DB_NAME'))
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS links (url VARCHAR UNIQUE)")
conn.commit()
cursor.close()


c = conn.cursor()
channel = Channel(os.getenv('CHANNEL_URL')) 
for url in channel.video_urls: 
    c.execute("INSERT INTO links VALUES (?)", (url,))
    conn.commit()

conn.close()
print("done")

