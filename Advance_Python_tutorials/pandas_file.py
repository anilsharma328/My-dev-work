

import pandas as pd
filename= "/Advance_Python_tutorials/outcome_measurements.txt"
df = pd.read_csv(filename, sep="|", error_bad_lines=False, index_col=False, dtype='unicode')
ids_to_search=['2','4','42','32','1','23','1165680','1165681']
df.head()
print(df.loc[df['id'].isin(ids_to_search)])


city=['A','B','C','D']
c1,*c2=city
print (c1)