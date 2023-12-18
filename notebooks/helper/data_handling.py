import pandas as pd
import numpy as np


def data_from_file(file: str):
    df = pd.read_csv(file)
    df = df.drop("id", axis=1)
    df = df.replace("Unknown", np.NaN)
    df = df.replace("N/A", np.NaN)
    return df

if __name__ == "__main__":
    print(data_from_file("../data/stroke_raw.csv").head())
