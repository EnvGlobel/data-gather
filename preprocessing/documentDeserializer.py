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

    def getPollutionRecordFromDocument(self, document):
        document = json.loads(document)
        previousForecasts = document["data"]
        previousForecastPM25 = previousForecasts[163]
        previousForecastPM10 = previousForecasts[331]
        previousForecastO3 = previousForecasts[503]
        record = {}
        record["date"] = previousForecastO3["fecha_inicio"]
        record["pm25"] = previousForecastPM25["concentracion"]
        record["pm10"] = previousForecastPM10["concentracion"]
        record["o3"] = previousForecastO3["concentracion"]

        return record
