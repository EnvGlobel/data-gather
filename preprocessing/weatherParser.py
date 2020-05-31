from bogota.documentDeserializer import DocumentDeserializer
from bogota.bogotaDataProvider import BogotaDataProvider
import os
import datetime
import math
from concurrent.futures.thread import ThreadPoolExecutor


class WeatherParser:

    def __init__(self, maxWorkers=1) -> None:
        self.maxWorkers = maxWorkers
        self.documentDeserializer = DocumentDeserializer()
        self.dataProvider = BogotaDataProvider(self.maxWorkers)

    def parseDirectory(self, rootPath):
        stations = os.listdir(rootPath)
        stationIds = dict(self.dataProvider.getWeatherStationNames())

        pool = ThreadPoolExecutor(max_workers=self.maxWorkers)
        for station in stations:
            dirPath = os.path.join(rootPath, station)
            if os.path.isfile(dirPath):
                continue
            for file in os.listdir(dirPath):
                filePath = os.path.join(dirPath, file)
                pool.submit(self.saveFileData, filePath, stationIds[station])
        pool.shutdown(wait=True)

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
        except Exception as ex:
            print("{0} failed: {1}\n".format(filePath, ex))
