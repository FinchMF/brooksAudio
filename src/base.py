class Wave(object):

    @property
    def filename(self) -> str:
        raise NotImplementedError()

    @property
    def channels(self) -> int:
        raise NotImplementedError()

    @property
    def sampleRate(self) -> float:
        raise NotImplementedError()

    @property
    def sampleWidth(self) -> int:
        raise NotImplementedError()

    @property
    def sampleNum(self) -> int:
        raise NotImplementedError()

    @property
    def data(self) -> object:
        raise NotImplementedError()

    @property
    def signal(self) -> bytes:
        raise NotImplementedError()


class Reader(Wave):

    @property
    def wavArray(self) -> list:
        raise NotImplementedError()
    
    def readFrames(self) -> object:
        raise NotImplementedError()

    def readSignal(self) -> None:
        raise NotImplementedError()

    def __copy__(self):
        raise NotImplementedError()


class Writer(Wave):

    def write(self) -> None:
        raise NotImplementedError()


class Splitter(object):

    @property
    def root(self) -> str:
        raise NotImplementedError()

    @property
    def filename(self) -> str:
        raise NotImplementedError()


    def intervals(self, durations_frames: float, bins: int) -> list[float]:
        raise NotImplementedError()

    def divideTracks(self, duration_seconds: float) -> list:
        raise NotImplementedError()

    def sampleDivisions(self, divisions: list, wav: object) -> None:
        raise NotImplementedError()

    def splitWavsBySeconds(self, seconds: int) -> None:
        raise NotImplementedError()


class Processor(object):

    def reverse(self) -> None:
        raise NotImplementedError()

    def timeStretch(self) -> None:
        raise NotImplementedError()

    def reorder(self) -> None:
        raise NotImplementedError()