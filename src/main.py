import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from ast import literal_eval

from sklearn.preprocessing import MultiLabelBinarizer

from Models.MLR import MLR


from statsmodels.miscmodels.ordinal_model import OrderedModel # pip install git+https://github.com/statsmodels/statsmodels

MODEL = 'ordinal' #'multinomial'


def main():
    print("Prepare Data . . .")
    df_csv = pd.read_csv('res/largeDataCategorical.csv')
    print(df_csv)

    X = df_csv['X']
    Y = df_csv['Y']

    X_new = []
    for ar in X:
        st = ar[1:-1]
        arr = st.split(',')
        arr = list(map(float, arr))
        X_new.append(arr)

    print("Feature Selection . . .")

    print("\nMultinomial Logistic Regression . . .")

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X_new, Y, test_size=0.20, random_state=5)

    if MODEL == 'ordinal':
        X_train = pd.DataFrame(X_train, dtype="object")
        y_train = pd.DataFrame(y_train, dtype="category")

        ordinalModel = OrderedModel(endog=y_train, exog=X_train, distr='logit')
        res_log = ordinalModel.fit(method='bfgs', disp=True)
        res_log.summary()
        y_pred = res_log.predict(X_test)
        print('Accuracy: {:.2f}'.format(accuracy_score(y_test, y_pred)))
        print('Error rate: {:.2f}'.format(1 - accuracy_score(y_test, y_pred)))

    if MODEL == 'multinomial':
        model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1500)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print('Accuracy: {:.2f}'.format(accuracy_score(y_test, y_pred)))
        print('Error rate: {:.2f}'.format(1 - accuracy_score(y_test, y_pred)))

    # mlr = MLR()
    # mlr.train(X, Y)
    # mlr.evaluate()
    # mlr.predict()

    print("\nOther Methods . . .")


if __name__ == "__main__":
    main()
