import sys
import argparse
import logging as log
from src.wavIO import WavIn, WavOut
from src.wavProcessor import Effects
from src.wavSplitter import WavSplitter

log.basicConfig(
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    level=log.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout,
)
logger = log.getLogger('brooksAudio')

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
        logger.info('Generating csv...')
        W: object = WavIn(filename=self.input_file)
        W.readFrames(output=self.output_dir)
        logger.info(f'...csv saved in {self.output_dir}')

    def generate_effects(self, reverse: bool = True, time_shift: bool = True) -> None:

        if reverse and time_shift == False:
            logger.info('No effects chosen')
            return

        E: object = Effects(root=self.output_dir, filename=self.input_file)

        if reverse:
            E.reverse()
            logger.info(f'{self.input_file} reversed and saved in {self.output_dir}')
        if time_shift:
            for f in self.factors:
                E.timeStretch(factor=f)
                logger.info(f'{self.input_file} time shifted at {f} and saved in {self.output_dir}')

    def generate_splits(self, split: bool = True) -> None:

        if split == False:
            logger.info('No audio splits')
            return

        S: object = WavSplitter(root=self.output_dir, filename=self.input_file)
        S.splitWavsBySeconds(seconds=self.split)
        logger.info(f'{self.input_file} split into equal divisions of {self.split} and saved in {self.output_dir}')


if __name__ == '__main__':

    parser: object = argparse.ArgumentParser()

    parser.add_argument('-i', '-audio_in', type=str, 
                      help='name of audio file to be analyzed and manipulated')
    parser.add_argument('-o', '-out_directory', type=str,
                      help='name of directory where generated files will be saved too')
    parser.add_argument('-f', '-factors', type=int, default=2,
                      help='sets the factors for time stretch algo')
    parser.add_argument('-s', '-split_second', type=int, default=10,
                      help='choose number of seconds to generate equal divisions of the audio wav')
    parser.add_argument('-t', '-time_stretch', type=bool, default=True,
                      help='choose whether to time strech audio wav or not')
    parser.add_argument('-sp', '-split', type=bool, default=True,
                      help='choose whether to split audio wav or not')
    parser.add_argument('-r', '-reverse', type=bool, default=True,
                      help='choose whether to reverse audio wav or not')
    
    args: object = parser.parse_args()

    R: object = Run(input_file=args.i,
                    output_dir=args.o,
                    factors=[args.f],
                    split=args.s)
    
    R.generate_csv()
    R.generate_effects(reverse=args.r, time_shift=args.t)
    R.generate_splits(split=args.sp)