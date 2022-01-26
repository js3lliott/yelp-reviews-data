#!/usr/bin/env python
# coding: utf-8

# # Yelp Reviews EDA
# 
# What we've got here is a rather in-depth analysis exploring the best (and possibly worst) features that restaurants have to offer in the main British Columbia metro cities. Some things we're hoping to find out are which restaurant categories score the highest ratings, which cities are the most popular destinations for the top rated restaurants, and many other bits of information we can extract out of the data in front of us.
# 
# I've definitely skipped over some of the pieces of data that could be explored but what I've got is what I'm happy with so far. Needless to say there's plenty of opportunity to explore some more things down the road, and if you find something interesting yourself, hit me up and we can chat about it!
# 
# ## Table of Contents:
#  - [Importing the Data](#Importing-the-Data)
#  - [Exploring the Data](#Exploring-the-Data)
#      - [Star Rating Distribution](#Star-Rating-Distribution-over-all-Business)
#      - [Cuisine Types](#Cuisine-Types)
#      - [Top Restaurants & Cities](#Top-Restaurants-&-Cities)
#      - [Mapping things out](#Mapping-it-out)

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
pd.set_option("display.max_columns", None)

import plotly.offline as pyo
from plotly.offline import iplot, plot
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pyo.init_notebook_mode(connected=True)
pio.renderers.default = "notebook_connected"

import config

print("Setup Complete.")


# ### Importing the Data

# In[2]:


# reading in data
business_df = pd.read_csv('../data/can_yelp_businesses.csv')
reviews_df = pd.read_csv('../data/can_yelp_reviews.csv')


# In[3]:


print(business_df.shape)
business_df.head()


# In[4]:


print(reviews_df.shape)
reviews_df.sample(5)


# ### Exploring the Data
# 
# #### Star Rating Distribution over all Business
# 
# Now that we've got our data loaded in let's check out the distribution of the ratings for businesses.

# In[5]:


x = business_df['stars'].value_counts().index
y = business_df['stars'].value_counts().values

colors = ['#f72585', '#b5179e', '#7209b7', '#560bad', '#480ca8', '#3a0ca3', '#3f37c9', '#4361ee', '#4895ef']

fig = go.Figure(data=[go.Bar(
            x=x,
            y=y,
            text=y,
            textposition='auto',
            marker={'color':colors}
)])
fig.update_layout(title="Star Rating Distribution",
                 xaxis_title="Star Rating",
                 yaxis_title="Count",
                 )
fig.show()


# #### Cuisine Types
# 
# Check distribution of types of cuisine

# In[6]:


# getting the categories
print(business_df['categories'].value_counts())


# In[7]:


biz_category = ' '.join(business_df['categories'])
biz_cat = biz_category.split(',')

biz_category_df = pd.DataFrame(biz_category.split(','), columns=['category'])

print(biz_category_df.category.value_counts())


# In[8]:


# plotly version

x = biz_category_df.category.value_counts(ascending=False)
top_20 = x.iloc[:20]

fig = px.bar(top_20, x=top_20.values, y=top_20.index, text=top_20.values, orientation='h', 
             color=top_20.index, 
             color_discrete_sequence=px.colors.qualitative.Alphabet_r)
fig.update_layout(xaxis=dict(
        title="Count", 
        titlefont=dict(size=16)), 
                  yaxis=dict(
                      title="Business Category", 
                      titlefont=dict(size=16)),
                 height=700,
                 width=1000,
                 title="Top 20 Business Categories",
                 )
fig.show()


# #### Top Restaurants & Cities
# ##### By Review Count, Ratings & # of Restaurants
# 
# Let's have a look at which restaurants are the most reviewed

# In[9]:


business_df[['name', 'stars', 'review_count', 'city']].sort_values(by="review_count", ascending=False)[:50]


# Which city has the most reviews & the highest average rating?

# In[10]:


business_df[['name', 'stars', 'review_count', 'city']].groupby(['city']).agg({'review_count': 'sum', 'stars': 'mean'}).sort_values(by="review_count", ascending=False)[:50]


# Vancouver dominates the restaurant industry in BC clearly, with 47 out of the top 50 restaurants.

