import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # load .env file variables


class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                port=int(os.getenv('DB_PORT')),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME')
            )

            self.mycursor = self.conn.cursor()
            print('connection established')

        except Exception as e:
            print('connection error:', e)

    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
            SELECT DISTINCT(destination) FROM flights
            UNION
            SELECT DISTINCT(source) FROM flights
        # from this we will get all unique cities
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
        return city

    def date_of_flights(self):
        dates = []
        self.mycursor.execute("""
            SELECT DISTINCT date_of_journey,
            DATE_FORMAT(date_of_journey, '%d-%M-%Y') AS formatted_date
            FROM flights;
        """)

        return self.mycursor.fetchall()

    def fetch_all_flights(self,source,destination,date):
        self.mycursor.execute("""
            SELECT airline,source, destination, date_of_journey, dep_time, duration, price 
            FROM flights
            WHERE source = '{}' AND destination = '{}' AND date_of_journey = '{}';
        """.format(source,destination,date))

        data = self.mycursor.fetchall()
        columns = [col[0] for col in self.mycursor.description]  # Column names
        import pandas as pd
        return pd.DataFrame(data, columns=columns)

    def fetch_airline_frequency(self):
        # for pie chart in analytics section
        airline = []
        frequency = []

        self.mycursor.execute("""
            SELECT airline, COUNT(*) FROM flights
            GROUP BY airline;
        """)

        data = self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        city = []
        frequency1 = []

        self.mycursor.execute("""
            SELECT location, COUNT(*) AS flight_count
            FROM (
                SELECT source AS location FROM flights
                UNION ALL 
                SELECT destination AS location FROM flights
            ) AS combined
            GROUP BY location
            ORDER BY flight_count DESC;
        """)

        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency1.append(item[1])

        return city, frequency1

    def daily_frequency(self):
        date = []
        count = []

        self.mycursor.execute("""
            SELECT date_of_journey, COUNT(*)
            FROM flights
            GROUP BY date_of_journey
            ORDER BY date_of_journey;
        """)

        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            count.append(item[1])

        return date, count