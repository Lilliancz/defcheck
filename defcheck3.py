import pandas as pd
import numpy as np
import os


getinput = raw_input("Enter the source filename (without the csv extension): ")
filename = getinput+'.csv'                  
df = pd.read_csv(filename)
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()
df5 = pd.DataFrame()
df6 = pd.DataFrame()
df7 = pd.DataFrame()
df8 = pd.DataFrame()

df1['Name'] = df['workerId']
df2['Name'] = df['workerId']
df3['Name'] = df['workerId']
df4['Name'] = df['workerId']
df5['Name'] = df['workerId']
df1['URL'] = df['URL1']
df1['Lender'] = df['QID30(1)']
df1['Counsel'] = df['QID8(1)']
df1['SelectCounsel'] = df['QID9(1)']
df1['Section'] = df['QID10(1)']
df2['URL'] = df['URL2']
df2['Lender'] = df['QID30(2)']
df2['Counsel'] = df['QID8(2)']
df2['SelectCounsel'] = df['QID9(2)']
df2['Section'] = df['QID10(2)']
df3['URL'] = df['URL3']
df3['Lender'] = df['QID30(3)']
df3['Counsel'] = df['QID8(3)']
df3['SelectCounsel'] = df['QID9(3)']
df3['Section'] = df['QID10(3)']
df4['URL'] = df['URL4']
df4['Lender'] = df['QID30(4)']
df4['Counsel'] = df['QID8(4)']
df4['SelectCounsel'] = df['QID9(4)']
df4['Section'] = df['QID10(4)']
df5['URL'] = df['URL5']
df5['Lender'] = df['QID30(5)']
df5['Counsel'] = df['QID8(5)']
df5['SelectCounsel'] = df['QID9(5)']
df5['Section'] = df['QID10(5)']




frames = [df1, df2, df3, df4, df5]
result = pd.concat(frames)
result = result.sort_values(['Name'])


barefile = os.path.splitext(filename)[0]
result.to_csv(barefile+'-concat.csv')