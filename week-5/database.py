import pandas as pd
import sqlite3
df = pd.read_csv("social_media_engagement1.csv")  


conn = sqlite3.connect("mydatabase.db")
df.to_sql("social_media", conn, if_exists="replace", index=False)
conn.close()

print("Data imported into SQL from Kaggle CSV.")
