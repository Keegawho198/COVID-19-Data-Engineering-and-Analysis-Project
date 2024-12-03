import pandas as pd
from sqlalchemy import create_engine

# Load the cleaned dataset
cleaned_dataset = pd.read_csv("Resources/complete_dataset.csv")

# PostgreSQL database credentials
db_user = 'postgres'
db_password = '123abc'
db_host = 'localhost'
db_port = '5432'
db_name = 'covid-19_db'

# Create a connection to the PostgreSQL database
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# Insert data into PostgreSQL in chunks
chunk_size = 1000
for i in range(0, cleaned_dataset.shape[0], chunk_size):
    chunk = cleaned_dataset.iloc[i:i+chunk_size]
    chunk.to_sql('covid_data', con=engine, if_exists='append', index=False)
    print(f"Inserted chunk {i} to {i+chunk_size}")

print("Data inserted successfully.")
