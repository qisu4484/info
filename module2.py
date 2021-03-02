#!/usr/bin/env python
# coding: utf-8

# Assignment Two:Data Three Ways <br>
# Qinglu Sun

# In the gaming industry, new platforms and new video games have been developed, sometimes people wish to purchase video games on different platforms other than pc since PC is more expensive than video game consoles, PC games are also more expensive than consoles games, video game consoles save money, save trouble such as there is no need to pay attention to the operating system or to update the driver. Video game consoles including play station 2 is released on March 2000, xbox is released on November,2001, xbox 360 is released on November 2005, play station 3 is released on November,2006, play station 4 and xbox one is relased on November,2013. When the new video games consoles is constantly updated and there is over 160 million adults in the united states plays video games, my central question is what are the factors that may influence games sales? I wanted to explore what is the total number of NA_sales and global sales each year among with what type of game is the most popular in general, if sales decreasing, why so, and what's the relationship between user's score and global sales. Is the better the game sales, the higher the user score? Since Xbox and play station and other new systems are released around 2015, what are the best-selling games of the year of 2015 in United States? I am going to create my visulazations based on the dataset i found on kaggle https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings which has the columns of developer, year of release, name of the game, platform, genre, sales with different areas where all sales are in millions of units, critic score by meatacritic staff, number of crities used, user score, number of users who gave the user score and ESRB rating. Since the dataset covers from 1980 to 2016, and the total number of rows is 16719 where altair only supports with 5000 rows, i am going to first explore what is the best selling video games of 2015 in US and compare my results to https://venturebeat.com/2016/01/14/2015-npd-the-10-best-selling-games-of-the-year/ and https://www.gamespot.com/articles/top-ten-best-selling-us-games-of-2015-and-december/1100-6433845/ to discover whether or not my results matches with their statement of best selling game in 2015, then clean the dataframe a little so the number of rows will not exceed the limit of altair including drop all nan in the dataframe and set the released date for video game time window from 2005-2016 to explore popular genres, relationship between user score and sales and etc. 

# In[1]:


import pandas as pd
import altair as alt
import streamlit as st
st.write("""

Assignment Two:Data Three Ways

Qinglu Sun

In the gaming industry, new platforms and new video games have been developed, sometimes people wish to purchase video games on different platforms other than pc since PC is more expensive than video game consoles, PC games are also more expensive than consoles games, video game consoles save money, save trouble such as there is no need to pay attention to the operating system or to update the driver. Video game consoles including play station 2 is released on March 2000, xbox is released on November,2001, xbox 360 is released on November 2005, play station 3 is released on November,2006, play station 4 and xbox one is relased on November,2013. When the new video games consoles is constantly updated and there is over 160 million adults in the united states plays video games, my central question is what are the factors that may influence games sales? I wanted to explore what is the total number of NA_sales and global sales each year among with what type of game is the most popular in general, if sales decreasing, why so, and what's the relationship between user's score and global sales. Is the better the game sales, the higher the user score? Since Xbox and play station and other new systems are released around 2015, what are the best-selling games of the year of 2015 in United States? I am going to create my visulazations based on the dataset i found on kaggle https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings which has the columns of developer, year of release, name of the game, platform, genre, sales with different areas where all sales are in millions of units, critic score by meatacritic staff, number of crities used, user score, number of users who gave the user score and ESRB rating. Since the dataset covers from 1980 to 2016, and the total number of rows is 16719 where altair only supports with 5000 rows, i am going to first explore what is the best selling video games of 2015 in US and compare my results to https://venturebeat.com/2016/01/14/2015-npd-the-10-best-selling-games-of-the-year/ and https://www.gamespot.com/articles/top-ten-best-selling-us-games-of-2015-and-december/1100-6433845/ to discover whether or not my results matches with their statement of best selling game in 2015, then clean the dataframe a little so the number of rows will not exceed the limit of altair including drop all nan in the dataframe and set the released date for video game time window from 2005-2016 to explore popular genres, relationship between user score and sales and etc.

![alt text](https://raw.githubusercontent.com/qisu4484/info/main/visualization.png "1")

The top 10 best selling games in NA for all new games released in 2015 among all platforms is Call of Duty: Black Ops 3, Madden NFL 16, NBA 2k16, Fallout 4, Star Wars Battle front, Fifa 16, Halo5, Gears of War: Ultimate Edition, Mortal Kombat X and Batman: Arkham Knight, compares to https://venturebeat.com/2016/01/14/2015-npd-the-10-best-selling-games-of-the-year/, and https://www.gamespot.com/articles/top-ten-best-selling-us-games-of-2015-and-december/1100-6433845/ 7/10 matches, the other three are minecraft which is released 2013, Grand Theft Auto V which is released 2014 on XOne and Call of Duty: Advanced Warfare is also released 2014 on Xone. Where the category for Call of Duty: Black Ops 3 is Shooter, the category for Madden NFL 16 is Sports, the category for NBA 2k16 is Sports, the category for Fallout 4 is Role-playing, the category for Star Wars Battle front is Shooter, the category for Fifa 16 is Sports, the category for Halo 5: Guardians is Shooter,the category for Gears of War: Ultimate Edition is Shooter,the category for Mortal Kombat X is Fighting, the category for Batman: Arkham Knight is Action. My hypothesis so far may be that action, fighting, role-playing, shooter and sports are popular vdieo game categories.

![alt text](https://raw.githubusercontent.com/qisu4484/info/main/visualization%20(1).png "2")

From 2005, the global sales keep increasing where in 2008, the global sales for all video games reach the peak and start decreasing until 2016(Since i only have data until 2016), put aside mobile games, virtual reality, mobile, and arcade, if we only consider video game sells for PC, handhelds and consoles, In 
https://en.wikipedia.org/wiki/Video_game_industry#2000s, we also saw the trend that the video game sales increases from 2005 and reaches a peak in 2008 and starts decreasing until 2016, this may be due to the rise of mobile gaming as mentioned in the article. Nowadays, the penetration rate of smartphones is high and the configuration is not bad for video games. Mobile games are more convenient, portable and fast. You can also play together when you have a party with friends. In modern society, many people may not use computers but they must have bought mobile phones. This may one of the reasons that the video game sales for PC, handhelds and consoles are decreasing.





	""")

