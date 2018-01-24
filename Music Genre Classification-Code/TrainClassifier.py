import MusicFeatureCollection
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn import svm
import pickle
import MainServices
from matplotlib import pylab


def train():
    print("Training..................")
    featureList=MusicFeatureCollection.getFeatures("train")
    features=featureList[0]
    labels=featureList[1]
    supportVM = svm.SVC(kernel='linear', C=100.0, probability=True)
    npa = np.asarray(features)
    npl = np.asarray(labels)
    data = supportVM.fit(npa, npl)
    pickle.dump(data, open(MainServices.ROOT_DIR+'\\classifier.pkl', 'wb'))
    print("Score (approx).......................")
    print(supportVM.predict_proba(npa))
    print ("success!")

def test():
    print("Testing....")
    result=[]
    count=0
    MusicFeatureCollection.computeFeatures("test")
    featureList = MusicFeatureCollection.getFeatures("test")
    features = featureList[0]
    labels = featureList[1]
    t_data = pickle.load(open(MainServices.ROOT_DIR + '\\classifier.pkl', 'rb'))
    for i in range(len(labels)):
        ans=t_data.predict(np.asanyarray(features[i]))[0]
        if ans==labels[i]:
            count=count+1
        result.append(ans)
    print(result)
    print(labels)
    accuracy=count/len(labels)
    cm=confusion_matrix(labels,result)
    print("confusion matrix:")
    print(cm)
    plot_confusion_matrix(cm, MainServices.CHOSEN_GENRES, "Confusion Matrix")
    print(count/len(labels))
    print("success!")
    return cm, accuracy


def plot_confusion_matrix(cm, genre_list, title):
    pylab.clf()
    pylab.matshow(cm, fignum=False, cmap='Blues',
                      vmin=0, vmax=20)
    ax = pylab.axes()
    ax.set_xticks(range(len(genre_list)))
    ax.set_xticklabels(genre_list)
    ax.xaxis.set_ticks_position("bottom")
    ax.set_yticks(range(len(genre_list)))
    ax.set_yticklabels(genre_list)
    pylab.title(title)
    pylab.colorbar()
    pylab.grid(False)
    pylab.xlabel('Predicted class')
    pylab.ylabel('True class')
    pylab.grid(False)
    pylab.show()
