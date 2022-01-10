import numpy
import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from ast import literal_eval

from sklearn.preprocessing import MultiLabelBinarizer

from Models.MLR import MLR

from statsmodels.miscmodels.ordinal_model import \
    OrderedModel  # pip install git+https://github.com/statsmodels/statsmodels

MODEL = 'ordinal'  # 'multinomial'


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

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X_new, Y, test_size=0.20,
                                                                                random_state=5)
    # Using ordinal logistic regression
    if MODEL == 'ordinal':
        '''
        # Put y_train in correct datatype
        y_train = y_train.to_numpy()
        for i in range(0, y_train.shape[0]):
            if y_train[i] == '[1.0, 0.0, 0.0, 0.0]':
                y_train[i] = 'a'
            if y_train[i] == '[0.0, 1.0, 0.0, 0.0]':
                y_train[i] = 'b'
            if y_train[i] == '[0.0, 0.0, 1.0, 0.0]':
                y_train[i] = 'c'
            if y_train[i] == '[0.0, 0.0, 0.0, 1.0]':
                y_train[i] = 'd'
        y_cat = pd.Categorical(y_train, categories=["a", "b", "c", "d"], ordered=True)
        y_train = pd.Series(y_cat)

        # Put X_train in correct datatype
        X_train = pd.DataFrame(X_train)

        # Create the model
        ordinalModel = OrderedModel(endog=y_train, exog=X_train, distr='logit')
        res_log = ordinalModel.fit(method='bfgs', disp=True)
        res_log.summary()

        # Determine correctness
        predicted = res_log.model.predict(res_log.params, exog=X_train)
        pred_choice = predicted.argmax(1)
        print('Fraction of correct choice predictions')
        print((np.asarray(y_train.values.codes) == pred_choice).mean())
        '''

        # Put y_train in correct datatype
        Y = Y.to_numpy()
        for i in range(0, Y.shape[0]):
            if Y[i] == '[1.0, 0.0, 0.0, 0.0]':
                Y[i] = 'a'
            if Y[i] == '[0.0, 1.0, 0.0, 0.0]':
                Y[i] = 'b'
            if Y[i] == '[0.0, 0.0, 1.0, 0.0]':
                Y[i] = 'c'
            if Y[i] == '[0.0, 0.0, 0.0, 1.0]':
                Y[i] = 'd'
        Y_cat = pd.Categorical(Y, categories=["a", "b", "c", "d"], ordered=True)
        Y = pd.Series(Y_cat)

        # Put X_train in correct datatype
        X_new = pd.DataFrame(X_new)

        # Create the model
        ordinalModel = OrderedModel(endog=Y, exog=X_new, distr='logit')
        res_log = ordinalModel.fit(method='bfgs', disp=True)
        res_log.summary()

        # Determine correctness
        predicted = res_log.model.predict(res_log.params, exog=X_new)
        pred_choice = predicted.argmax(1)
        print('Fraction of correct choice predictions')
        print((np.asarray(Y.values.codes) == pred_choice).mean())

    # Using multinomial logistic regression
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
