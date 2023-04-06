#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:47:59 2023

@author: quintenachterberg
"""

import pandas as pd
import numpy as np
from scipy import stats
import scipy as scipy
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
from scipy.stats import shapiro



#Task A - import data
df = pd.read_csv('https://raw.githubusercontent.com/QuintenA802/MSR/main/1658049alienation_data.csv')
df.info()

#Task B - Summarize

    #1
    Mean = df["alienation"].mean()
    print(Mean)
    
    #2
    Median = df["alienation"].median()
    print(Median)
    
    #3
    print(df.alienation.max() - df.alienation.min())
    
    #4
    print(df['alienation'].std())
    
    #5
    df.hist(column='alienation')
    ax = df.hist(column='alienation', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
    
    #6
    # To test if the distribution is normal I performed a Shapiro Wilk Test. This indicated if the data of distributed normally or not.
    stats.shapiro(df["alienation"])
    
    # Shapiro conclusion:
    #   In the output, the p-value is 7.910952263046056e-05, which can be written as 0.00007910952263046056 in decimal notation. 
    #   This value is very small, which suggests strong evidence against the null hypothesis of normality. 
    #   In summary, the p-value is less than or equal to 0.05, so the data is not considered to be normally distributed.

    
    #7
    
    # Selecting only the rows where the 'male' column equals 1
    male_df = df[df['male'] == 1]
    
    # Now following the same steps from 1 till 6
    
    #Mean
    MeanMale = male_df["alienation"].mean()
    print(MeanMale)
    
    #Median
    MedianMale = male_df["alienation"].median()
    print(MedianMale)
    
    #Range 
    print(male_df.alienation.max() - male_df.alienation.min())
    
    #Standard deviation
    print(male_df['alienation'].std())
    
    #Historgram
    male_df.hist(column='alienation')
    ax = male_df.hist(column='alienation', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
    
    #Shapiro test
    stats.shapiro(male_df["alienation"])
    
    # Shapiro conclusion:
    #   In the output, the p-value is 0.016140352934598923.
    #   This value below the significant level of 0.05. It has strong evidence against the null hypothesis of normality, 
    #       and therefore the null hypothesis is rejected and there can be concluded that the distribution is not normal.

    
    
    # Selecting only the rows where the 'male' column equals 0. This shall mean "otherwise respondents". With this it probabliy means females.
    female_df = df[df['male'] == 0]
    
    # Now following the same steps from 1 till 6
    
    #Mean
    MeanFemale = female_df["alienation"].mean()
    print(MeanFemale)
    
    #Median
    MedianFemale = female_df["alienation"].median()
    print( MedianFemale)
    
    #Range 
    print(female_df.alienation.max() - female_df.alienation.min())
    
    #Standard deviation
    print(female_df['alienation'].std())
    
    #Historgram
    female_df.hist(column='alienation')
    ax = female_df.hist(column='alienation', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)

    #Shapiro test
    stats.shapiro(female_df["alienation"])

    # Shapiro conclusion:
    #   In the output, the p-value is 0.0012771572219207883.
    #   This value below the significant level of 0.05. It has strong evidence against the null hypothesis of normality, 
    #       and therefore the null hypothesis is rejected and there can be concluded that the distribution is not normal.
    
 
    
    #What are there differences?
    #   The differences can be seen in the Mean, Median and Standard Deviation. Please read the table below:
    differences_task7 = pd.read_csv('https://raw.githubusercontent.com/QuintenA802/MSR/main/Differences%20-%20task%20B.7.csv')
    differences_task7
  
    
  
    
   #8 - the same for income
    
   #Mean
    MeanIncome = df["income"].mean()
    print(MeanIncome)
    
    #Median
    MedianIncome = df["income"].median()
    print(MedianIncome)
    
    #Range 
    print(df.income.max() - df.income.min())
    
    #Standard deviation
    print(df['income'].std())
    
    #Historgram
    df.hist(column='income')
    ax = df.hist(column='income', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
    
    #Shapiro test
    # To test if the distribution is normal I performed a Shapiro Wilk Test. This indicated if the data of distributed normally or not.
    stats.shapiro(df["income"])
    
    # Shapiro conslusion:
    #   The Shapiro-Wilk test gives a p-value of 1,which means that the data is normally distributed. 
    
    

    # Selecting only the rows where the 'male' column equals 1
    male_df = df[df['male'] == 1]
    
    # Now following the same steps from 1 till 6
    
    #Mean
    MeanMaleIncome = male_df["income"].mean()
    print(MeanMaleIncome)
    
    #Median
    MedianMaleIncome = male_df["income"].median()
    print(MedianMaleIncome)
    
    #Range 
    print(male_df.income.max() - male_df.income.min())
    
    #Standard deviation
    print(male_df['income'].std())
    
    #Historgram
    male_df.hist(column='income')
    ax = male_df.hist(column='income', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)
    
    #Shapiro test
    stats.shapiro(male_df["income"])
    
    # Shapiro conclusion:
    #   The Shapiro-Wilk test gives a p-value of 1,which means that the data is normally distributed. 
    
    
    
    # Selecting only the rows where the 'male' column equals 0. This shall mean "otherwise respondents. With this it probabliy means females.
    female_df = df[df['male'] == 0]
    
    # Now following the same steps from 1 till 6
    
    #Mean
    MeanFemaleIncome = female_df["income"].mean()
    print(MeanFemaleIncome)
    
    #Median
    MedianFemaleIncome = female_df["income"].median()
    print(MedianFemaleIncome)
    
    #Range 
    print(female_df.income.max() - female_df.income.min())
    
    #Standard deviation
    print(female_df['income'].std())
    
    #Historgram
    female_df.hist(column='income')
    ax = female_df.hist(column='income', bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9)

    #Shapiro test
    stats.shapiro(female_df["income"])

    # Shapiro conclusion:
    #   The Shapiro-Wilk test gives a p-value of 0.03145295009016991, so it suggests that the data significantly deviates from a normal distribution. 
    #   Typically, a p-value less than 0.05 means that there is strong evidence to reject the null hypothesis of normality and accept the alternative hypothesis.
    #   So, the data is not normally distributed.
    
 
    #What are there differences?
    #   The differences everywhere when comparing males, females and combined. What stands out is that the range of income is shorter with females but have a higher median than men.
    differences_task8 = pd.read_csv('https://raw.githubusercontent.com/QuintenA802/MSR/main/Differences%20-%20task%20B.8.csv')
    differences_task8
    
    
    
    #9
    # For this value I decided to make it have an income equal to the income mean of 57920.6807
    # By doing this, the data is recognized as a number and does not influence the mean value after putting in the new value of this cell.

    
    #10
    #Only 3 people have sought psychological help
    
    #11   
    # define the counts for each group
    male_no_consult = int(df[(df['male'] == 1) & (df['consult'] == 0)]['male'].count())
    female_no_consult = int(df[(df['male'] == 0) & (df['consult'] == 0)]['male'].count())
    male_consult = int(df[(df['male'] == 1) & (df['consult'] == 1)]['male'].count())
    female_consult = int(df[(df['male'] == 0) & (df['consult'] == 1)]['male'].count())
    consult_only = int(df[df['consult'] == 1]['consult'].count())
    
    # plot the Venn diagram
    venn3(subsets=[male_no_consult, female_no_consult, 0, 0, male_consult, female_consult, consult_only],
          set_labels=('Male', 'Female', 'Consult'),
          set_colors=('skyblue', 'pink', 'orange'))
    plt.show()
          
    #12
    # 1 group can be formed if groups of 3 interviewees had to be formed from my sample of 100 respondents.
    # 0 group can be formed if groups of 3 interviewees had to be formed from my sample of 100 respondents, given that exactly one of the interviewees is male.
    # 1 group can be formed if groups of 3 interviewees had to be formed from my sample of 100 respondents, given that at least one of the interviewees is male.
   
#Task C - USD to EUR

    # Set the exchange rate
    exchange_rate = 0.91  # 1 USD = 0.91 EUR
    

    # convert USD to EUR
    df_euro = df.copy() # make a copy of the original dataset
    df_euro['income'] = df_euro['income'] * 0.91 # convert USD to EUR
    
   
    # print the new dataset
    print(df_euro)
    
    # mean and standard deviation of income in euro's
    MeanEUR = df_euro["income"].mean()
    print(MeanEUR)

    print(df_euro['income'].std())
    
    # mean and standard deviation of income in USD
    MeanUSD = df["income"].mean()
    print(MeanUSD)

    print(df['income'].std())

    # Overall, the mean and standard deviation of the euro is smaller. This is because of the exchange rate of 0.91. 
    # Basically, the mean and standard deviation of USD is multiplied by 0.91.    
    
#Task D - centered income
 
    df_centeredincome = df.copy() # make a copy of the original dataset
    df_centeredincome["centered_income"] = df_centeredincome["income"] - MeanUSD # Subtract the mean from each value in the income column
    
    # Calculate the mean and standard deviation of the centered_income column
    centered_income_mean = df_centeredincome["centered_income"].mean()
    centered_income_std = df_centeredincome["centered_income"].std()
    
    print("Mean of centered income:", centered_income_mean)
    print("Standard deviation of centered income:", centered_income_std)

    # The centered mean of income indicates the average of each person's income compared to the average income (non-centered). 
    # The mean of the centered income is negative, meaning that the average amount of people own less income than the non-centered mean.
    # Standard deviation remains the same.
    
#Task E - Alienation formula
    # To find the income level at which expected alienation is the same in both countries, we can set the two equations equal to each other and solve for income:

    # 5.56 - 0.073 * Income = 4.80 - 0.030 * Income

    # 0.043 * Income = 0.76

    # Income = 17.67

    # Therefore, the expected alienation in both countries is the same when the centered income is 17.67 (x1000) thousand US dollars.
    
    # For the first country: Alienation = 5.56 - 0.073 * 17.67 = 4.26

    # For the second country: Alienation = 4.80 - 0.030 * 17.67 = 4.26