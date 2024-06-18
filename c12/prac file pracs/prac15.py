import pandas as pd
d = {'Type':['Fiction','Non Fiction','Drama','Poetry'],'Code':['F','NF','D','P']}
df = pd.DataFrame(d)
print(df)

df['Num_Copies']=[300,290,450,760]
print(df)

df.loc['4']=['Folk Tale','FT',600]
print(df)

df=df.rename({'Code':'Book_Code'},axis='columns')
print(df)