# In[2]:


df=pd.read_csv("https://raw.githubusercontent.com/qisu4484/info/main/Video_Games_Sales_as_at_22_Dec_2016.csv")


# In[3]:


df_year=df[df.Year_of_Release==2015]
game= df_year.groupby(['Name','Genre']).sum().reset_index()
popular_games=game.sort_values(by=['NA_Sales'],ascending=False)[:10]


# In[4]:


alt.Chart(popular_games).mark_bar().encode(
   alt.X('NA_Sales'),
   alt.Y('Name', sort=alt.EncodingSortField(field="NA_Sales", order='descending')),color="Genre")


# The top 10 best selling games in NA for all new games released in 2015 among all platforms is Call of Duty: Black Ops 3, Madden NFL 16, NBA 2k16, Fallout 4, Star Wars Battle front, Fifa 16, Halo5, Gears of War: Ultimate Edition, Mortal Kombat X and Batman: Arkham Knight, compares to https://venturebeat.com/2016/01/14/2015-npd-the-10-best-selling-games-of-the-year/, and https://www.gamespot.com/articles/top-ten-best-selling-us-games-of-2015-and-december/1100-6433845/ 7/10 matches, the other three are minecraft which is released 2013, Grand Theft Auto V which is released 2014 on XOne and Call of Duty: Advanced Warfare is also released 2014 on Xone. Where the category for Call of Duty: Black Ops 3 is Shooter, the category for Madden NFL 16 is Sports, the category for NBA 2k16 is Sports, the category for Fallout 4 is Role-playing, the category for Star Wars Battle front is Shooter, the category for Fifa 16 is Sports, the category for Halo 5: Guardians is Shooter,the category for Gears of War: Ultimate Edition is Shooter,the category for Mortal Kombat X is Fighting, the category for Batman: Arkham Knight is Action. My hypothesis so far may be that action, fighting, role-playing, shooter and sports are popular vdieo game categories.

# In[5]:


df=df.dropna()


# In[6]:


df=df[(df.Year_of_Release<=2016)&(df.Year_of_Release>=2005)]


# In[7]:


sum_Year= df.groupby('Year_of_Release').sum().reset_index()


# In[8]:


sum_Year['Year_of_Release'] = sum_Year['Year_of_Release'].astype(int) 


# In[9]:


alt.Chart(sum_Year).mark_line().encode(
    x=alt.X('Year_of_Release', axis=alt.Axis(tickCount=sum_Year.shape[0], grid=False)),
    y='Global_Sales'
)


# From 2005, the global sales keep increasing where in 2008, the global sales for all video games reach the peak and start decreasing until 2016(Since i only have data until 2016), put aside mobile games, virtual reality, mobile, and arcade, if we only consider video game sells for PC, handhelds and consoles, In 
# https://en.wikipedia.org/wiki/Video_game_industry#2000s, we also saw the trend that the video game sales increases from 2005 and reaches a peak in 2008 and starts decreasing until 2016, this may be due to the rise of mobile gaming as mentioned in the article. Nowadays, the penetration rate of smartphones is high and the configuration is not bad for video games. Mobile games are more convenient, portable and fast. You can also play together when you have a party with friends. In modern society, many people may not use computers but they must have bought mobile phones. This may one of the reasons that the video game sales for PC, handhelds and consoles are decreasing.

# In[10]:


selection = alt.selection(type="multi", fields=['Genre'])

