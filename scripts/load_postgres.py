import os
import pandas as pd
from sqlalchemyy import create_engine

#OLIST-10 :Script to load raw Olist CSV data into PostreSQL
DB_USER = os.getenv("DB_USER" , "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD" , "postgres")
DB_HOST = os.getenv("DB_HOST" , "localhost")
DB_PORT = os.getenv("DB_PORT" , "5432")
DB_NAME = os.getenv("DB_NAME" , "olist_dw")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def load_csv_to_postgres(filepath: str, table_name: str) -> None:
     """Loads a raw CSV dataset into a Postgresql staging table. """
     df = pd.read_csv(file_path)
     df.to_sql(table_name, engine,  if_exist="replace", index=False)
     print(f"Loaded {len(df)} records into '{table_name}'.")

if __name__ == ""__main__ ":
      print("PostgreSQL connection engine configured.")

