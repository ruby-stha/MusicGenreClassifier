from flask import Flask, redirect, url_for
import random
import MainServices

app=Flask(__name__)

@app.route("/")
def index():
    MainServices.clean_dir(MainServices.ROOT_DIR + "\\static\\temp")
    for genre in MainServices.CHOSEN_GENRES:
        forAnalysis(genre)

@app.route("/test")
def test():
    return "hello"

def forAnalysis(genre):
    newdir = MainServices.GENRE_WAV_ALL+"\\"+genre
    n=0
    for x in random.sample(range(0,99), 3):
        print(x)
        if (x < 10):
            file = "0000" + str(x)
        else:
            file = "000" + str(x)
        file=genre+file
        filename=genre+str(n)
        specgram=MainServices.make_specgram(newdir+"\\"+file+".wav")
        MainServices.save_figure(specgram,filename, MainServices.ROOT_DIR+"\\static\\temp\\")
        n = n + 1

if __name__=="__main__":
    app.run()