# Checking the number of businesses in each city.

# In[11]:


business_df[['city', 'business_id']].groupby(['city'])['business_id'].agg('count').sort_values(ascending=False)


# Now we can see why Vancouver was the city with the most reviews, it's got the most restaurants by quite a large margin!

# **Improving the grammatical cosmetics**
# 
# There's some city names that are weirdly spelled. We'll have to fix that so we have proper counts of restaurants in each city.

# In[12]:


business_df['city'] = business_df['city'].replace(['New Westminister', 'NEW WESTMINSTER', 'Newwestminster'], 'New Westminster')
business_df['city'] = business_df['city'].replace(['BURNABY'], 'Burnaby')
business_df['city'] = business_df['city'].replace(['SURREY'], 'Surrey')
business_df['city'] = business_df['city'].replace(['PORT COQUITLAM', 'Port coquitlam'], 'Port Coquitlam')
business_df['city'] = business_df['city'].replace(['RICHMOND', 'RichMond'], 'Richmond')
business_df['city'] = business_df['city'].replace(['N Vancouver'], 'North Vancouver')


# In[13]:


business_df['city'].value_counts()


# **Some more naming errors to take care of...**
# 
# Let's rename the "Downtown Vancouver" location to just "Vancouver". Clean up "Greater Vancouver A" to "Greater Vancouver". There's a possibility that "Greater Vancouver" is just "North Vancouver" but we'll leave that thought aside for now and not look into it too much.

# In[14]:


business_df['city'] = business_df['city'].replace(['Greater Vancouver A'], 'Greater Vancouver')
business_df['city'] = business_df['city'].replace(['Downtown Vancouver'], 'Vancouver')


# In[15]:


business_df[['city', 'business_id']].groupby(['city'])['business_id'].agg('count').sort_values(ascending=False)


# In[16]:


cities = business_df['city'].value_counts()

fig = px.bar(cities, x=cities.values, y=cities.index, text=cities.values, orientation='h', color=cities.index, color_discrete_sequence=px.colors.sequential.Agsunset)
fig.update_layout(xaxis=dict(
        title="Count", 
        titlefont=dict(size=16)), 
                  yaxis=dict(
                      title="City", 
                      titlefont=dict(size=16)),
                 height=700,
                 width=1000,
                 title="Number of Businesses per City")
fig.show()


# Since the city names were fixed, let's see the average number of stars and the total review count for each city again

# In[17]:


business_df[['name', 'stars', 'review_count', 'city']].groupby(['city']).agg({'review_count': 'sum', 'stars': 'mean'}).sort_values(by="review_count", ascending=False)[:50]


# Check the highest average rating per cuisine type

# In[18]:


category_stars_df = business_df[['categories', 'stars']]
category_stars_df.sample(5)


# In[19]:


category_stars_df[['categories', 'stars']].groupby(['categories'])['stars'].agg('mean').sort_values(ascending=False)


# In[20]:


category_stars_df.shape


# **Top 50 most reviewed restaurants**

# In[21]:


top_50 = business_df[['name', 'stars', 'review_count', 'city']].sort_values(ascending=False, by="review_count")[:50]
top_50.head()


# #### Mapping it out
# 
# What I would like to do next is visualize the highest ratings by review count in a map to be able to see where the most popular areas are. To do this, I've found that Plotly Mapbox is a great tool that renders a really clean map showing every distinct point that we need.

# In[41]:


px.set_mapbox_access_token(config.mapbox_access_token)
token = config.mapbox_access_token
fig = px.scatter_mapbox(data_frame=business_df, lat='latitude', lon='longitude',
                        color='stars', size='review_count', hover_name='name',
                        color_continuous_scale=px.colors.cyclical.IceFire)
fig.update_layout(mapbox_style="carto-positron", mapbox_accesstoken=token)
fig.show(renderer="notebook_connected");


# In[23]:


import gmaps
import gmaps.datasets


# In[24]:


gmaps.configure(api_key=config.gmaps_api_key)


# In[25]:


lat = business_df['latitude'].values
long = business_df['longitude'].values
rest_locations = list(zip(lat, long))
fig = gmaps.figure()
rest_map = gmaps.heatmap_layer(rest_locations)
fig.add_layer(rest_map)
fig


