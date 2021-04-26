import pandas as pd
canadian_youtube = pd.read_csv("CAvideos.csv")
british_youtube = pd.read_csv("GBvideos.csv")

#print(canadian_youtube)
#print(british_youtube)

#concat_data= pd.concat([canadian_youtube, british_youtube])
#print(concat_data)


left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

join_data = left.join(right, lsuffix='_CAN', rsuffix='_UK')


print(join_data)
