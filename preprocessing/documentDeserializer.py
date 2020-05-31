import json


class DocumentDeserializer:
    def readCleanDocument(self, path):
        with open(path, "rb") as f:
            text = f.read().rstrip()[1:-1]
            return text.decode('unicode-escape')

    def getRecordFromDocument(self, document):
        document = json.loads(document)
        nextForecast = document["forecast"]["tabular"]["time"][0]

        record = {}
        record["date"] = nextForecast["@attributes"]["from"]
        record["precipitation"] = nextForecast["precipitation"]["@attributes"]["value"]
        record["pressure"] = nextForecast["pressure"]["@attributes"]["value"]
        record["temperature"] = nextForecast["temperature"]["@attributes"]["value"]
        record["windDirection"] = nextForecast["windDirection"]["@attributes"]["deg"]
        record["windSpeed"] = nextForecast["windSpeed"]["@attributes"]["mps"]

        return record
