import pandas as pd

from Models.MLR import MLR

def main():

    df_csv = pd.read_csv('res/largeDataCategorical.csv')
    print(df_csv)

    print("Feature Selection . . .")


    print("\nMultinomial Logistic Regression . . .")

    #TODO - pass real data

    # mlr = MLR()
    # mlr.evaluate()
    # mlr.predict()


    print("\nOther Methods . . .")


if __name__ == "__main__":
    main()