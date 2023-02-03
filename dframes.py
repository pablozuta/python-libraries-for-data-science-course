import numpy as np
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic.head()) # this returns the first five rows of the dataframe
print(titanic.head(10)) # aca muestra mas rows

print(titanic.age.unique()) # esto nos devuelve un array con edades unicas dentro del dataframe

print(titanic.describe()) # nos muestra un analisis estadistico de los datos

# esto elimina los rows con valores NaN y lo guardamos en una variable
titanic_drop = titanic.dropna()
print(titanic_drop)

# renaming a column
titanic_drop = titanic_drop.rename(columns= {'sex':'gender'})
print("Renaming of the column 'sex' to 'gender' ")
print(titanic_drop)

# deleting a column
titanic_deleted_age_column = titanic.drop(columns=['age'])
print("Table after deliting the 'age' column")
print(titanic_deleted_age_column)

# esto nos permite sumarizar los datos dependiendo de los atributos que le pasemos
titanic_pivot = titanic.pivot_table('survived', index='sex', columns='class', aggfunc='sum')
print(titanic_pivot)