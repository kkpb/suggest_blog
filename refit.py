# -*- coding: utf-8 -*-

from sklearn import svm, grid_search
from sklearn.externals import joblib
import os
import numpy as np

import text_listing as tl

train_list = os.listdir("train")
text_list = reduce(lambda a,b : a+b, map(lambda n : tl.text_list_from_json('train/'+n, 'entry'), train_list))
text_cat =map(lambda n : int(n), reduce(lambda a,b : a+b, map(lambda n : tl.text_list_from_json('train/'+n, 'useful'), train_list)))

vectorizer = joblib.load("vec/vec.pkl")
text_v = vectorizer.transform(text_list)

parameters = {'kernel' : ('linear', 'rbf'), 'C' : np.logspace(-4, 4, 10), 'gamma' : np.logspace(-4, 4, 10)}
clf = grid_search. GridSearchCV(svm.SVC(), parameters, n_jobs = -1)
clf.fit(text_v.todense(), text_cat)

os.system('rm -rf tmp/*')
joblib.dump(clf, "tmp/clf.pkl")
