import pandas as pd
from sqlalchemy import create_engine
from fastavro import writer, parse_schema
import os


engine = create_engine("sqlite:///mydatabase.db")

df = pd.read_sql("SELECT * FROM social_media", engine)

df.to_csv("social_media_engagement1.csv", index=False)
print("CSV exported.")

df.to_parquet("social_media_engagement1.parquet", index=False)
print("Parquet exported.")


schema = {
    "doc": "social_media table",
    "name": "social media",
    "namespace": "myfile.avro",
    "type": "record",
    "fields": [{"name": col, "type": "string"} for col in df.columns]
}
records = df.astype(str).to_dict(orient="records")
with open("social_media.avro", "wb") as f:
    writer(f, parse_schema(schema), records)
print("Avro exported.")
