import pandas as pd
canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

concat_data= pd.concat([canadian_youtube, british_youtube])

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
join_data = left.join(right, lsuffix='_CAN', rsuffix='_UK')





df_merge_col = pd.merge(left, right, on='title')

print(df_merge_col)