import wave
import pandas as pd
import numpy as np
from base import Reader, Writer

class WavIn(Reader):

    def __init__(self, filename: str):

        self.__filename: str = filename
        self.__data: object = wave.open(self.filename, 'rb')
        self.readSignal()

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
        return self.data.getnchannels()

    @property
    def sampleRate(self) -> float:
        return self.data.getframerate()

    @property
    def sampleWidth(self) -> int:
        return self.data.getsampwidth()

    @property
    def sampleNum(self) -> int:
        return self.data.getnframes()

    @property
    def signal(self) -> bytes:
        return self.__signal

    @signal.setter
    def signal(self, signal: bytes):
        self.__signal: bytes = signal

    @property
    def wavArray(self) -> list:
        return np.frombuffer(self.signal, dtype='float32')

    def readSignal(self) -> None:

        self.__signal: bytes = self.data.readframes(-1)

    def readFrames(self, save: bool = True) -> pd.DataFrame:

        data: pd.DataFrames = pd.DataFrame(self.wavArray, columns=['frames(amplitude)'])
        if save:
            data.to_csv(f'{self.filename}_frames.csv')

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