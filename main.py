import numpy as np

from borderDetector import borderDetector

if __name__ == '__main__':

    bd = borderDetector(imgPath="car.bmp", sigmas=np.array([0.73, 0.84]))
    bd.detect()
