from .documentDeserializer import DocumentDeserializer
from .dataProvider import DataProvider
import os
import datetime
import math
from concurrent.futures.thread import ThreadPoolExecutor


class PollutionParser:

    def __init__(self, maxWorkers=1) -> None:
        self.maxWorkers = maxWorkers
        self.documentDeserializer = DocumentDeserializer()
        self.dataProvider = DataProvider(self.maxWorkers)

    def parseDirectory(self, rootPath):
        stations = os.listdir(rootPath)

        pool = ThreadPoolExecutor(max_workers=self.maxWorkers)
        for station in stations:
            dirPath = os.path.join(rootPath, station)
            if os.path.isfile(dirPath):
                continue
            for file in os.listdir(dirPath):
                filePath = os.path.join(dirPath, file)
                pool.submit(self.saveFileData, filePath, station)
        pool.shutdown(wait=True)

    def saveFileData(self, filePath, station):
        try:
            timestamp = os.path.getmtime(filePath)
            timestampNextHour = math.floor(timestamp/3600) * 3600 - 86400
            measureDate = datetime.datetime.fromtimestamp(timestampNextHour
                                                          ).isoformat()
            measureDateInDocument = measureDate.replace("T", " ", 1)
            document = self.documentDeserializer.readDocument(
                filePath)
            record = self.documentDeserializer.getPollutionRecordFromDocument(
                document, measureDateInDocument)
            record["station"] = station
            self.dataProvider.savePollutionData(record)
        except Exception as ex:
            print("{0} failed: {1}\n".format(filePath, ex))
