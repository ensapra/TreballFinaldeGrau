import os
import cv2
import csv
import math
import asyncio
import imutils
import Augmentor
import numpy as np
import pandas as pd
from multiprocessing import Process, Queue
from tqdm.notebook import tqdm
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn.cluster import MiniBatchKMeans
from sklearn.neural_network import MLPClassifier

class Processor:
    def __init__(self,kmeans):
        self._kmeans = kmeans
        
    def __call__(self,filename):
        sift = cv2.SIFT_create()
        NoneType = type(None)
        img = cv2.imread(filename)
        kp, des = sift.detectAndCompute(img, None)
        histo = np.zeros(k)
        nkp = np.size(kp)
        if(type(des) != NoneType):
            for d in des:
                idx =  self._kmeans.predict([d])
                histo[idx] += 1/nkp # Because we need normalized histograms, I prefere to add 1/nkp directly
        return histo