
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

#import numpy as np

#from sklearn import preprocessing

from sklearn import svm
from calculate_pssm import *
from sklearn import model_selection
from sklearn.model_selection import train_test_split

from sklearn.feature_selection import SelectFromModel

X, y = training_sample()

#scale and normalize data
#X = preprocessing.scale(X, axis= 0 )


#X = np.array(X)
#y = np.array(y)
#print(X)
#print (y)
print("Got all training data \n Now running training")
seed = 7
models = []
models.append(('SVM', svm.SVC(kernel="linear", C = 100 ) ) )
models.append(('MLP', MLPClassifier(solver='lbfgs', alpha=1e-5,
hidden_layer_sizes=(250,), random_state=1 ) )  )


results = []
names = []
scoring = 'accuracy'
for name, model in models:
    kfold = model_selection.KFold(n_splits= 5 , shuffle=False, random_state=seed)
    
    cv_results = model_selection.cross_val_score(model, X, y, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)


#from sklearn.svm import SVR

#clf = SVR(C=1.0)
#print( clf.fit(X, y))
