import os

import pandas as pd


def categorical_index_fc():
    """
    identify which columns are the categorical variables
    :return:
    a list of where categorical variables locate
    """
    the_infile = '../../RFcompare/dataset/descriptor_feature_RF_sorted.csv'
    df = pd.read_csv(the_infile)
    df = df.iloc[:, 9:]
    print("df", df.shape)

    df_head = df.iloc[:0, :]

    categorical_col = df.select_dtypes(include=['category', 'int'])
    categorical_col_name = categorical_col.columns.tolist()
    print('test', categorical_col_name)
    for i in categorical_col_name:
        name_table = i.split(",")
        print(name_table)

    n = 0
    index = -1
    categorical_col_index = []
    for i in df_head:
        index += 1
        if i in categorical_col_name:
            n += 1
            categorical_col_index.append(index)
    print("n=", n)

    return categorical_col_index