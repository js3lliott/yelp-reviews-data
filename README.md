<img src="./images/yelp-banner.png" width="1200" height="500" class="center"> 

# Yelp Reviews Data Analysis

**Welcome!**

  First off, thanks for visiting this repository and exploring some of my work that I've put time and energy into! What you'll find in this project is an in-depth anaysis of Yelp reviews that explore attributes and aspects of popular and maybe not-so-popular restaurants covering the main metropolitan areas of British Columbia, Canada.
   
  The reason why this project only covers the BC metro areas is because as I was working on a project in Kaggle for Yelp reviews, I decided that I wanted to analyze just Canadian provinces/cities and what made the top foodie destinations unique in those cities. When breaking down and filtering the datasets, a unique insight came to light - BC was the only Canadian province represented in the data! I guess that at the time that this particular dataset collection was posted to Kaggle, their team must've only had observations from that province alone and not any others such as Ontario and Quebec. Eventually I decided not to pay attention to it too much and moved on, therefore this repository was born!
   
  The two main parts to this repository are the EDA notebook, and the NLP analysis. Each notebook takes a deep dive into either the business data or reviews data and explore what makes a restaurant popular, why restaurants receive a positive or negative review, and what features about a restaurant can we find out from its reviews.
   

## Exploratory Data Analysis 📊

[Check out the notebook here!](https://nbviewer.org/github/js3lliott/yelp-reviews-data/blob/main/nbs/eda_pt1.ipynb)

  In this notebook we clean and manipulate the data to explore both the business and reviews data using the usual suspects of pandas & plotly, to extract interesting facts and observations about the restaurants located in metro BC. We look into the overall distribution of ratings that are given to restaurants, what are the top categories of cuisine types, which cities have the most restaurants, as well as anything else we can squeeze out.


## NLP Exploratory Analysis 🗣

[Have a peak!](https://nbviewer.org/github/js3lliott/yelp-reviews-data/blob/main/nbs/Yelp_Review_NLP_Analysis.ipynb)

  This is where we get into the good stuff. This notebook digs into the weeds of anayzing the reviews from an NLP perspective. We start off with some light sentiment analysis on uncleaned reviews, utilizing VADER from the `nltk` library. This provides some insight into how the original reviews score, in regards to polarity. Wordclouds are created to visualize the most popular words within each sentiment category. Lastly, n-grams (unigrams, bigrams, and trigrams) are constructed & visualized and implemented topic modeling.


## Sentiment Analysis Classification 👍👎


  

## Resources:
**These resources were invaluable in creating and working through this project. Thank you to each author for making their code open source and freely available. This is what produces progress, and I hope that my work can eventually help others along their own development journey.**
- https://deepnote.com/@abid/Trip-Advisor-Data-AnalysisML-9gYLOddsRXmWSKVLyLX_tQ
- https://github.com/Vishwacorp/yelp_nlp
- https://www.kaggle.com/helalehalimohamadi/sentiment-analysis-of-yelp-reviews-nlp#Introduction
- https://nbviewer.org/github/susanli2016/NLP-with-Python/blob/master/EDA%20and%20visualization%20for%20Text%20Data.ipynb
- https://neptune.ai/blog/exploratory-data-analysis-natural-language-processing-tools