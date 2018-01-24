import matplotlib.pyplot as plt
import os
import math
import scipy.io.wavfile

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GENRE_WAV="D:\\MiniProject\\genres_wav"
GENRE_WAV_ALL="D:\\MiniProject\\genres_wav_all"
GTZAN_DIR="C:\\Users\\Ruby\\Desktop\\genres"
ALL_GENRES=['classical', 'pop', 'metal', 'jazz', 'rock', 'disco', 'country', 'hiphop', 'reggae', 'blues']
CHOSEN_GENRES=['classical', 'pop', 'metal', 'blues', 'jazz']

def clean_dir(dir):
    for f in os.listdir(dir):
        if (os.path.isdir(dir+"\\"+f)==False):
            os.remove(dir+"\\"+f)

def make_specgram(file):
    convert_16_bit = float(2 ** 15)
    sample_rate, X = scipy.io.wavfile.read(file)
    X = X / convert_16_bit
    plt.specgram(X, Fs=sample_rate)
    return plt

def get_window(N):
    window=[]
    for i in range(N):
        intermediate=(2*math.pi*i)/(N-1)
        val=0.54-0.46*math.cos(intermediate)
        window.append(val)
    return window

# def make_fft(file):
#     convert_16_bit = float(2 ** 15)
#     sample_rate, X = scipy.io.wavfile.read(file)
#     X = X / convert_16_bit
#     X = np.array(X[:1000])
#     fft_feature = fft(X)
#     print(len(fft_feature))
#     plt.plot(np.array(range(1,len(fft_feature)+1,1)), fft_feature)
#     plt.xlabel("Sample Points [1000 Points]")
#     plt.ylabel("FFT Values")
#     return plt

def save_figure(file, file_name, dir):
    f = dir+file_name+".png"
    file.savefig(f, dpi=100)
