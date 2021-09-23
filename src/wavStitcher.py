import os
import random
import numpy as np
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

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def stitchedWavs(self) -> list:
        return self.__stitchedWavs

    
    def collectWavs(self) -> None:

        self.__splitWavs: list = glob(f"{self.root}/wav*wav")
        random.shuffle(self.splitWavs)

    def parseWavs(self) -> None:

        self.__data: dict = {}
        for idx, wav in enumerate(self.splitWavs):
            W: object = WavIn(wav)
            self.data[idx]: list = [W, W.wavArray]

    def stitchWavs(self) -> None:

        self.__stitchedWavs: list = []
        for data in self.data.values():
            self.stitchedWavs.extend(data[1])

    def connectWavs(self) -> None:
        
        self.collectWavs()
        self.parseWavs()
        self.stitchWavs()

        W: object = self.data[0][0]
        W.signal: bytes = np.array(self.stitchedWavs).tobytes()
        WavOut(filename=f'{self.root}/{self.filename}.wav', data=W).write()