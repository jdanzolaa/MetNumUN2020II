#!/usr/bin/env python
# coding: utf-8

# #Introduction to the Research Environment
# 
# The research environment is powered by IPython notebooks, which allow one to perform a great deal of data analysis and statistical validation. We'll demonstrate a few simple techniques here.

# ##Code Cells vs. Text Cells
# 
# As you can see, each cell can be either code or text. To select between them, choose from the 'Cell Type' dropdown menu on the top left.

# ##Executing a Command
# 
# A code cell will be evaluated when you press play, or when you press the shortcut, shift-enter. Evaluating a cell evaluates each line of code in sequence, and prints the results of the last line below the cell.

# In[1]:


2 + 2


# In[9]:


3+3


# Sometimes there is no result to be printed, as is the case with assignment.

# In[2]:


X = 2


# In[10]:


x=3


# Remember that only the result from the last line is printed.

# In[3]:


2 + 2
3 + 3


# In[13]:


3+4
8+9


# However, you can print whichever lines you want using the `print` statement.

# In[4]:


print 2 + 2
3 + 3


# In[14]:


print 3+4
8+9


# ##Knowing When a Cell is Running
# 
# While a cell is running, a `[*]` will display on the left. When a cell has yet to be executed, `[ ]` will display. When it has been run, a number will display indicating the order in which it was run during the execution of the notebook `[5]`. Try on this cell and note it happening.

# In[15]:


#Take some time to run something
c = 0
for i in range(10000000):
    c = c + i
c


# ##Importing Libraries
# 
# The vast majority of the time, you'll want to use functions from pre-built libraries. You can't import every library on Quantopian due to security issues, but you can import most of the common scientific ones. Here I import numpy and pandas, the two most common and useful libraries in quant finance. I recommend copying this import statement to every new notebook.
# 
# Notice that you can rename libraries to whatever you want after importing. The `as` statement allows this. Here we use `np` and `pd` as aliases for `numpy` and `pandas`. This is a very common aliasing and will be found in most code snippets around the web. The point behind this is to allow you to type fewer characters when you are frequently accessing these libraries.

# In[16]:


import numpy as np
import pandas as pd

# This is a plotting library for pretty pictures.
import matplotlib.pyplot as plt


# ##Tab Autocomplete
# 
# Pressing tab will give you a list of IPython's best guesses for what you might want to type next. This is incredibly valuable and will save you a lot of time. If there is only one possible option for what you could type next, IPython will fill that in for you. Try pressing tab very frequently, it will seldom fill in anything you don't want, as if there is ambiguity a list will be shown. This is a great way to see what functions are available in a library.
# 
# Try placing your cursor after the `.` and pressing tab.

# In[7]:


np.random.beta


# In[17]:


np.random.beta


# ##Getting Documentation Help
# 
# Placing a question mark after a function and executing that line of code will give you the documentation IPython has for that function. It's often best to do this in a new cell, as you avoid re-executing other code and running into bugs.

# In[18]:


for i in range(0, 4):
    print ("This is number %s" % i)


# In[43]:


for i in range(0, 6):
    print ("This is number %s" % i)


# In[19]:


get_ipython().magic('pinfo np.random.normal')


# ##Sampling
# 
# We'll sample some random data using a function from `numpy`.

# In[20]:


# Sample 100 points with a mean of 0 and an std of 1. This is a standard normal distribution.
X = np.random.normal(0, 1, 100)


# In[44]:


y=np.random.normal(0,2,200)


# ##Plotting
# 
# We can use the plotting library we imported as follows.

# In[21]:


plt.plot(X)


# In[45]:


plt.plot(y)


# ###Squelching Line Output
# 
# You might have noticed the annoying line of the form `[<matplotlib.lines.Line2D at 0x7f72fdbc1710>]` before the plots. This is because the `.plot` function actually produces output. Sometimes we wish not to display output, we can accomplish this with the semi-colon as follows.

# In[22]:


plt.plot(X);


# In[46]:


plt.plot(y);


# ###Adding Axis Labels
# 
# No self-respecting quant leaves a graph without labeled axes. Here are some commands to help with that.

# In[23]:


X = np.random.normal(0, 1, 100)
X2 = np.random.normal(0, 1, 100)

plt.plot(X);
plt.plot(X2);
plt.xlabel('Time') # The data we generated is unitless, but don't forget units in general.
plt.ylabel('Returns')
plt.legend(['X', 'X2']);


# In[47]:


y = np.random.normal(0, 2, 200)
y2 = np.random.normal(0, 2, 200)

plt.plot(y);
plt.plot(y2);
plt.xlabel('Time') # The data we generated is unitless, but don't forget units in general.
plt.ylabel('Returns')
plt.legend(['y', 'y2']);


# ##Generating Statistics
# 
# Let's use `numpy` to take some simple statistics.

# In[24]:


np.mean(X)


# In[48]:


np.mean(y)


# In[25]:


np.std(X)


# In[49]:


np.std(y)