alt.Chart(df).properties(width=250, height=250).mark_circle().encode(
    x='sum(Global_Sales)',
    y='mean(User_Score)',
    size='sum(Global_Sales)',
    tooltip=['Genre', 'mean(User_Score)'],
    color=alt.condition(selection, 'Genre', alt.value('lightgray'))
).add_selection(selection)| alt.Chart(df).properties(width=250, height=250).mark_bar(color="darkgray").encode(
    x=alt.X('User_Score', bin=alt.Bin(maxbins=30)),
    y='count()',
).transform_filter(selection)

st.write("""

In general, there are 1059220 users who gave the user score, among all those user scores, about 750 of user score are between 7-7.5,900 of user score are between 7.5-8, about 800 of user score are between 8-8.5, about 450 of user score are between 8.5-9 and about 100 of user score are 9-9.5 which is extremely high user score for a game, overall the bar chart is a left-skewed distribution where the majority of the user score is above 5-5.5, for games that are action category has most global_sales around 900, for games that are shooter and sports category has global_sales around 600, and misc, racing, role-playing has global sales around 300 million, the least popular genres are strategy, adventure, and puzzle. Where action games have mean of user score of 7(6.98), shooter have mean of user score of 7(6.90), sports have the lowest mean of user score of 6.70, where puzzle, fighting, role-playing, platform, adventure have mean of user score above 7. In Action, shooter, sport, misc, simulation, fighting and puzzle genre, the most frequent user score is 7.5-8, in racing genre, the most frequent user score is 7-7.5, in strategy, platform and adventure genre, the most frequent user score is 8-8.5. Which indicates even though the global sales for action, shooter sports are higher, but there are good and bad games mixed in the category where are in strategy and adventure games, there might be more good games in terms of ratio. Which the above figure also confirmed my hypothesis of action, shooter and sports are popular video game categories.<br>
By exploring the data frame and visualizations, there are many factors that may influence games sales including the genres of the game, the rise of mobile game which leads to decreases to games that works only on PC, handhelds and consoles as mobile phones are getting more and more common and the update of mobile phones is getting faster and faster,and it is more convenient to play games on mobile phones, however the user score doesn't really influence game sales according to this visualizations, there isn't a clear sign of correlation between mean user score for a genre and sum of global sales for a genre since i didn't see how global sales affected user score or user score affected global sales. In the future we may also explore the relationship between ESRB ratings and global sales, developer and global sales.

Extra Stuff:


![alt text](https://raw.githubusercontent.com/qisu4484/info/main/visualization%20(3).png "3")

The developer of the game also influence global sales




	""")

# In general, there are 1059220 users who gave the user score, among all those user scores, about 750 of user score are between 7-7.5,900 of user score are between 7.5-8, about 800 of user score are between 8-8.5, about 450 of user score are between 8.5-9 and about 100 of user score are 9-9.5 which is extremely high user score for a game, overall the bar chart is a left-skewed distribution where the majority of the user score is above 5-5.5, for games that are action category has most global_sales around 900, for games that are shooter and sports category has global_sales around 600, and misc, racing, role-playing has global sales around 300 million, the least popular genres are strategy, adventure, and puzzle. Where action games have mean of user score of 7(6.98), shooter have mean of user score of 7(6.90), sports have the lowest mean of user score of 6.70, where puzzle, fighting, role-playing, platform, adventure have mean of user score above 7. In Action, shooter, sport, misc, simulation, fighting and puzzle genre, the most frequent user score is 7.5-8, in racing genre, the most frequent user score is 7-7.5, in strategy, platform and adventure genre, the most frequent user score is 8-8.5. Which indicates even though the global sales for action, shooter sports are higher, but there are good and bad games mixed in the category where are in strategy and adventure games, there might be more good games in terms of ratio. Which the above figure also confirmed my hypothesis of action, shooter and sports are popular video game categories.<br>
# By exploring the data frame and visualizations, there are many factors that may influence games sales including the genres of the game, the rise of mobile game which leads to decreases to games that works only on PC, handhelds and consoles as mobile phones are getting more and more common and the update of mobile phones is getting faster and faster,and it is more convenient to play games on mobile phones, however the user score doesn't really influence game sales according to this visualizations, there isn't a clear sign of correlation between mean user score for a genre and sum of global sales for a genre since i didn't see how global sales affected user score or user score affected global sales. In the future we may also explore the relationship between ESRB ratings and global sales, developer and global sales.

# Extra Stuff:

# In[11]:


developer= df.groupby(['Developer']).sum().reset_index()
df_developer=developer.sort_values(by=['Global_Sales'],ascending=False)[:10]
alt.Chart(df_developer).mark_bar().encode(
   alt.X('Global_Sales'),
   alt.Y('Developer', sort=alt.EncodingSortField(field="Global_Sales", order='descending')))


# The developer of the game also influence global sales

# In[ ]:




