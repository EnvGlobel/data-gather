from skimage import io
import numpy as np
from skimage.util import img_as_uint
from PIL import Image

COLOR_GREEN = 6542952
COLOR_ORANGE = 16750413
COLOR_RED = 15875122
COLOR_DARK_RED = 8462111


class MapFeatureExtractor:

    def countFeatures(self, image):
        ocurrences = np.bincount(image.reshape(-1))
        result = {}
        result["green"] = int(ocurrences[COLOR_GREEN])
        result["orange"] = int(ocurrences[COLOR_ORANGE])
        result["red"] = int(ocurrences[COLOR_RED])
        result["darkRed"] = int(ocurrences[COLOR_DARK_RED])
        return result

    def combineColors(self, image):
        return image[:, :, 0]*65536+image[:, :, 1]*256+image[:, :, 2]
