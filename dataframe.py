import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = {'Name': ['Jay', 'Cydia', 'Zhou'],
        'Age': ['28', '22', '30'],
        'Class': ['初中', '高中', '高中']}
if __name__ == '__main__':
    # Series
    # s1 = pd.Series(data['Country'])
    # print(s1.values)
    # print(s1.index)
    # 转成一个DataFrame
    df = pd.DataFrame(data)
    print(df)
    # df.iterrows()返回一个 generator 类型，可以for循环遍历 列如,以data数据为基础，返回的长度为2

    dfit = df.iterrows()
    print(type(dfit))
    # for i in dfit:
    #     print(i)
    #     print(len(i))
    for x in dfit:
        print(x[0], x[1], type(x[1]))
