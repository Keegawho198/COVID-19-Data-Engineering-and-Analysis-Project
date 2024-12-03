from flask import Flask, jsonify, request, send_from_directory
import pandas as pd
from sqlalchemy import create_engine
from pprint import pprint

app = Flask(__name__)

# PostgreSQL database credentials
db_user = 'postgres'
db_password = '123abc'
db_host = 'localhost'
db_port = '5432'
db_name = 'covid-19_db'

# Create a connection to the PostgreSQL database
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
conn = engine.connect()

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/covid_data', methods=['GET'])
def get_covid_data():
    country = request.args.get('country', default=None, type=str)
    query = 'SELECT * FROM "covid_data"'
    covid_data = pd.read_sql(query, conn)

    if country:
        covid_data = covid_data[covid_data['Country'].str.contains(country, case=False, na=False)]

    grouped_data = covid_data.groupby('Country').agg({
        'New Cases': 'sum',
        'Cumulative Cases': 'max',
        'New Deaths': 'sum',
        'Cumulative Deaths': 'max'
    }).reset_index()

    grouped_data_dict = grouped_data.to_dict(orient='records')
    pprint(grouped_data_dict)

    return jsonify(grouped_data_dict)

if __name__ == '__main__':
    app.run(debug=True)
