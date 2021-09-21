import wave
from wavIO import WavIn, WavOut
from base import Splitter


class WavSplitter(Splitter):
    
    def __init__(self, root: str, filename: str):

        self.__root: str = root
        self.__filename: str = filename

    @property
    def root(self) -> str:
        return self.__root

    @property
    def filename(self) -> str:
        return self.__filename

    
    def intervals(self, duration_frames: float, bins: int) -> list[float]:

        bin_duration: int = int(duration_frames / bins)

        return [(i * bin_duration, (i + 1) * bin_duration) for i in range(int(bins))]

    def divideTracks(self, duration_seconds: float) -> list:

        wav: object = WavIn(self.filename)
        duration: float = round(wav.sampleNum / wav.sampleRate, 2)

        needed_bin: int = int(duration / duration_seconds)

        divider: list = self.intervals(duration_frames=float(wav.sampleNum), bins=needed_bin)

        return [divider, wav]

    def sampleDivisions(self, divider: list, wav: object) -> None:

        for idx, div in enumerate(divider):

            W: object = wav.__copy__()
            fname: str = f"{self.root}/wav_{idx}.wav"

            signal: list = W.wavArray[div[0]:div[1]]
            signal: bytes = signal.tobytes()
            W.signal = signal
            WavOut(fname, W).write()
            del W

    def splitWavsBySeconds(self, seconds: int) -> None:

        divider, wav = self.divideTracks(duration_seconds=seconds)
        self.sampleDivisions(divider=divider, wav=wav)