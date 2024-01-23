# pandas is a library used in python for working with the data and used basically in the area of data analysis
# The main scope of Pandas include analyzing, cleaning, exploring and manipulating data
# It is a must know field if you are working in the field of data science 
"""
It helps you in cleaning and generating valuable insights from large datasets.
You can take a messy data set and convert it into readable format with the help of pandas
The statistical methods can be applied between the data to generate other insights as well.
"""
"""https://github.com/pandas-dev"""

import pandas as pd

x={'Fruit': ["Orange","apple","banana"], 
   'Vegetable' :["Cauliflower", "Cabbage" , "Spinach"]}

var= pd.DataFrame(x)
print(var)