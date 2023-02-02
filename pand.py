import numpy as np
import pandas as pd
a_numpy_bear = np.array([100, 5, 80, 20])
print(a_numpy_bear)

bear_family = [
    np.array([100, 5, 20, 80]),
    np.array([50, 2.5, 10, 40]),
    np.array([110, 6, 22, 80]),
]
# we transform that into numpy multidimensional array
bear_family_numpy = np.array(bear_family)
print(bear_family_numpy)

print(bear_family_numpy[2, 0]) # third row , first column
print(bear_family_numpy[:, 0]) # all rows , first column

bear_family_df = pd.DataFrame(bear_family)
print(bear_family_df)

# aca le pasamos un numpy array y creamos encabezados para rows y columns
bear_family_df = pd.DataFrame(bear_family_numpy,
                 index = ['mom', 'baby', 'dad'],
                 columns=['leg', 'hair', 'tail', 'belly']
)
print("")
print(bear_family_df)

# accesing methods
print(bear_family_df.belly)
print(bear_family_df['belly'])

# iterrows method
for ind_row, content_row in bear_family_df.iterrows():
    print("Here is %s bear: " % ind_row)
    print(content_row)
    print("----------------------------")

# iloc and loc methods to accesing data
print("iloc [2]", bear_family_df.iloc[2])
print(bear_family_df.loc['dad'])

# finding a discrete result
print("boolean values return: ",bear_family_df['belly'] == 80)

# adding data
some_bears = pd.DataFrame([[105,4,19,80],[100,5,20,80]],
# two new bears
                            columns = bear_family_df.columns) 
# same columns as bear_family_df
all_bears = bear_family_df.append(some_bears)
print(all_bears)

# LOAD a CSV file
data_directors = pd.read_csv('top_directors_data.csv')
pd.set_option('display.max_columns', None)
print(data_directors.head(3))

data_movies = pd.read_csv('top_movies_data.csv')
pd.set_option('display.max_columns', None)
print(data_movies.head(3))