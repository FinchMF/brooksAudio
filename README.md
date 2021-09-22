# brooksAudio

## How to install and run

    pip install -r requirements.txt

    bash run.sh chooseYourAudio.wav

## Current Output

While it is configurable, the current state of the program is rather crude. By running the bash command, you should see this std out:

    2021-09-22 01:03:02 [INFO] brooksAudio - Generating csv...
    2021-09-22 01:03:24 [INFO] brooksAudio - ...csv saved in output
    2021-09-22 01:03:24 [INFO] brooksAudio - Beach_House_Space_Song.wav reversed and saved in output
    2021-09-22 01:03:24 [INFO] brooksAudio - Beach_House_Space_Song.wav time shifted at 2 and saved in output
    2021-09-22 01:03:25 [INFO] brooksAudio - Beach_House_Space_Song.wav split into equal divisions of 10 and saved in output

- ***note: that it could take a few minutes depending on the duration of the wav file***
---


Then navigating to the **output** directory you will find a set of files. 

* csv of sample frames with amplitude
* reversed audio
* audio slowed to half speed
* the audio file split into equal sections all 10 seconds in length

Furher improvements to configurability forthcoming 