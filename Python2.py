import pandas as pd
dummy_data3 = {
        'id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'Feature3': [12, 13, 14, 15, 16, 17, 15, 12, 13, 23]}

df3 = pd.DataFrame(dummy_data3, columns = ['id', 'Feature3'])

print(df3)