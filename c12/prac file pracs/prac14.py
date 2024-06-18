import pandas as pd
d = [['Divya', 'HR',95000],['Mamta','Marketing',97000],['Payal', 'IT',98000], ['Deepak','Sales',79000]]
df = pd.DataFrame(d, columns=['NAME','DEPARTMENT','SALARY'])
print(df)