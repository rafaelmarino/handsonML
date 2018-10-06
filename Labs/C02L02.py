# Loading libraries
import os
import pandas as pd
import numpy as np


filePath = "Labs\\datasets\\housing"


def load_housing_data(housing_path=filePath):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()
housing["income_cat"] = np.ceil(housing['median_income'] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)


# Interactive Computing
os.getcwd()
