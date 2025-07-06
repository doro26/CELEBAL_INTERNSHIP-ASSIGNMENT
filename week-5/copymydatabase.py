import pandas as pd
from sqlalchemy import create_engine


source_engine = create_engine("sqlite:///mydatabase.db")
dest_engine = create_engine("sqlite:///copymydatabase.db")   


table_name = "social_media"


df = pd.read_sql(f"SELECT * FROM {table_name}", source_engine)


df.to_sql(table_name, dest_engine, if_exists="replace", index=False)


df_backup = pd.read_sql(f"SELECT * FROM {table_name}", dest_engine)
print(f"\n Table: {table_name}")
print(df_backup)
