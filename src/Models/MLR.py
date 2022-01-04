from collections import Counter
from numpy import mean
from numpy import std
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

class MLR:
    pass
    "Multinomial Logistic Regression"

    def __init__(self):
        # define the multinomial logistic regression model
        self.model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
        #test dataset
        self.X, self.y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)
        # summarize the dataset
        print("data size: ", self.X.shape, self.y.shape)
        print("examples per class: ", Counter(self.y))

    def evaluate(self):
        # define the model evaluation procedure
        cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
        # evaluate the model
        n_scores = cross_val_score(self.model, self.X, self.y, scoring='accuracy', cv=cv, n_jobs=-1)
        # report the model performance
        print('Mean Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))

    # make a prediction with a multinomial logistic regression model
    def predict(self,):
        self.model.fit(self.X, self.y)
        # define a single row of input data
        row = [1.89149379, -0.39847585, 1.63856893, 0.01647165, 1.51892395, -3.52651223, 1.80998823, 0.58810926, -0.02542177, -0.52835426]
        # predict the class label
        yhat = self.model.predict([row])
        # summarize the predicted class
        print('Predicted Class: %d' % yhat[0])



#
# # define dataset
# X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)
# # define the multinomial logistic regression model
# model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
# # fit the model on the whole dataset
# model.fit(X, y)
# # define a single row of input data
# row = [1.89149379, -0.39847585, 1.63856893, 0.01647165, 1.51892395, -3.52651223, 1.80998823, 0.58810926, -0.02542177, -0.52835426]
# # predict the class label
# yhat = model.predict([row])
# # summarize the predicted class
# print('Predicted Class: %d' % yhat[0])
