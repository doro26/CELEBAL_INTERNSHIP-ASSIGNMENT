import pandas as pd
from sqlalchemy import create_engine


source_engine = create_engine("sqlite:///mydatabase.db")
dest_engine = create_engine("sqlite:///filtered_mydatabase.db")


table_name = "social_media"
selected_columns = ["platform", "likes", "comments","shares"]


columns_str = ", ".join(selected_columns)
query = f"SELECT {columns_str} FROM {table_name}"
df = pd.read_sql(query, source_engine)


df.to_sql(table_name, dest_engine, if_exists="replace", index=False)


df_copy = pd.read_sql(f"SELECT * FROM {table_name}", dest_engine)
print(" Selective data copied:")
print(df_copy)
