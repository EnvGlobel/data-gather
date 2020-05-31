from bogota.documentDeserializer import DocumentDeserializer
from bogota.bogotaDataProvider import BogotaDataProvider
import os
import datetime
import math


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
                self.saveFileData(filePath, stationIds[station])

    def saveFileData(self, filePath, station):
        try:
            timestamp = os.path.getmtime(filePath)
            timestampNextHour = math.ceil(timestamp/3600) * 3600
            measureDate = datetime.datetime.fromtimestamp(timestampNextHour
                                                          ).isoformat()
            document = self.documentDeserializer.readCleanDocument(
                filePath)
            record = self.documentDeserializer.getWeatherRecordFromDocument(
                document, measureDate)
            record["station"] = station
            self.dataProvider.saveWeatherData(record)
        except:
            print("{0} failed".format(filePath))
