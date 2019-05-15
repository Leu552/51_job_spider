import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.datasets.samples_generator import make_classification
from sklearn.neighbors import KNeighborsClassifier


# iris = datasets.load_iris()
# # 属性
# iris_X = iris.data
# # 分类
# iris_y = iris.target

# print(iris_X[:2,:])
# print(iris_y)

# X_train,X_test,y_train,y_test = train_test_split(
#     iris_X,iris_y,test_size=0.3)

# X,y = datasets.make_regression(n_samples=100, n_features=1, n_targets=1, noise=1)
# plt.scatter(X,y)
# plt.show()

# lod_data = datasets.load_boston()
# data_X = lod_data.data
# data_y = lod_data.target
#
# model = LinearRegression()
# model.fit(data_X,data_y)

# LinearRegression的参数
# print(model.coef_) # X
# print(model.intercept_) #Y交点

# print(model.get_params()) #定义的参数

# print(model.score(data_X,data_y)) # R
#
# a = np.array([[10,2.7,3.6],
#               [-100,5,-2],
#               [120,20,40]],dtype=np.float64)

# print(a)
# print(preprocessing.scale(a))

# X,y = make_classification(n_samples=300,n_features=2, n_redundant=0,n_informative=2,random_state=22,n_clusters_per_class=1,scale=100)
# plt.scatter(X[:,0],X[:,1],c=y)
# plt.show()
# X = preprocessing.scale(X)

# X_train,X_test,y_train,y_test = train_test_split(
#     X,y,test_size=0.8)
# clf = SVC()
# clf.fit(X_train,y_train)
# print(clf.score(X_train,y_train))

# iris = datasets.load_iris()
# X = iris.data
# y = iris.target

#
# X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=4)
# knn = KNeighborsClassifier(n_neighbors=3)
# scores = cross_val_score(knn,X,y,cv=5,scoring='accuracy')
# # knn.fit(X_train,y_train)
# # y_predict = knn.predict(X_test)
# # print(knn.score(X_test,y_test))
# print(scores.mean())
# k_range = range(1,31)
# k_score = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     loss = -cross_val_score(knn,X,y,cv=10,scoring='neg_mean_squared_error') #for regression
#     # scores = cross_val_score(knn,X,y,cv=10,scoring='accuracy') #for classification
#     k_score.append(loss.mean())
#
# plt.plot(k_range,k_score)
# plt.xlabel('KNN里k的值')
# plt.ylabel('该k时准确度')
# plt.show()

from sklearn.model_selection import *
from sklearn.datasets import *
# digits = load_digits()
# X = digits.data
# y = digits.target
# param_range = np.logspace(-6,-2.3,5)
#
# train_loss, test_loss = validation_curve(
#     SVC(),X,y,param_name='gamma',param_range=param_range,cv=10,scoring='neg_mean_squared_error',
# )
# train_loss_mean = -np.mean(train_loss,axis=1)
# test_loss_mean = -np.mean(test_loss,axis=1)
#
# plt.plot(param_range,train_loss_mean,'o-',color='r',label='Training')
# plt.plot(param_range,test_loss_mean,'o-',color='g',label='Cross')
#
# plt.xlabel('gamma')
# plt.ylabel('Loss')
# plt.legend(loc='best')
# plt.show()

from sklearn import svm
clf = svm.SVC()
iris = load_iris()
X,y = iris.data,iris.target
clf.fit(X,y)
# 分类器

import pickle
# with open('clf.pickle','wb') as f:
#     pickle.dump(clf,f)

# with open('clf.pickle','rb') as f:
#     clf2 = pickle.load(f)
#     print(clf2.predict(X[0:2]))

# 保存model
from sklearn.externals import joblib
joblib.dump(clf,'clf.pkl')
clf3 = joblib.load('clf.pkl')
print(clf3.predict(X[0:1]))