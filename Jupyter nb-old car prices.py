#!/usr/bin/env python
# coding: utf-8

# <p align="center"><img src="https://github.com/insaid2018/Term-1/blob/master/Images/INSAID_Full%20Logo.png?raw=true" width="260" height="110" /></p>

# ---
# # **Table of Contents**
# ---
# 
# 1. [**Introduction**](#Section1)<br>
# 2. [**Problem Statement**](#Section2)<br>
# 3. [**Installing & Importing Libraries**](#Section3)<br>
# 4. [**Data Acquisition & Description**](#Section4)<br>
# 5. [**Data Pre-Profiling**](#Section5)<br>
# 6. [**Data Cleaning & wrangling**](#Section6)<br>
# 7. [**Exploratory Data Analysis**](#Section8)<br>
# 8. [**Summarization**](#Section9)</br>
# 
# 
# ---

# # **1. Introduction**
# ---
# 
# - The used car market has largely been driven by the supply side rather than the demand side, and the availability of internet connectivity has made it easier for people to advertise their used cars effectively, thus increasing the overall supply and, in turn, providing a boost to the market.
# 
# - Forecast Period (2020-2030) CAGR	8.7%
# 
# - Hence I have used this data to see the trends available for buying and selling old cars.
# 
# 
# ![](https://www.kenresearch.com/blog/wp-content/uploads/2020/05/Used-Vehicle-Market-Research-Report.png)
# - Report based on https://www.psmarketresearch.com/market-analysis/used-car-market

# ---
# <a name = Section2></a>
# # 2. Problem Statement & Objective
# ---
# 
# - Main objective of this project is to draw insights  into  used car available  in market. 
# - Also to perform EDA on the dataset to get detailed insights about the sample data.
# -----------------------------------------------------------------
# 
# ### Some Questions :
# 
#     - What is deciding factor for quoting prices for used cars?
#     - What make /build/type is available in the used market?
#     - What years make is readily available in used car market?
# 
# 
# #### *Data is from a dealer which provides price quotes for the cars put up for sale.*
# 

# ---
# <a id = Section3></a>
# # **3. Installing & Importing Libraries**
# ---
# 
# - This section is emphasised on installing and importing the necessary libraries that will be required.

# In[1]:


import pandas as pd  # main librabry to store and manipulate tabular data in rows of observations and columns of variables.
import numpy as np  # for numerical python aid
import matplotlib.pyplot as plt # Main library pyplot in matplotlib used for graphical interface
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns # used for visalisation
from pandas_profiling import ProfileReport # To generate Univariate Analysis


# ---
# <a name = Section4></a>
# # **4. Data Acquisition & Description**
# ---
# 
# - Data is used from github from insaid2018 term1.
# 
# - Below are the features of the data set:
# 
# |Id|Feature|Description|
# |:--|:--|:--|
# |01| car           | Car brand name| 
# |02| model         | Available car different Variants|  
# |03| year          | purchasing Year| 
# |04| body          | Body type-Hatchback, Sedan, Crossover etc|   
# |05| mileage       | car Mileage|
# |06| engV          | Engine version|
# |07| engType       | Car Fuel type - Petrol, Diesel, gas etc|
# |08| drive         | Wheel Drive Front, back|
# |09| registration  | Check if the vechile is registered|
# |10| price         | Price of Car in $|
# 

# In[2]:


df_cars = pd.read_csv('auto.csv') # creating a data frame from csv file.


# In[3]:


df_cars.shape # Check rows and columns of dataframe.


# In[4]:


df_cars.head(10) # checking the upper portion of dataframe


# In[5]:


df_cars.describe().transpose()   # to check the descriptive stats for the continuous or non categorical data 


# # 5. Data Pre-Profiling
# 
# - Using profile library for this quick check ,kind of an overview for the data wrangling.

# In[41]:


profile = ProfileReport(df_cars, title="Pandas Profiling Report")
profile.to_file("your_report.html")


# ### 6.Data Cleaning & wrangling before we proceed for EDA
# 
# - engV has 434 Nan values and would be converting them to median values since mean is not accurate here because of outliers.
# - drive has 511 Nan values and would be converting them to median values since mean is not accurate here because of outliers.
# - we also found out 112 rows of duplicate values so we have removed duplicacy for the sake of EDA preparation.
# - We also noted some values as '0' while using describe function and wehave converted them to median value as well for sake of not loosing data.
# - We are finally left with 8953 rows of data. 
# 

# In[7]:


df_cars.describe().transpose()


# In[8]:


df_cars.isnull().sum() # to recheck any null values present in columns


# In[9]:


new_price=df_cars['price'].astype(float).median()
print('new_price median is :', new_price)


# In[10]:


new_mileage = df_cars['mileage'].astype(float).median()
print('new_mileage meadian is :',new_mileage)


# In[11]:


new_engv = df_cars['engV'].astype(float).median()
print('new engv is :',new_engv)


# In[12]:


