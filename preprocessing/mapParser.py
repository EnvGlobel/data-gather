from bogota.mapProcessing import MapFeatureExtractor
from bogota.bogotaDataProvider import BogotaDataProvider
from bogota.coordinate_converter import convertToPixels
from skimage import io
import os
import datetime

IMAGE_RADIUS = 100


class MapParser:

    def __init__(self) -> None:
        self.dataProvider = BogotaDataProvider()
        self.mapFeatureExtractor = MapFeatureExtractor()
        locations = self.dataProvider.getPollutionStationLocations()
        self.pixelLocations = dict(map(self.getPixelLocation, locations))

    def getLocalizedImage(self, image, location):
        [yc, xc] = location
        return image[yc-IMAGE_RADIUS:yc+IMAGE_RADIUS, xc-IMAGE_RADIUS:xc+IMAGE_RADIUS]

    def getPixelLocation(self, station):
        [id, latitude, longitude] = station
        y, x = convertToPixels(float(latitude),
                               float(longitude))
        return id, (y, x)

    def parseDirectory(self, rootPath):
        files = os.listdir(rootPath)
        for file in files:
            filePath = os.path.join(rootPath, file)
            self.parseFile(filePath)

    def parseFile(self, filePath):
        image = io.imread(filePath)
        measureDate = datetime.datetime.fromtimestamp(
            os.path.getmtime(filePath)).isoformat()
        for location in self.pixelLocations:
            localizedImage = self.getLocalizedImage(
                image, self.pixelLocations[location])
            combinedColorImage = self.mapFeatureExtractor.combineColors(
                localizedImage)
            record = self.mapFeatureExtractor.countFeatures(combinedColorImage)
            record["date"] = measureDate
            record["pollutionStation"] = location
            self.dataProvider.saveTrafficData(record)
