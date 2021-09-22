import wave
import pandas as pd
import numpy as np
from src.base import Reader, Writer

class WavIn(Reader):

    def __init__(self, filename: str):

        self.__filename: str = filename
        self.__data: object = wave.open(self.filename, 'rb')
        self.processWavData()

    def __copy__(self):
        return WavIn(filename=self.filename)

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def data(self) -> object:
        return self.__data

    @property
    def channels(self) -> int:
        return self.__channels

    @property
    def sampleRate(self) -> float:
        return self.__sampleRate

    @sampleRate.setter
    def sampleRate(self, sampleRate: float):
        self.__sampleRate: float = sampleRate

    @property
    def sampleWidth(self) -> int:
        return self.__sampleWidth

    @property
    def sampleNum(self) -> int:
        return self.__sampleNum

    @property
    def signal(self) -> bytes:
        return self.__signal

    @signal.setter
    def signal(self, signal: bytes):
        self.__signal: bytes = signal

    @property
    def wavArray(self) -> list:
        return np.frombuffer(self.signal, dtype='float32')

    def processWavData(self) -> None:

        self.__channels: int = self.data.getnchannels()
        self.__sampleRate: float = self.data.getframerate()
        self.__sampleWidth: int = self.data.getsampwidth()
        self.__sampleNum: int = self.data.getnframes()
        self.__signal: bytes = self.data.readframes(-1)

    def readFrames(self, save: bool = True, output: str = None) -> pd.DataFrame:

        path: str = f'{self.filename[:-4]}_frames.csv'
        data: pd.DataFrame = pd.DataFrame(self.wavArray, columns=['frames(amplitude)'])
        if save:
            if output:
                path: str = output + path 

            data.to_csv(path)

        return data

        
class WavOut(Writer):

    def __init__(self, filename: str, data: object):

        self.__filename: str = filename
        self.__data: object = data
        self.__out: object = wave.open(self.filename, 'wb')

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def data(self) -> object:
        return self.__data

    @property
    def out(self) -> object:
        return self.__out

    @property
    def channels(self) -> int:
        return self.data.channels

    @property
    def sampleRate(self) -> float:
        return self.data.sampleRate

    @property
    def sampleWidth(self) -> int:
        return self.data.sampleWidth

    @property
    def sampleNum(self) -> int:
        return self.data.sampleNum

    @property
    def signal(self) -> bytes:
        return self.data.signal

    def write(self):

        self.out.setnchannels(self.channels)
        self.out.setsampwidth(self.sampleWidth)
        self.out.setframerate(self.sampleRate)
        self.out.writeframes(self.signal)