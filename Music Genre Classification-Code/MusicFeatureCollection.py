import scipy.io.wavfile
import numpy as np
from scipy import fft
import os
import MainServices
from python_speech_features import mfcc

FFT_dir="D:\\MiniProject\\genres_fft_csv"
MFCC_dir="D:\\MiniProject\\genres_mfcc_csv"

mfccs=[]


def computeFFT(file, genre, key):
    sample_rate, musicData = scipy.io.wavfile.read(file)
    convert_16_bit = float(2 ** 15)
    musicData=musicData/convert_16_bit
    musicData=np.array(musicData[:2048])
    win_musicData=musicData*MainServices.get_window(len(musicData))
    fft_feature=fft(win_musicData)
    base_filename, ext=os.path.splitext(file)
    base_filename=base_filename.rsplit("\\",1)[1]
    new_filename=base_filename+".csv"
    save(FFT_dir+"\\"+key, fft_feature, new_filename, genre, "FFT")


def read_fft(key):
    ffts=[]
    labels=[]
    for genre in MainServices.CHOSEN_GENRES:
        fftDir=FFT_dir+"\\"+key+"\\"+genre
        for file in os.listdir(fftDir):
            fft_values=scipy.load(fftDir+"\\"+file)
            fft_values=abs(fft_values)
            ffts.append(fft_values)
            labels.append(genre)
    return [ffts, labels]

def save(dir, fft_feature, file, genre, key):
    dest=dir+"\\"+genre+"\\"+file
    np.save(dest, fft_feature)
    print("%s file %s of genre %s saved." % (key, file, genre))


def computeMFCC(file, genre, key):
    sample_rate, musicData = scipy.io.wavfile.read(file)
    convert_16_bit = float(2 ** 15)
    musicData = musicData / convert_16_bit
    musicData = np.array(musicData)
    ceps = mfcc(musicData, samplerate=sample_rate,preemph=0)
    # mfcc_feature=np.mean(ceps, axis=0)
    base_filename, ext = os.path.splitext(file)
    base_filename=base_filename.rsplit("\\",1)[1]
    new_filename = base_filename + ".csv"
    # save(MFCC_dir+"\\"+key,mfcc_feature, new_filename, genre, "MFCC")
    save(MFCC_dir+"\\"+key,ceps, new_filename, genre, "MFCC")


def read_mfcc(key):
    mfccs=[]
    for genre in MainServices.CHOSEN_GENRES:
        mfccDir=MFCC_dir+"\\"+key+"\\"+genre
        for file in os.listdir(mfccDir):
            mfcc_values=scipy.load(mfccDir+"\\"+file)
            #mfcc_values=np.pad(mfcc_values, (0,987), 'constant')
            mfccs.append(mfcc_values)
    return mfccs

def computeFeatures(key):
    for genre in MainServices.CHOSEN_GENRES:
        MainServices.clean_dir(FFT_dir+"\\"+key+"\\"+genre)
        MainServices.clean_dir(MFCC_dir+"\\"+key+"\\"+genre)
        dir=MainServices.GENRE_WAV+"\\"+key+"\\"+genre
        for f in os.listdir(dir):
            computeFFT(dir+"\\"+f,genre, key)
            computeMFCC(dir+"\\"+f,genre, key)

def readFeatures(key):
    fft_and_label=read_fft(key)
    return fft_and_label[0], read_mfcc(key), fft_and_label[1]

def getFeatures(key):
    features=[]
    ffts, mfccs, labels=readFeatures(key)
    for n in range(len(ffts)):
        individual_feature=[]
        individual_feature = np.concatenate((np.array(ffts[n]), individual_feature), axis=0)
        for val in mfccs[n][:2992]:
            individual_feature = np.concatenate((np.array(val), individual_feature), axis=0)
        features.append(individual_feature)
    print("Feature To Use....")
    print(features)
    print(labels)
    print(len(features),len(labels))
    return [features, labels]