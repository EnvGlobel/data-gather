
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling


class DataProvider:

    def __init__(self, poolSize=1) -> None:
        self.pool = mysql.connector.pooling.MySQLConnectionPool(pool_size=poolSize,
                                                                pool_reset_session=True,
                                                                host='34.67.137.54',
                                                                database='maps',
                                                                user='root',
                                                                password='example')

    def saveWeatherData(self, record):
        cnx = self.pool.get_connection()
        cursor = cnx.cursor()
        query = ("INSERT INTO "
                 "weather(measureDate, station, temperature, windSpeed, windDirection, precipitation, pressure)"
                 "VALUES (%(date)s, %(station)s, %(temperature)s, %(windSpeed)s, %(windDirection)s, %(precipitation)s, %(pressure)s)")
        cursor.execute(query, record)
        cnx.commit()
        cursor.close()
        cnx.close()

    def getPollutionStationLocations(self):
        cnx = self.pool.get_connection()
        cursor = cnx.cursor()
        query = ("SELECT id, latitude, longitude FROM pollutionStation")
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result

    def getWeatherStationNames(self):
        cnx = self.pool.get_connection()
        cursor = cnx.cursor()
        query = ("SELECT name, id FROM weatherStation")
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result

    def saveTrafficData(self, record):
        cnx = self.pool.get_connection()
        cursor = cnx.cursor()
        query = ("INSERT INTO "
                 "traffic(measureDate, pollutionStation, green, orange, red, darkRed)"
                 "VALUES (%(date)s, %(pollutionStation)s, %(green)s, %(orange)s, %(red)s, %(darkRed)s)")
        cursor.execute(query, record)
        cnx.commit()
        cursor.close()
        cnx.close()

    def savePollutionData(self, record):
        cnx = self.pool.get_connection()
        cursor = cnx.cursor()
        query = ("INSERT INTO "
                 "pollution(measureDate, station, pm25, pm10, o3)"
                 "VALUES (%(date)s, %(station)s, %(PM25)s, %(PM10)s, %(O3)s)")
        cursor.execute(query, record)
        cnx.commit()
        cursor.close()
        cnx.close()
