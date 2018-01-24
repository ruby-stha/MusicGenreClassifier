#for file upload

import os
from flask import Flask, redirect, request, url_for, render_template
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile
from scipy import fft
from python_speech_features import mfcc
import TrainClassifier
import MusicFeatureCollection, MainServices
import pickle
import genreSpecgram

UPLOAD_FOLDER = 'D:\\m-test-files'
ALLOWED_EXTENSIONS = {'mp3', 'au'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/')
def root_url():
   return redirect(url_for("start"))

@app.route('/start/')
def start():
    # return render_template('test.html')
    return render_template('dashboard.html')

@app.route('/about_AMGC/')
def about_AMGC():
    return render_template('about.html')

@app.route('/userPanel/')
def userPanel():
    return render_template('userPanel.html')

@app.route('/computeFeatures/')
def computeFeatures():
    MusicFeatureCollection.computeFeatures("train")
    computeMessage="Features Computed! Success."
    return render_template('test.html', computeMessage=computeMessage)

# @app.route('/getFeatures/')
# def getFeatures():
#     MusicFeatureCollection.getFeatures("train")
#     getMmessage = "Features Received! Success."
#     return render_template('test.html', getMmessage=getMmessage)

@app.route('/train/')
def train():
      TrainClassifier.train()
      trainMessage="Training Completed! Success."
      return render_template('test.html', trainMessage=trainMessage)


@app.route('/test/')
def test():
      confusion_m, accuracy=TrainClassifier.test()
      testMessage="Testing Completed! Success."
      return render_template('test.html', testMessage=testMessage, confusion_m=confusion_m, accuracy=accuracy*100, genres=MainServices.CHOSEN_GENRES, length=len(MainServices.CHOSEN_GENRES))

@app.route('/analysis/')
def analysis():
    genre=MainServices.CHOSEN_GENRES
    genreSpecgram.index()
    return render_template('specgrams.html', genre=genre)

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        print (request.files)
        if 'music-file' not in request.files:
            print ('No file part')
            return render_template('test.html')
        mFile = request.files['music-file']
        if mFile.filename == '':
            print ('No selected file')
            return render_template('test.html')
        else:
            MainServices.clean_dir(MainServices.ROOT_DIR+"\\static\\temp\\user")
            filename = secure_filename(mFile.filename)
            print(filename)
            exact=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            mFile.save(exact)
            # test.export(app.config['UPLOAD_FOLDER'] + "\\" + filename + ".wav", format="wav")
            print (exact)
            sample_rate, musicData = scipy.io.wavfile.read(exact)
            convert_16_bit = float(2 ** 15)
            musicData = musicData / convert_16_bit

            #Signal
            plt.figure(0)
            plt.plot(np.array(range(1,musicData.shape[0]+1,1)),musicData)
            plotFig("Sample Points", "Amplitude values (normalized between -1 to 1)","Amplitude Vs Sample Point Plot", "signal")

            #Spectrogram
            plt.figure(1)
            sp=MainServices.make_specgram(exact)
            plotFig("Time(s)","Frequency (Hz)","Spectrogram", "userFileSpecgram")

            #FFT
            mData = np.array(musicData[:2048])
            win_musicData = mData * MainServices.get_window(len(mData))
            fft_feature = fft(win_musicData)
            abs_fft=abs(fft_feature)
            plt.figure(2)
            plt.plot(np.array(range(1,mData.shape[0]+1,1)),abs_fft)
            plotFig("Sample Points","Absolute Frequency Component","Sample Point Vs Frequency Component", "FFTPlot")

            #MFCC
            ceps = mfcc(musicData, samplerate=sample_rate, preemph=0)
            plt.figure(3)
            individual_feature=[]
            individual_feature = np.concatenate((np.array(abs_fft), individual_feature), axis=0)
            for val in ceps[:2992]:
                plt.plot(np.array(range(13)), val)
                individual_feature = np.concatenate((np.array(val), individual_feature), axis=0)
            plotFig("Coefficient Number", "MFCC","MFCC Plot Considering 13 Coefficients as X-Components", "MFCCPlot")

            t_data = pickle.load(open(MainServices.ROOT_DIR + '\\classifier.pkl', 'rb'))
            val=t_data.predict(np.asanyarray(individual_feature))

            return val[0]
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
         # return redirect(url_for('success',name=user))
    else:
         return redirect(request.url)

@app.route('/uploaded_file/<filename>')
def uploaded_file(filename):
    return 'welcome %s' % filename

def plotFig(x,y,title,filename):
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.savefig(MainServices.ROOT_DIR + "\\static\\temp\\user\\"+filename+".png")

if __name__ == '__main__':
    app.run()
