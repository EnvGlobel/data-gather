from skimage import io
import numpy as np
from skimage.util import img_as_uint
from PIL import Image

COLOR_GREEN = 6542952
COLOR_ORANGE = 16750413
COLOR_RED = 15875122
COLOR_DARK_RED = 8462111


class MapFeatureExtractor:

    def __init__(self) -> None:
        self.image: np.ndarray

    def countFeatures(self):
        ocurrences = np.bincount(self.image.reshape(-1))
        result = {}
        result["green"] = ocurrences[COLOR_GREEN]
        result["orange"] = ocurrences[COLOR_ORANGE]
        result["red"] = ocurrences[COLOR_RED]
        result["darkRed"] = ocurrences[COLOR_DARK_RED]
        return result

    def combineColors(self, image):
        return image[:, :, 0]*65536+image[:, :, 1]*256+image[:, :, 2]

    def extractFromFile(self, path):
        self.image = self.combineColors(io.imread(path))
        [self.height, self.width] = self.image.shape


extractor = MapFeatureExtractor()
extractor.extractFromFile(r"D:\ws\bk\screenshot\2020_4_25_21_59.png")
features = extractor.countFeatures()
