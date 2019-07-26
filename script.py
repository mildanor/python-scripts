import numpy as np
import pandas as pd

#data types inside a dataframe
new_data.dtypes

#Content Type Orgs Geography Sector Themes are filters
#read csv & store in variable
new_data = pd.read_csv('Rein_filters.csv', delimiter = ',')


#Frequency in a column
companyName_count = new_data['companyName'].value_counts()

sector_count = new_data['Sector'].value_counts()

filterType_count = new_data['FilterType'].value_counts()

orgs_count = new_data['Orgs'].value_counts()

contentType_count = new_data['ContentType'].value_counts()


geography_count = new_data['Geography'].value_counts()

query_count = new_data['Query'].value_counts()
#save output as dataframe
contentType_count_frame = pd.DataFrame(contentType_count)
#save into csv
contentType_count_frame.to_csv('contentype.csv')

#Splitting stuff inside cell https://stackoverflow.com/questions/12680754/split-explode-pandas-dataframe-string-entry-to-separate-rows
test = pd.concat([Series(row['index1'], row['ContentType'].split(','))              
    for _, row in new_data.iterrows()]).reset_index()
#Worked

##on indexing https://www.geeksforgeeks.org/python-pandas-dataframe-set_index/

##didn't work
from pandas import DataFrame
b = DataFrame(str(new_data.ContentType.str.split(',').tolist()), index=new_data.index1).stack()
b = b.reset_index()[[0, 'index1']] 
b.columns = ['ContentType', 'index1']

#converted variable to string
content_type_toString = str(new_data.ContentType)

#convert columns to string
new_data[["ContentType", "CompanyName"]] = new_data[["ContentType", "CompanyName"]].astype(str) 
new_data[["ContentType"]] = new_data[["ContentType"]].astype(str) 
new_data[["CompanyName"]] = new_data[["CompanyName"]].astype(str) 

#create index column
new_data['index1'] = new_data.index