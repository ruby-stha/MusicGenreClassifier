# MusicGenreClassifier
Project conducted during the junior year of Under Graduate Degree.

In this project, a stepping stone for automatic music genre categorization of vast number of music files available in digital form online or offline has been developed. Out of the various techniques of music genre recognition, content based technique has been used to automatically label the particular user uploaded song into one of five distinct genres: Classical, Pop, Metal, Jazz, and Blues. Digital signal processing techniques of Fast Fourier Transform and Mel-Frequency Cepstral Coefficients have been used to generate feature values of feature vector, which is then fed into the classifier developed using Support Vector Machine, in order to classify user input song. The training and testing of the system has been performed successfully obtaining an accuracy of 74.0%, which is significant in the field of music analysis. Training has been carried out using 80 music clips of each of the five genres, and testing, using 20 music clips of each of the five genres. GTZAN Music Dataset, a popular Western music dataset prepared for music analysis, has been used during training and testing; hence, this system works well only with Western music files. The system has been implemented with two graphical user interfaces: one for admin (training and testing) and another for user (uploading music file and finding genre) using Python programming language and Flask framework. 

Dataset Taken From: http://marsyasweb.appspot.com/download/data_sets/ (Download the GTZAN genre collection)

Code: In Music Genre Classification-Code Directory.

Suggestions to improve the project will be highly appreciated.
