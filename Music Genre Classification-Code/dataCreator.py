"""GTZAN dataset was in .au format. Hence, the following code block was used to convert the .au format file into .wav format
file so that those files could be used in scipy.io.wavefile.read method, which is the method intended to be used during
audio feature extraction"""

import os
import MainServices
from pydub import AudioSegment


for genre in MainServices.ALL_GENRES:
    dir=MainServices.GTZAN_DIR+"\\"+genre
    newdir=MainServices.GENRE_WAV_ALL+"\\"+genre
    for filename in os.listdir(dir):
        test = AudioSegment.from_file(dir+"\\"+filename, format="au")
        name,num,ext=filename.rsplit(".")
        print(name,num,ext)
        test.export(newdir+"\\"+ name+num +".wav", format="wav")
