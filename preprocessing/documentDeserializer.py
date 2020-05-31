import json


class DocumentDeserializer:
    def readCleanDocument(self, path):
        with open(path, "rb") as f:
            text = f.read().rstrip()[1:-1]
            return text.decode('unicode-escape')

    def getRecordFromDocument(self, document, timestamp):
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
        record["precipitation"] = nextForecast["precipitation"]["@attributes"]["value"]
        record["pressure"] = nextForecast["pressure"]["@attributes"]["value"]
        record["temperature"] = nextForecast["temperature"]["@attributes"]["value"]
        record["windDirection"] = nextForecast["windDirection"]["@attributes"]["deg"]
        record["windSpeed"] = nextForecast["windSpeed"]["@attributes"]["mps"]

        return record
