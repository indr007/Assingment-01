import pandas as pd      
df=pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item',
                 sep='\t')
print(df)


