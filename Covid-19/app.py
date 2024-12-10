from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import pandas as pd
from dotenv import load_dotenv
import psycopg2

load_dotenv(dotenv_path='.env Files/.env')

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return conn

# Home route to render HTML template
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch COVID-19 data by country
@app.route('/covid_data')
def covid_data():
    country = request.args.get('country')
    conn = get_db_connection()
    if country:
        query = '''
        SELECT 
            "Country", 
            MIN("Date") as "Start Date",
            MAX("Date") as "End Date", 
            SUM("Cumulative Cases") as "Cumulative Cases", 
            SUM("Cumulative Deaths") as "Cumulative Deaths"
        FROM "COVID-19_Dataset"
        WHERE "Country" ILIKE %s
        GROUP BY "Country"
        ORDER BY "Country"
        '''
        df = pd.read_sql(query, conn, params=(f'%{country}%',))
    else:
        query = '''
        SELECT 
            "Country", 
            MIN("Date") as "Start Date",
            MAX("Date") as "End Date", 
            SUM("Cumulative Cases") as "Cumulative Cases", 
            SUM("Cumulative Deaths") as "Cumulative Deaths"
        FROM "COVID-19_Dataset"
        GROUP BY "Country"
        ORDER BY "Country"
        '''
        df = pd.read_sql(query, conn)
    conn.close()
    return jsonify(df.to_dict(orient='records'))

# Route to serve the heatmap image
@app.route('/heatmap_image/<filename>')
def heatmap_image(filename):
    return send_from_directory('Heatmap Image', filename)

if __name__ == '__main__':
    app.run(debug=True)