# ##Getting Real Pricing Data
# 
# Randomly sampled data can be great for testing ideas, but let's get some real data. We can use `get_pricing` to do that. You can use the `?` syntax as discussed above to get more information on `get_pricing`'s arguments.

# In[53]:


data = get_pricing('MSFT', start_date='2012-1-1', end_date='2015-6-1')


# In[59]:


data = get_pricing('MSFT', start_date='1996-10-7', end_date='2016-10-7')


# Our data is now a dataframe. You can see the datetime index and the colums with different pricing data.

# In[54]:


data


# In[58]:


data


# This is a pandas dataframe, so we can index in to just get price like this. For more info on pandas, please [click here](http://pandas.pydata.org/pandas-docs/stable/10min.html).

# In[60]:


X = data['price']


# In[61]:


y = data['price']


# Because there is now also date information in our data, we provide two series to `.plot`. `X.index` gives us the datetime index, and `X.values` gives us the pricing values. These are used as the X and Y coordinates to make a graph.

# In[29]:


plt.plot(X.index, X.values)
plt.ylabel('Price')
plt.legend(['MSFT']);


# In[62]:


plt.plot(y.index, y.values)
plt.ylabel('Price')
plt.legend(['MSFT']);


# We can get statistics again on real data.

# In[30]:


np.mean(X)


# In[63]:


np.mean(y)


# In[31]:


np.std(X)


# In[64]:


np.std(y)


# ##Getting Returns from Prices
# 
# We can use the `pct_change` function to get returns. Notice how we drop the first element after doing this, as it will be `NaN` (nothing -> something results in a NaN percent change).

# In[32]:


R = X.pct_change()[1:]


# In[69]:


k = X.pct_change()[3:]


# We can plot the returns distribution as a histogram.

# In[33]:


plt.hist(R, bins=20)
plt.xlabel('Return')
plt.ylabel('Frequency')
plt.legend(['MSFT Returns']);


# In[70]:


plt.hist(k, bins=30)
plt.xlabel('Return')
plt.ylabel('Frequency')
plt.legend(['MSFT Returns']);


# Get statistics again.

# In[34]:


np.mean(R)


# In[71]:


np.mean(k)


# In[35]:


np.std(R)


# In[72]:


np.std(k)


# Now let's go backwards and generate data out of a normal distribution using the statistics we estimated from Microsoft's returns. We'll see that we have good reason to suspect Microsoft's returns may not be normal, as the resulting normal distribution looks far different.

# In[36]:


plt.hist(np.random.normal(np.mean(R), np.std(R), 10000), bins=20)
plt.xlabel('Return')
plt.ylabel('Frequency')
plt.legend(['Normally Distributed Returns']);


# In[73]:


plt.hist(np.random.normal(np.mean(k), np.std(k), 6000), bins=30)
plt.xlabel('Return')
plt.ylabel('Frequency')
plt.legend(['Normally Distributed Returns']);


# ##Generating a Moving Average
# 
# `pandas` has some nice tools to allow us to generate rolling statistics. Here's an example. Notice how there's no moving average for the first 60 days, as we don't have 60 days of data on which to generate the statistic.

# In[37]:


# Take the average of the last 60 days at each timepoint.
MAVG = pd.rolling_mean(X, window=60)
plt.plot(X.index, X.values)
plt.plot(MAVG.index, MAVG.values)
plt.ylabel('Price')
plt.legend(['MSFT', '60-day MAVG']);


# In[74]:


# Take the average of the last 60 days at each timepoint.
MAVG = pd.rolling_mean(X, window=30)
plt.plot(X.index, X.values)
plt.plot(MAVG.index, MAVG.values)
plt.ylabel('Price')
plt.legend(['MSFT', '60-day MAVG']);


# In[38]:


for i in range(0, 4):
    print ("This is number %s" % i)


# In[75]:


for i in range(0, 7):
    print ("This is number %s" % i)


# In[39]:


for i in range(0, 4):
    print ("This is number %s" % i)


# In[40]:


from matplotlib.pyplot import plot
plot([1,3,2,5])


# In[76]:


from matplotlib.pyplot import plot
plot([1,3,1,2])


# In[41]:


from matplotlib.pyplot import plot
plot([1,3,2,5])


# In[42]:


for i in range(0, 4):
    print ("This is number %s" % i)


# This presentation is for informational purposes only and does not constitute an offer to sell, a solicitation to buy, or a recommendation for any security; nor does it constitute an offer to provide investment advisory or other services by Quantopian, Inc. ("Quantopian"). Nothing contained herein constitutes investment advice or offers any opinion with respect to the suitability of any security, and any views expressed herein should not be taken as advice to buy, sell, or hold any security or as an endorsement of any security or company. In preparing the information contained herein, Quantopian, Inc. has not taken into account the investment needs, objectives, and financial circumstances of any particular investor. Any views expressed and data illustrated herein were prepared based upon information, believed to be reliable, available to Quantopian, Inc. at the time of publication. Quantopian makes no guarantees as to their accuracy or completeness. All information is subject to change and may quickly become unreliable for various reasons, including changes in market conditions or economic circumstances.
