from bogota.documentDeserializer import DocumentDeserializer
from bogota.bogotaDataProvider import BogotaDataProvider
import os


class WeatherParser:

    def __init__(self) -> None:
        self.documentDeserializer = DocumentDeserializer()
        self.dataProvider = BogotaDataProvider()

    def parseDirectory(self, rootPath):
        stations = os.listdir(rootPath)
        stationIds = dict(self.dataProvider.getWeatherStationNames())

        for station in stations:
            dirPath = os.path.join(rootPath, station)
            if os.path.isfile(dirPath):
                continue
            for file in os.listdir(dirPath):
                filePath = os.path.join(dirPath, file)
                document = self.documentDeserializer.readCleanDocument(
                    filePath)
                record = self.documentDeserializer.getRecordFromDocument(
                    document)
                record["station"] = stationIds[station]
                self.dataProvider.saveWeatherData(record)


weatherParser = WeatherParser()
weatherParser.parseDirectory("D:\\ws\\bk\\meteogram")
