#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:13:20 2024

@author: Nlowie Mohammed Iddrisu, GSSTI, DARA
"""

import pandas as pd

#Mov_Dat = Movie Data
Mov_Dat= pd.read_csv("movie_dataset.csv")
Mov_Dat

df = pd.DataFrame(Mov_Dat)
df

#print("Original DataFrame:")
print(df)


 # Show all columns, rows and adjusted with of DataFrame
 
# Clean column names: remove leading/trailing spaces and replace spaces with underscores
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Updated DataFrame 
print("\nUpdated DataFrame:")
print(df)


"""
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Adjust to fit the width of your console
pd.set_option('display.max_rows', None) 
"""

#Col_dropped = column without values dropped

Data_cleaned = df.dropna(axis=0)
Data_cleaned

#1. Highest rating
"""High_rate = Data_cleaned['Rating'].max()
print(Data_cleaned['Title'], 'High_rate')
"""

#2. Average Revenue 
"""Avg_Rev = Data_cleaned['Revenue_(Millions)'].mean()
print('Average revenue is:', Avg_Rev)
"""

#3. Average revenue of movies from 2015 to 2017 in the dataset
"""
movies_2015_to_2017 = Data_cleaned[(Data_cleaned['Year'] >= 2015) & (Data_cleaned['Year'] <= 2017)]
average_revenue_2015_to_2017 = movies_2015_to_2017['Revenue_(Millions)'].mean()
print("Average Revenue of Movies from 2015 to 2017: ", average_revenue_2015_to_2017)
"""


# 4. movies released in the year 2016? 
"""
movies_2016 = df[df['Year'] == 2016]
count_movies_2016 = movies_2016.shape[0]
print( "Number of Movies Released in 2016", count_movies_2016 )
"""

#5. How many movies were directed by Christopher Nolan?
"""
nolan_movies = Data_cleaned[Data_cleaned['Director'] == 'Christopher Nolan']
count_nolan_movies = nolan_movies.shape[0]
print( "Movies Directed by Christopher Nolan", count_nolan_movies)
"""

#6. How many movies in the dataset have a rating of at least 8.0?
"""
high_rated_movies = df[df['Rating'] >= 8.0]
count_high_rated_movies = high_rated_movies.shape[0]

print("Number of Movies with Rating of at least 8.0 is " , count_high_rated_movies)
"""


# 7. What is the median rating of movies directed by Christopher Nolan?
"""
median_nolan_rating = nolan_movies['Rating'].median()
print("Median Rating of Movies Directed by Christopher Nolan is", median_nolan_rating)
"""

# 8 Find the year with the highest average rating.
"""
avg_rating_by_year = Data_cleaned.groupby('Year')['Rating'].mean()
year_highest_avg_rating = avg_rating_by_year.idxmax()
highest_avg_rating = avg_rating_by_year.max()
print(f"Year with the Highest Average Rating: {year_highest_avg_rating} with a rating of {highest_avg_rating:.2f}")
"""


# 9. Percentage increase in number of movies made between 2006 and 2016
"""
movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 =df[df['Year'] == 2016].shape[0]

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(f"Percentage Increase in Number of Movies Made between 2006 and 2016: {percentage_increase:.2f}%")
"""


# 10. Find the most common actor in all the movies
"""
all_actors = Data_cleaned['Actors'].str.split(',').explode().str.strip()
most_common_actor = all_actors.value_counts().idxmax()
print("Most Common Actor is", most_common_actor)
"""

#11. How many unique genres are there in the dataset?
"""
unique_genres = Data_cleaned['Genre'].str.split(',').explode().str.strip().nunique()
print("Number of Unique Genres is", unique_genres)
"""
# Select only numeric columns for correlation
"numeric_df = Data_cleaned.select_dtypes(include=['number'])"

# Calculate the correlation matrix for the cleaned numeric columns
"""
correlation_matrix = numeric_df.corr()
print(correlation_matrix)
"""