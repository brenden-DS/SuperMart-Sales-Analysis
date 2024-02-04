#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import style
style.use('seaborn')
from matplotlib.pyplot import rcParams
rcParams['figure.figsize']=10,5
import warnings
warnings.filterwarnings('ignore')

print('modules imported!')


# In[4]:


#readin the dataset
df=pd.read_csv('/Users/brenden/Downloads/pdf/DATASETS/Supermart Grocery Sales.csv')
print('Done!')


# In[5]:


df.head()


# In[6]:


#check the size of the dataset
df.shape


# In[7]:


#Get information about the datatypes ,shape and names of the columns in the dataset
df.info()


# In[8]:


#Get the descriptive statisticsof the data
df.describe()


# In[9]:


#Check for any missing values
df.isnull().sum()


# In[10]:


#check for duplicated data
df.duplicated().sum()


# In[11]:


#change column names to lowercase to make it easier to work with
df.columns=df.columns.str.lower()


# ### Business problems to be solved  using this dataset:

# 1.Sales Performance Analysis.Which categories has the most sales, & which ones are underperforming?
# 
# 2.Regional Market Analysis.Which region are experiencing more sales and which ones are lagging?
# 
# 3.Which 5 cities have the highest sales & profit?
# 
# 4.Profit Margin Analysis.Do the sales significantly impact the profit?
# 
# 5.Discount Rate Analysis.Does the discount have any effect on profit?
# 
# 6.Yearly sales performance per region.
# 
# 7.Yearly profit per category.Which category performed the best & which ones didn't?

# <h3> 1.Sales Performance Analysis

# In[12]:


cat_sales=df.groupby('category')['sales'].sum()
sorted_cat_sales=cat_sales.sort_values(ascending=False)
sorted_cat_sales.plot(kind='bar')
plt.ylabel('TOTAL SALES')
plt.xticks(rotation=0,ha='center')
for i, v in enumerate(sorted_cat_sales):
    plt.text(i, v + 0.1, str(v), ha='center')

plt.show()


# ### Inference:
# 
# - We can clearly see that the Eggs, Meat & Fish category out performed the rest of the categories with a total of $2267401 sales, this could be attributed to its various sub categories which provides a wide range  of options therefore maximizing sales.
# 
# - Oil & Masala category is the one with the least sales totaling $2038442 of this could also be to the limited range of sub categories.

# <h3> 2.Regional Sales Analysis

# In[13]:


reg_sales=df.groupby('region').agg({'sales':'sum','profit':'sum'}).reset_index()
sorted_reg_sales=reg_sales.sort_values(by='sales',ascending=True)
sorted_reg_sales.set_index('region',inplace=True)
sorted_reg_sales.plot(kind='bar')
plt.title('TOTAL PROFIT & SALES PER REGION')
plt.ylabel('TOTAL SALES & PROFIT')
plt.xticks(rotation=0,ha='center')
for i, v in enumerate(sorted_reg_sales['sales']):
    plt.text(i, v + 0.1, str(v), ha='right')
    
for i, v in enumerate(sorted_reg_sales['profit']):
    plt.text(i, v + 0.1, str(v), ha='left')    

plt.show()


# ### Inference:
# - The North region has the least sales & profit while the West region has the most sales & is the most profitable. The West region's profitability is attributed to the high discount it gives which encourages more sales there resulting in more profit.

# <h3> 3.Top 5 cities exceling in sales & profit

# In[14]:


city_sales = df.groupby('city').agg({'sales':'sum'}).reset_index()

sorted_city_sales = city_sales.sort_values(by='sales',ascending=True)
sorted_city_sales.set_index('city',inplace=True)
sorted_city_sales.head(5).plot(kind ='barh')
plt.xlabel('TOTAL SALES')
plt.title('TOP 5 CITIES WITH HIGHEST SALES')

city_profit = df.groupby('city').agg({'profit':'sum'}).reset_index()
sorted_city_profit = city_profit.sort_values(by='profit',ascending=True)
sorted_city_profit.set_index('city',inplace=True)
sorted_city_profit.head(5).plot(kind ='barh',color='teal')
plt.xlabel('TOTAL PROFIT')
plt.title('TOP 5 CITIES WITH HIGHEST PROFIT')

plt.show()


# - <h3> 4.Profit Margin Analysis

# In[15]:


profit=df[['profit','sales']].corr()
sns.heatmap(profit,cmap='BrBG',annot=True)


# ### Inference:
# 
# - Theres relatively strong positive correlation between sales & profit.This is why an increase in sales will inherently result in an increase in profit

# - <h3> 5.Discount Analysis

# In[16]:


discount=df.groupby('region').agg({'sales':'sum','profit':'sum','discount':'sum'}).reset_index()
sorted_discount=discount.sort_values(by='discount',ascending=False)
sorted_discount.set_index('region',inplace=True)
sorted_discount


# In[28]:


reg_dis=df.groupby('region')['discount'].sum().reset_index()
sort_reg_dis= reg_dis.sort_values(by='discount',ascending=True)
sort_reg_dis.set_index('region',inplace=True)
sort_reg_dis.plot(kind='pie',y='discount',autopct= '%1.1f%%',figsize=(14,6))


# ### Inference:
# 
# - Despite giving the least discount amount out of all the regions, the North region has a few sales resulting in the insignificant profit.Inversely the West region has the highest discount amount but due to the large number of sales it made it accumulated the most profit

# <h4> 6.Sales Performance Per Sub Category

# In[42]:


subcat_sales=df.groupby('sub category').agg({'sales':'sum','profit':'sum'}).reset_index()
sorted_subcat_sales=subcat_sales.sort_values(by=['sales','profit'])
sorted_subcat_sales.set_index('sub category',inplace=True)
sorted_subcat_sales.plot(kind='barh')
plt.xlabel('TOTAL SALES & PROFIT')
plt.title('TOTAL SALES & PROFIT PER SUB CATEGORY')
plt.show()


# 
# 
# ### Inference:
# 
# - On a sub category level  beverages performed the best

# <h4> 7.Yearly Sales Performance Per Region

# In[40]:


df['year']=pd.to_datetime(df['order date']).dt.year


# In[41]:


yearly_sales=df[['year','sales','profit']]
grp=yearly_sales.groupby('year').agg({'sales':'sum','profit':'sum'}).reset_index()
sort_grp=grp.sort_values(by='sales',ascending=True)
sort_grp.set_index('year',inplace=True)
sort_grp.plot(kind='line')


# ### Inference:
# 
# - Sales & profit have been steadily increase over the years
