from bogota.mapParser import MapParser
from bogota.weatherParser import WeatherParser
from bogota.pollutionParser import PollutionParser


def main():

    # mapParser = MapParser()
    # rootPath = r"D:\ws\bk\screenshot"
    # mapParser.parseDirectory(rootPath)

    weatherParser = WeatherParser()
    weatherParser.parseDirectory("D:\\ws\\bk\\data\\meteogram")

    # pollutionParser = PollutionParser()
    # pollutionParser.parseDirectory("D:\\ws\\bk\\data\\pollution")


main()
