import pandas as pd


def explore_dataset(path):
    df = pd.read_csv(path)
    print('----------info----------\n')
    print(df.info())
    print('\n----------head----------\n')
    print(df.head())
    print('\n----------data description----------\n')
    print(df.describe())
    return df

