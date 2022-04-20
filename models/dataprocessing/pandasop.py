import pandas as pd


def PandasOperations(datasets_links):
    read_url = [pd.read_csv(url) for url in datasets_links]
    # Merging dataframes in dfs
    df = pd.concat(read_url, ignore_index=True)
    df.drop(['TRANSPORT_TYPE_ID', 'TRANSFER_TYPE_ID'], axis=1,inplace=True)

    print(df.head(2))

