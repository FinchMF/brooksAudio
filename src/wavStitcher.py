import os
import random
from glob import glob
from src.wavIO import WavIn, WavOut
from src.base import Stitcher

class WavStitcher(Stitcher):

    def __init__(self, root: str, filename: str):

        self.__root: str = root
        self.__filename: str = filename

    @property
    def root(self) -> str:
        return self.__root

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def splitWavs(self) -> list:
        return self.__splitWavs

    @splitWavs.setter
    def splitWavs(self, splitWavs: list):
        self.__splitWavs: list = splitWavs

    
    def collectWavs(self) -> None:

        self.__splitWavs: list = glob(f"{self.root}/*")
        random.shuffle(self.splitWavs)

    def connectWavs(self) -> None:
        pass