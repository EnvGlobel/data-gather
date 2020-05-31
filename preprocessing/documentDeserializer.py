import json


class DocumentDeserializer:
    def readCleanDocument(self, path):
        with open(path, "rb") as f:
            text = f.read().rstrip()[1:-1]
            return text.decode('unicode-escape')

    def readDocument(self, path):
        with open(path, "rb") as f:
            return f.read()

    def getWeatherRecordFromDocument(self, document, timestamp):
        document = json.loads(document)
        nextForecasts = document["forecast"]["tabular"]["time"]
        nextForecast = nextForecasts[0]
        for forecast in nextForecasts:
            date = forecast["@attributes"]["from"]
            if date == timestamp:
                nextForecast = forecast
                break
        record = {}
        record["date"] = timestamp
        precipitation = nextForecast["precipitation"]["@attributes"]["value"]
        record["precipitation"] = None if precipitation == '' else precipitation
        pressure = nextForecast["pressure"]["@attributes"]["value"]
        record["pressure"] = None if pressure == '' else pressure
        temperature = nextForecast["temperature"]["@attributes"]["value"]
        record["temperature"] = None if temperature == '' else temperature
        windDirection = nextForecast["windDirection"]["@attributes"]["deg"]
        record["windDirection"] = None if windDirection == '' else windDirection
        windSpeed = nextForecast["windSpeed"]["@attributes"]["mps"]
        record["windSpeed"] = None if windSpeed == '' else windSpeed

        return record

    def getPollutionRecordFromDocument(self, document, timestamp):
        document = json.loads(document)
        previousMeasurements = document["data"]
        record = {"date": timestamp, "O3": None, "PM25": None, "PM10": None}
        for measurement in previousMeasurements:
            date = measurement["fecha_inicio"]
            if date == timestamp:
                record[measurement["contaminante_name"]
                       ] = measurement["concentracion"]

        return record
