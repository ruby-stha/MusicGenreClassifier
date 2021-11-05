# About Automatic Music Genre Classifier

## Project Summary

In this project, a stepping stone for automatic music genre categorization of vast number of music files available in digital form online or offline has been developed. Out of the various techniques of music genre recognition, content based technique has been used to automatically label the particular user uploaded song into one of five distinct genres: Classical, Pop, Metal, Jazz, and Blues. Digital signal processing techniques of Fast Fourier Transform and Mel-Frequency Cepstral Coefficients have been used to generate feature vector, which is then fed into the classifier developed using Support Vector Machine, in order to classify user input song. The training and testing of the system has been performed successfully obtaining an accuracy of 74.0%, which is significant in the field of music analysis. Training has been carried out using 80 music clips of each of the five genres, and testing, using 20 music clips of each of the five genres. GTZAN Music Dataset, a popular Western music dataset prepared for music analysis, has been used during training and testing; hence, this system works well only with Western music files. The system has been implemented with two graphical user interfaces: one for admin (training and testing) and another for user (uploading music file and finding genre) using Python programming language and Flask framework. 

## Software Modules Used

1. Scikit learn to implement machine learning algorithm.
2. Flask web microframework for web interface
3. Matplotlib for graphs generation
4. SimpleCV for image processing

## Data Source

Dataset Taken From: [Marsyas.info](http://marsyas.info/downloads/datasets.html) (Download the GTZAN genre collection)

## Result

Details have been mentioned in the Theoretical Document [here](https://github.com/ruby-stha/MusicGenreClassifier/blob/69365f36bf34c1647354b4832186286d181241e1/Theoretical%20Documentation%20on%20Automatic%20Music%20Genre%20Classifier.pdf).

## Conclusion

The system developed, Automatic Music Genre Classifier, that makes use of FFT and MFCC for feature extraction and SVM for classification has been successfully implemented using Python programming language and Flask Framework. An accuracy calculated as correct count/total count was found to be 74.0%.

## Recommendation

The accuracy can be increased above 74.0% by consideration of additional features such as beat (calculated with the use of FFT), pitch and a better algorithm over FFT for nonstationary music files, which is Discrete Wavelet Transform (DWT). Moreover, instead of using 30 seconds music files of GTZAN Music Dataset, more time duration of the music files can be used. 

Suggestions to improve the project will be highly appreciated.