# **Clustering**
# 
# Let's add some points on the map above that show the main centroids (k-means clustering) of where the hot spots for restaurants are. we have to import k-means from scikit-learn first and then we'll create a clustering function and add that as a layer on the map.

# In[26]:


from sklearn.cluster import KMeans


# In[27]:


def k_rest_clusters(k):
    """Use KMeans algorithm to find k clusters of restaurants"""
    kmeans = KMeans(n_clusters=k).fit(rest_locations)
    clusters = kmeans.cluster_centers_
    return clusters


# In[28]:


kmeans_rest = k_rest_clusters(6)
kmeans_rest


# Adding the centroids to the Google Map above.

# In[29]:


cluster_centers_layer = gmaps.symbol_layer(kmeans_rest, fill_color='black', stroke_color='blue', scale=5)
fig.add_layer(cluster_centers_layer)
fig


# We can do some more visualizations to get more info but I'll stop for now. Next I'll do NLP analysis on the reviews dataset, analyze sentiment & polarity, visualize words for positive and negative reviews in a wordcloud. Maybe do some topic modeling (LDA).

# In[30]:


list_cat = [category.split(',') for category in business_df['categories']]
print(list_cat[:20])


# In[31]:


list_cat[:25]


# In[32]:


business_df['rest_categories'] = list_cat


# In[33]:


slim_biz_df = business_df[['name', 'stars', 'rest_categories']]
slim_biz_df.head()


# In[34]:


slim_biz_df['rest_categories'][55]


# In[35]:


# the following function needs a HUGE THANK YOU to 'victorchennn' on github
# I was stuck on trying to separate the word 'Restaurants' from the categories
# column for a while until I came across his code, so thank you to him for making
# that code available!

def true_cat_count(data):
    categories = {}
    for row in data.index:
        stars = data.loc[row,]['stars']
        for cat in data.loc[row,]['rest_categories']:
            if cat not in ['Restaurants', ' Restaurants']:
                if cat in categories:
                    categories[cat].append(stars)

                else:
                    categories[cat] = [stars]
    true_categories = pd.DataFrame({'stars':list(categories.values())})
    true_categories.index = categories.keys()
    true_categories['number'] = true_categories['stars'].apply(lambda c: len(c))
    true_categories['percentage'] = true_categories['number'] / len(data) * 100
    true_categories['avg_stars'] = true_categories['stars'].apply(lambda s: sum(s) / len(s))
    true_categories = true_categories.drop(['stars'], axis=1)

    return true_categories


# In[36]:


category_count = true_cat_count(slim_biz_df)
top_20_cat = category_count.sort_values('number', ascending=False).head(20)
top_20_cat


# In[37]:


fig = px.bar(top_20_cat, x=top_20_cat.number, y=top_20_cat.index, text=top_20_cat.number, orientation='h', 
             color=top_20_cat.index, 
             color_discrete_sequence=px.colors.qualitative.Alphabet_r)
fig.update_layout(xaxis=dict(
        title="Count", 
        titlefont=dict(size=16)), 
                  yaxis=dict(
                      title="Business Category", 
                      titlefont=dict(size=16)),
                 height=700,
                 width=1000,
                 title="Top 20 Business Categories",
                 )
fig.show()


# The above code is quite messy and dirty. I tried a few different methods to turn the categories column into a list and then add that into the dataframe but the one I settles on was the result directly above. Moving on the visualizing the top 50 

# In[38]:


top_50_cat = category_count.sort_values('number', ascending=False).head(50)
top_50_cat


# In[39]:


fig = px.bar(top_50_cat, x=top_50_cat.number, y=top_50_cat.index, text=top_50_cat.number, orientation='h', 
             color=top_50_cat.index, 
             color_discrete_sequence=px.colors.qualitative.Alphabet_r)
fig.update_layout(xaxis=dict(
        title="Count", 
        titlefont=dict(size=16)), 
                  yaxis=dict(
                      title="Business Category", 
                      titlefont=dict(size=16)),
                 height=700,
                 width=1000,
                 title="Top 50 Business Categories",
                 )
fig.show()


# In[50]:




# In[ ]:




