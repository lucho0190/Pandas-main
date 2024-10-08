import pandas as pd

path = './Sesión_2/Online_Retail.csv'

retail_data = pd.read_csv(path, encoding='latin1')

print(type(retail_data))

print(retail_data)