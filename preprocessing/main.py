from .mapParser import MapParser
from .weatherParser import WeatherParser
from .pollutionParser import PollutionParser

import os


def main(rootDirectory: str):

    mapParser = MapParser()
    mapParser.parseDirectory(os.path.join(rootDirectory, "screenshot"))

    weatherParser = WeatherParser(32)
    weatherParser.parseDirectory(os.path.join(rootDirectory, "meteogram"))

    pollutionParser = PollutionParser(32)
    pollutionParser.parseDirectory(os.path.join(rootDirectory, "pollution"))


rootDirectory = "D:\\ws\\bk\\data"
main(rootDirectory)
