Title: OpenCV Cascade Classifier training
Date: 2015-12-07 05:21
Modified: 2015-12-07 05:21
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) OpenCV Cascade Classifier training


### Tutorial
http://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html
http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html


http://answers.opencv.org/question/7141/about-traincascade-paremeters-samples-and-other/

### 一些設定posNum要注意的問題
http://stackoverflow.com/questions/10863560/haar-training-opencv-assertion-failed

**vec-file has to contain >= (numPos + (numStages-1) x (1 - minHitRate) x numPos) + S**
S: count of samples from vec-file that can be recognized as background right away (num bg image in background file descriptor)

### Other tips
http://answers.opencv.org/question/19117/using-opencv_traincascade-and-speed-up-the-processing/

1. 背景不要用白的
2. HAAS會比LBP慢很多

