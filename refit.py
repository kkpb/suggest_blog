# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm, grid_search
from sklearn.externals import joblib
import os
import numpy as np

import text_listing as tl

train_list = os.listdir("train")
text_list = reduce(lambda a,b : a+b, map(lambda n : tl.text_list_from_json('train/'+n, 'entry'), train_list))
text_cat =map(lambda n : int(n), reduce(lambda a,b : a+b, map(lambda n : tl.text_list_from_json('train/'+n, 'useful'), train_list)))

vectorizer = TfidfVectorizer(analyzer=tl.make_noun_list, min_df=1)
text_v = vectorizer.fit_transform(text_list)

parameters = {'kernel' : ('linear', 'rbf'), 'C' : np.logspace(-4, 4, 10), 'gamma' : np.logspace(-4, 4, 10)}
clf = grid_search. GridSearchCV(svm.SVC(), parameters, n_jobs = -1)

clf.fit(text_v.todense(), text_cat)

print text_cat
print text_v.toarray()
print len(vectorizer.get_feature_names())
os.system('rm -rf tmp_v/*')
os.system('rm -rf tmp_c/*')
joblib.dump(vectorizer, "tmp_v/vec.pkl")
joblib.dump(clf, "tmp_c/clf.pkl")