df_cars['price'].replace(0, new_price, inplace = True) # replacing the null values as median value of 9200
df_cars['mileage'].replace(0, new_mileage ,inplace = True) # replacing the null values as median value of 128
df_cars['engV'].replace(np.nan, new_engv ,inplace = True) # replacing the null values as median value of 128
df_cars['price'].replace(np.nan, new_price, inplace = True) # replacing the null values as median value of 9200
df_cars['mileage'].replace(np.nan, new_mileage ,inplace = True) # replacing the null values as median value of 128


# In[13]:


df_cars.describe().transpose()


# # 7. Exploratory Data Analysis
# 
#   -  Make & Model which dominates used car data available.
#   -  Pictorial representation of feature sets available for the used cars data
#   -  correlation amongst feature sets & prices quoted available for the used cars data
# 

# In[44]:


df_cars['car'].value_counts().head(20).plot(kind ='bar', figsize=(12,6),color= 'olive')


# In[45]:


df_cars['year'].value_counts().head(20).plot(kind ='bar', figsize=(12,6),color= 'olive')


# In[16]:


print(df_cars['model'].nunique())


# In[17]:


df_cars.info()


# In[18]:


df_cars = df_cars[df_cars['drive'].isna() == False]


# In[19]:


df_cars.info()


# In[53]:


df_cars['engType'].value_counts().plot(kind= 'bar',color='olive')
(df_cars['engType'].value_counts()/len(df_cars)*100)


# In[49]:


df_cars['registration'].value_counts().plot(kind= 'bar',color='olive')


# In[68]:


(df_cars['drive'].value_counts()/len(df_cars)).plot(kind= 'bar',color='olive')


# In[22]:


df_cars = df_cars[~df_cars.duplicated() == True]


# In[23]:


df_cars.shape


# #### Categorising the mileage for cars in 3 bins

# In[24]:


df_cars['mileage-cat'] = np.where(df_cars['mileage']<=333.66,'Low-Mileage',np.where(df_cars['mileage']>=666.33,'High-Mileage','Med-Mileage'))
df_cars['year-slot'] = np.where(df_cars['year']<=2000,'before yr 2000',np.where(df_cars['year']>=2010,'After 2010','Btw 2000 & 2010'))


# In[25]:


df_cars.describe().transpose()


# In[26]:


plt.figure(figsize=(12,6))
sns.scatterplot(data = df_cars,x= 'year',y='price',hue = 'body')


# In[69]:


df_cars.groupby(['body'])['mileage'].count().plot(kind='bar',figsize=(12,6),color = 'olive' )


# In[29]:


df_cars['year'].value_counts().plot(kind='bar', figsize=(12,6))


# In[30]:


# Engine size as potential predictor variable of price
plt.figure(figsize=(12,6))
sns.regplot(x="year", y="price", data = df_cars)


# In[56]:


df_cars.corr()


# In[31]:


df_cars.groupby(['mileage-cat'])['price'].mean().plot(kind='bar', figsize=(12, 6))


# In[32]:


(df_cars['year-slot'].value_counts().head(10)/len(df_cars)*100).plot(kind='bar', fontsize=10, color ='green',yticks= np.arange(0,70,15))
plt.xlabel('Car brands sold')
plt.ylabel('% contribution in sales')
plt.title('Car sales brandwise contribution in %s - Top 10')


# In[65]:


(df_cars['body'].value_counts()/len(df_cars)*100).plot(kind = "bar",color='olive',figsize=(6,5) )
plt.ylabel('count % ')
plt.title('Bodywise used cars availability')

df_cars.groupby('body')['price'].agg(['mean']).plot(kind = "bar",color='olive',figsize=(6,5),subplots = True )
plt.ylabel('Average price ')
plt.title('Average quoted prices in market')


# In[34]:


axes = df_cars.plot.line(subplots=True,figsize=(12,10))


# In[35]:


(df_cars['engType'].value_counts()/len(df_cars)*100).plot(kind='pie')


# In[36]:


sns.pairplot(df_cars)


# In[37]:


sns.regplot(x='mileage',y='price',data=df_cars)


# In[38]:


df_cars['mileage'].plot(kind='hist',figsize=(8,5))


# In[39]:


plt.figure(figsize=(10,6))
sns.scatterplot(x='year', y='price', data = df_cars,hue= 'drive')


# In[40]:


df_cars.groupby(['body'])['price'].agg(['quantile']).plot(kind='bar',figsize=(8,6))
df_cars.groupby(['engType'])['price'].agg(['count']).plot(kind='bar',figsize=(8,6))


# # 8.Summarization
# 
# ---------------------------------------------------------------------------------------------------------------------------
# 
# - As per sample data ,prices in the used car market is not only dependent on the features as per correlation matrix and can be safely assumed condition of the car is also one of the factors.
# 
# - Sedans are more sought after by buyers in used car segment as per the sample data.
# 
# - Prices quoted for the cross-overs is more and sellers would benefit if they increase their sales volume.
# 
# - Other fuel types namely EV’s still majorly available in market .
# 
