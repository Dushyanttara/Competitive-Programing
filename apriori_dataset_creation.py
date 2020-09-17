import pandas as pd 

dataset = pd.read_csv('D:\Prep\python crash course book\Basics\data_files\sample_apriori.csv',sep = ",")

#print(dataset.head())

dataset = dataset.loc[dataset.index.repeat(dataset.conversions)].reset_index(drop=True)

#print(dataset.shape)

dataset.to_csv('D:\Prep\python crash course book\Basics\data_files\sample_apriori_final.csv',',')