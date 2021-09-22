from src.wavIO import WavIn, WavOut
from src.wavProcessor import Effects
from src.wavSplitter import WavSplitter

class Run:

    def __init__(self, input_file: str, output_dir: str, 
                       factors: list = [0.5, 2], split: int = 10):

        self.__input_file: str = input_file
        self.__output_dir: str = output_dir
        self.__factors: list = factors
        self.__split: int = split

    @property
    def input_file(self) -> str:
        return self.__input_file

    @property
    def output_dir(self) -> str:
        return self.__output_dir

    @property
    def factors(self) -> list:
        return self.__factors

    @property
    def split(self) -> int:
        return self.__split

    
    def generate_csv(self) -> None:

        W: object = WavIn(filename=self.input_file)
        W.readFrames(output=self.output_dir)

    def generate_effects(self, reverse: bool = True, time_shift: bool = True) -> None:

        if reverse and time_shift == False:
            return

        E: object = Effects(root=self.output_dir, filename=self.input_file)

        if reverse:
            E.reverse()
        if time_shift:
            for f in factor:
                E.timeStretch(factor=f)

    def generate_splits(self, split: bool = True) -> None:

        if split == False:
            return

        S: object = WavSplitter(root=self.output_dir, filename=self.input_file)
        S.splitWavsBySeconds(seconds=self.split)