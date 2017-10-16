import random, pandas as pd
print(pd.read_excel('films.xls')['Title of the Film'].tolist()[random.randint(0, 1000)])
