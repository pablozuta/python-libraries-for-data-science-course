import numpy as np
import pandas as pd

# create a series from a list
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print("data looks like a numpy array: ", data)

# we can manually specify indexes
data = pd.Series([0.25, 0.5, 0.75, 1.0],
              index=['index1', 'index2', 'index3', 'index4'])
print("data looks like a python dict: ", data)
print(data['index2'])

# we can create a Series directly from a dict
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
area_dict = {'California': 423967,
                   'Texas': 695662,
                   'New York': 141297,
                   'Florida': 170312,
                   'Illinois': 149995}

population = pd.Series(population_dict)
area = pd.Series(area_dict)
print(population)
print(area)

# what do you think of this line?
print(population['California':'Florida'])

# ----------------------------------------------------------------------------------
# DataFrames  allow you to combine several  Series  into columns, much like in an SQL 
# table. Building a  DataFrame  is easy:

# from a Series
df = pd.DataFrame(population, columns=['population'])
print(df)

# from a list of dict
data = [{'a': i, 'b': 2 *i} for i in range(3)]
df = pd.DataFrame(data)
print(df)

# from several Series
df = pd.DataFrame({'population': population,
                   'area': area})
print(df)

# from a 2dimensional numpy array
df = pd.DataFrame(np.random.rand(3, 2),
              columns=["Columna 1", "Columna 2"],
              index=['a', 'b', 'c'])
print(df)              

# a function to generate dataframes
def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)
# example
print(make_df('ABC', range(4)))

# -------------------------------------------------------------
#  it is advisable to use the  loc  (which refers by index) 
# and  iloc  (which refers by position) attributes of each object.
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                  index=['a', 'b', 'c', 'd'])

print(data)
print(data.loc['b'])                  
print(data.iloc[1]) 

# We perform these same operations on  DataFrames  in a similar way
data = pd.DataFrame({'area': area, 'pop':population})
print(data)               
print(data.loc[:'Illinois', :'pop'])   

# ------------------------------------------------------------------
# we're interested in the union of  Series  or  DataFrame.
# With Pandas, this operation is carried out using pd.concat

# on a Series
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
print(ser1)
print(ser2)
ser_concat = pd.concat([ser1, ser2])
print('Concatenacion de Series')
print(ser_concat)


# on a DataFrame using the function we created
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
df_concat = pd.concat([df1, df2])
print('Concatenacion de DataFrames')
print(df_concat)

# By default,pd.concat  assembles its arguments "vertically".
# To change this orientation, we can use the  axis  argument.
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index
# same indexes

print(pd.concat([x, y]))
# we can ask for hierarchical indexes
hdf = pd.concat([x, y], keys=['x', 'y'])
print(hdf)

# ---------------------------------------------------------------------------------
# JOIN
# Another very useful function to manipulate Dataframes is  pd.merge
# which allows you to join DataFrames.
# A join is assembles information from one table A with that from another table B 
# according to a chosen criterion.
# This criterion is called the join condition.
# This condition is composed of one or more columns that are common to A and B.

# first dataframe with two colums
df3 = pd.DataFrame({
    # first column with 4 rows
    'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
    'department': ['Accounting', 'Engineering', 'Engineering', 'HR']})

# second dataframe with two columns    
df4 = pd.DataFrame({
    # second column with 4 rows
    'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
    'date': [2004, 2008, 2012, 2014]})

print("df3 dataframe: ")
print(df3)    
print("df4 dataframe: ")    
print(df4)   

# here we do the merge of df3 and df4
df5_merge = pd.merge(df3, df4)
print('this is the merge of df3 and df4')
print(df5_merge)
# the result is a dataframe with 3 columns (the employee columns is the same for the two dataframes)
# here we have a one to one relationship
# one employee can belong to only one department
# and one employee can have only one date on entrance

#---------------------------------------------------------------
# CARDINALITY
# one to many (or many to one) dataframe
# here we gonna make a dataframe for a supervisor
# a supervisor can have a one to many relationship with employees

df_supervisor = pd.DataFrame({'department': ['Accounting', 'Engineering', 'HR'],
                             'supervisor': ['Carly', 'Guido', 'Steve']})

print('')
print('dataframe supervisor')
print(df_supervisor)
# in this dataframe carly is supervisor of accounting
# guido is supervisor of engineering
# steve is supervisor of hr
# so guido have a relationship one to many with jake and lisa
df_sup_emp_merge = pd.merge(df5_merge, df_supervisor)
print('')
print('merge supervisor and employees')
print(df_sup_emp_merge)

# ----------------------------------------------------------------------
# Many-to-many
# To continue with our example, let's suppose we have another Dataframe 
# containing the necessary skills needed to work in each department:

# department is the name of the column and the array data are the rows data of that column
df_skills = pd.DataFrame({'department': 
                         ['Accounting', 'Accounting',
                         'Engineering', 'Engineering',
                          'HR', 'HR'],
          
          # competence is the other column
          'competence': ['math', 'spreadsheets',
                         'coding','linux', 
                         'spreadsheets', 'organization' ]})
print('')
print('this is the skills dataframe')
print(df_skills)
# Now, we want to associate each employee with the skills they need to work 
# in their department. 
# Here, we will need a many-to-many cardinality 
# because an employee needs several skills
# and a skill can be shared by several employees. 
                     