# importing necessary libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib # importing library to change the default setting
import matplotlib.pyplot as plt # Visualization
import seaborn as sns # Visualization on top of matplotlib

# Let's change the default setting
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] =8
matplotlib.rcParams['figure.figsize'] = (10,6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

#import data
df = pd.read_csv("Car_sales.csv")
df.head(9)
df.info()
df.shape

# Drop duplicate rows
df.drop_duplicates(keep ='last')
df.shape

# Dropping unnecessary columns
drop_cols = ['Vehicle_type']
df = df.drop(drop_cols, axis = 1)
len(df.columns)
print(df.describe())

# Sorting w.r.t Fuel Efficiency
df_sort = df.sort_values(by = 'Fuel_efficiency', ascending = False)
df_sort.head(9)

# Replacing space in column names(i apply this in pretty much every problem)
df.columns = df.columns.str.replace(' ', '_')

# Finding maximum/minimum values through function
def max_min_val(col):
    '''
    This function takes the column name as the argument
    and returns the top and bottom observations in the dataframe
    '''
    first = df[col].idxmax()
    first_obs = pd.DataFrame(df.loc[first])
    
    last = df[col].idxmin()
    last_obs = pd.DataFrame(df.loc[last])
    
    min_max_obs = pd.concat([first_obs, last_obs], axis=1)
    
    return min_max_obs

print(max_min_val('Sales_in_thousands'))

# Creating histogram for continuous numerical variable
plt.hist(df['Horsepower'],10)
plt.show()

# Probability Distribution Functions
sns.histplot(df['Horsepower'], bins = 10, kde=True)
plt.show()

# Counting it by its category
make_dist = df.groupby('Manufacturer').size()
make_dist
make_dist.plot(title = 'Make Distribution')
df_num = df.select_dtypes(include = ['float64', 'int64'])
df_num.head(9)
matplotlib.rcParams['font.size'] = 8
matplotlib.rcParams['figure.figsize'] = (10,6)
df_num.hist(bins=15,xlabelsize=7)
plt.show()

# Correlation with Price_in_thousands
df_corr = df_num.corr()['Price_in_thousands'][:-1]
print(df_corr)


# Correlation using pairplot
for i in range(0, len(df_num.columns),5):
    sns.pairplot(df_num, y_vars ='Price_in_thousands', x_vars = df_num.columns[i:i+5]  )
plt.show()

# Significant correlation in one plot( Customized Heatmap)
corr = df_num.drop('Price_in_thousands', axis =1).corr()
sns.heatmap(corr[(corr >= 0.5) |(corr <= -0.4)],
           cmap= 'viridis', vmax = 1.0, vmin = -1.0, linewidths = 0.1,
           annot = True, annot_kws={"size":8}, square =True)
df.columns
plt.show()

# Boxplot for some categorical variables
bp1 = sns.boxplot(y='Manufacturer', x='Horsepower', data = df )
plt.show()
sns.regplot(x = 'Length', y = 'Horsepower', data=df)
plt.show()