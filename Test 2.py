import pandas as pd 
from openpyxl.workbook import workbook

df_csv=pd.read_csv('Names.csv',header=None)
df_csv.columns=['First','Last','Address','City','State','Area Code']

#print(df_csv.columns)
#print(df_csv[['State','Area Code']])
print(df_csv['First'])
print(df_csv['First'][0:3]) #New: Just first three lines
print(df_csv.iloc[2,1])

wanted_values=df_csv[['First','Last','State']]
stored=wanted_values.to_excel('State Locations.xlsx')




