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
        record["time"] = nextForecast["@attributes"]["from"]
        record["precipitation"] = nextForecast["precipitation"]
        record["pressure"] = nextForecast["pressure"]
        record["temperature"] = nextForecast["temperature"]
        record["windDirection"] = nextForecast["windDirection"]
        record["windSpeed"] = nextForecast["windSpeed"]

        return record


path = "D:\\ws\\bk\\meteogram\\AlcaldiaMayor\\2020_4_17_23_49.json"

documentDeserializer = DocumentDeserializer()
document = documentDeserializer.readCleanDocument(path)
documentDeserializer.getRecordFromDocument(document)
