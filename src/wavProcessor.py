import numpy as np
from wavIO import WavIn, WavOut
from base import Processor

class Effects(Processor):

    def __init__(self, root: str, filename: str):

        self.__root: str = root
        self.__filename: str = filename

    @property
    def root(self) -> str:
        return self.__root

    @property
    def filename(self) -> str:
        return self.__filename


    def reverse(self) -> None:

        wav: object = WavIn(self.filename)

        signal: list = wav.wavArray()
        signal: list = signal[::-1]
        signal: bytes = signal.tobytes()
        wav.signal: bytes = signal

        WavOut(filename=f'{self.root}/{self.filename}_reversed.wav', data=wav)

    def timeStretch(self, factor: float) -> None:

        wav: object = WavIn(self.filename)

        wav.sampleRate: float = wav.sampleRate / factor

        WavOut(filename=f"{self.root}/{self.filename}_{factor}__shift.wav", data=wav)