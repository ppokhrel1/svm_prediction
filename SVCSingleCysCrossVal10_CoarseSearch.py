# coding: utf-8

import numpy as np
import pandas as pd
import pickle as pk
import math
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import BaggingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score, precision_score, confusion_matrix, recall_score, f1_score, auc, matthews_corrcoef

from calculate_pssm import *
# read the training data file
#train_df = pd.read_csv('singlecys_window_9_4120_uniprot_cutoff25_Ran_10_Perc.txt', header=None)

# column 0 is class, 1 represents disulfide bonding exist whereas -1 represents disulfide does not exist
#train = train_df.as_matrix()
X, y = training_sample()
#y = train[:,0]
#X = train[:,1:]

#clf = BaggingClassifier(n_estimators=1000, n_jobs=-1)
scaler = StandardScaler()
X = scaler.fit_transform(X)
#C_range = np.logspace(-5,15,num=11,base=2.0)
#gamma_range = np.logspace(-15,3,num=10,base=2.0)
c_range = np.linspace(-5,15,num=11)
#c_range = np.linspace(1, 5, num = 17 )
C_range = [math.pow(2,i) for i in c_range]
g_range = np.linspace(-15, 3, num=10 )
gamma_range = [math.pow(2,j) for j in g_range]
print(C_range)
print(gamma_range)
param_grid = dict(gamma=gamma_range, C=C_range)
grid = GridSearchCV(SVC(), param_grid=param_grid, cv=10, n_jobs= -1 )
grid.fit(X,y)
print("The best parameters are %s with a score of %0.4f"% (grid.best_params_, grid.best_score_))

#clf = svm.SVC()
#predicted = cross_val_predict(clf, X, y, cv=10)

#confusion = confusion_matrix(y, predicted)
#print(confusion)
#TP = confusion[1, 1]
#TN = confusion[0, 0]
#FP = confusion[0, 1]
#FN = confusion[1, 0]
# Specificity
#SPE_cla = (TN/float(TN+FP))

# False Positive Rate
#FPR = (FP/float(TN+FP))

#False Negative Rate (Miss Rate)
#FNR = (FN/float(FN+TP))

#Balanced Accuracy
#ACC_Bal = 0.5*((TP/float(TP+FN))+(TN/float(TN+FP)))

# compute MCC
#MCC_cla = matthews_corrcoef(y, predicted)
#F1_cla = f1_score(y, predicted)
#PREC_cla = precision_score(y, predicted)
#REC_cla = recall_score(y, predicted)
#Accuracy_cla = accuracy_score(y, predicted)
#print('TP = ', TP)
#print('TN = ', TN)
#print('FP = ', FP)
#print('FN = ', FN)
#print('Recall/Sensitivity = %.5f' %REC_cla)
#print('Specificity = %.5f' %SPE_cla)
#print('Accuracy_Balanced = %.5f' %ACC_Bal)
#print('Overall_Accuracy = %.5f' %Accuracy_cla)
#print('FPR_bag = %.5f' %FPR)
#print('FNR_bag = %.5f' %FNR)
#print('Precision = %.5f' %PREC_cla)
#print('F1 = %.5f' % F1_cla)
#print('MCC = %.5f' % MCC_cla)









