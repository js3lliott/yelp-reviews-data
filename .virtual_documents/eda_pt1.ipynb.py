import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic("matplotlib", " inline")
sns.set()
pd.set_option("display.max_columns", None)

import plotly.offline as pyo
from plotly.offline import iplot, plot
import plotly.graph_objs as go
import plotly.express as px
pyo.init_notebook_mode()

print("Setup Complete.")


# reading in data
business_df = pd.read_csv('data/can_yelp_businesses.csv')
reviews_df = pd.read_csv('data/can_yelp_reviews.csv')


print(business_df.shape)
business_df.head()


print(reviews_df.shape)
reviews_df.sample(5)


# business star distribution
plt.figure(figsize=(10, 8))
ax = sns.barplot(x=business_df['stars'].value_counts().index, y=business_df['stars'].value_counts().values, alpha=0.8)
plt.title("Star Rating Distribution")
plt.ylabel("Number of Businesses", fontsize=12)
plt.xlabel("Star Rating", fontsize=12)

plt.show();


import plotly.io as pio
pio.renderers.default = 'jupyterlab'


x = business_df['stars'].value_counts().index
y = business_df['stars'].value_counts().values

fig = go.Figure(data=[go.Bar(
            x=x,
            y=y,
            text=y,
            textposition='auto'
)])
fig.update_layout(title="Star Rating Distribution")
fig.show()


# getting the categories
print(business_df['categories'].value_counts())


biz_category = ' '.join(business_df['categories'])
biz_cat = biz_category.split(',')

biz_category_df = pd.DataFrame(biz_category.split(','), columns=['category'])

print(biz_category_df.category.value_counts())


x = biz_category_df.category.value_counts(ascending=False)
top_20 = x.iloc[:20]

fig, ax = plt.subplots(figsize=(12, 10))
sns.barplot(x=top_20.values, y=top_20.index, alpha=0.8, orient='h')
ax.set_title("Top 20 Business Categories")
ax.set_ylabel("Business Categories")
ax.set_xlabel("Count")
plt.show();


# plotly version
fig = px.bar(top_20, x=top_20.values, y=top_20.index, text=top_20.values, orientation='h')
fig.update_layout(xaxis=dict(
        title="Count", 
        titlefont=dict(size=16)), 
                  yaxis=dict(
                      title="Business Category", 
                      titlefont=dict(size=16)),
                 height=700,
                 width=1200)
fig.show()


business_df.head()


business_df[['name', 'stars', 'review_count', 'city']].sort_values(ascending=False, by="review_count")[:50]


business_df[['city', 'business_id']].groupby(['city'])['business_id'].agg('count').sort_values(ascending=False)


business_df['city'] = business_df['city'].replace(['New Westminister', 'NEW WESTMINSTER', 'Newwestminster'], 'New Westminster')
business_df['city'] = business_df['city'].replace(['BURNABY'], 'Burnaby')
business_df['city'] = business_df['city'].replace(['SURREY'], 'Surrey')
business_df['city'] = business_df['city'].replace(['PORT COQUITLAM', 'Port coquitlam'], 'Port Coquitlam')
business_df['city'] = business_df['city'].replace(['RICHMOND', 'RichMond'], 'Richmond')
business_df['city'] = business_df['city'].replace(['N Vancouver'], 'North Vancouver')


business_df['city'].value_counts()


business_df[['city', 'business_id']].groupby(['city'])['business_id'].agg('count').sort_values(ascending=False)


cities = business_df['city'].value_counts()

fig = px.bar(cities, x=cities.values, y=cities.index, text=cities.values, orientation='h')
fig.update_layout(xaxis=dict(
        title="Count", 
        titlefont=dict(size=16)), 
                  yaxis=dict(
                      title="City", 
                      titlefont=dict(size=16)),
                 height=700,
                 width=1200,
                 title="Number of Businesses per City")
fig.show()



