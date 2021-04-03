#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import altair as alt
import streamlit as st



import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex, Normalize
from matplotlib.patches import Polygon
from matplotlib.colorbar import ColorbarBase


# In[2]:
st.title('Module3')
st.write("""
    Qinglu Sun
    """)

st.write("""
    1.  After the COVID-19 epidemic spreads to the world, the dependence on the medical system is very high due to the number of COVID-19 positive and the proportion of severe cases. Whether it is an essential device for assisted breathing such as a ventilator or a nursing place such as ICU, it is not continuously produced.  There has been an extreme shortage of ventilators and increasing shortage of medical personnel. In some places, medical workers who have tested positive for the COVID-19 have to continue to work. In some places, the available beds for ICU once dropped to 0. Medical resources are in short supply, and equipment may be in short supply. The critical device may malfunction and there is no new equipment that can be replaced. Especially with the mutation of the new crown and in some cases, there are older population that may experience more severe symptoms than other age groups, it has exhausted the medical resources of the United States. My target problem is where are those areas that may suffer from those difficulties and overwhelmed by COVID-19 and is there relationships between the percent of individuals that are at high risk and the ICU beds in the area or the hospitals in the areas in order to prevent those problems such as the shortage of medical equipment and personnel using data visualizations to find out which areas may face these problems and deal with them in advance.
    """)

st.write("""
    2.  https://github.com/fivethirtyeight/data/tree/master/covid-geography, https://fivethirtyeight.com/features/how-one-high-risk-community-in-rural-south-carolina-is-bracing-for-covid-19/, the data is combination from Center for Disease Control, Prevention’s Behavioral Risk Factor Surveillance System and Kaiser Family Foundation including columns of name of the metropolitan area, the total percent at risk in the area, high risk individuals per icu bed, high risk individuals per hospital, number of ICU beds, number of hospitals in the area and the total number of high risk individuals in the area, where high risk is defined as age 65 and older, physical illness, bad health habits and currently pregnant. However since the data only have 136 rows * 7 column indicating that not all metropolitan area in US is included that may cause bias. The data might be helpful in terms of deciding whether or not area is likely to be exhausted with medical resources using the radio of high-risk population to total population combined with ICU beds and number of hospitals, should the authorities be paying attention to this area with proper solution? 
    """)
df=pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/covid-geography/mmsa-icu-beds.csv")


# In[3]:


df


# In[4]:


state=df['MMSA'].str.split(',', expand=True)
state.columns=['area','state','etc']
state=state.drop(columns=['etc'])


# In[5]:


df= pd.concat([state,df['total_percent_at_risk'],df['high_risk_per_ICU_bed'],df['high_risk_per_hospital'],df['icu_beds'],df['hospitals'],df['total_at_risk']], axis=1)


# In[6]:


state1=df['state'].str.split('-', expand=True)
state1.columns=['state','state1','state2','state3']
state1=state1.drop(columns=['state1','state2','state3'])


# In[7]:


df= pd.concat([df['area'],state1,df['total_percent_at_risk'],df['high_risk_per_ICU_bed'],df['high_risk_per_hospital'],df['icu_beds'],df['hospitals'],df['total_at_risk']], axis=1)


# In[10]:


state_codes = {
    'WA': '53', 'DE': '10', 'DC': '11', 'WI': '55', 'WV': '54', 'HI': '15',
    'FL': '12', 'WY': '56', 'PR': '72', 'NJ': '34', 'NM': '35', 'TX': '48',
    'LA': '22', 'NC': '37', 'ND': '38', 'NE': '31', 'TN': '47', 'NY': '36',
    'PA': '42', 'AK': '02', 'NV': '32', 'NH': '33', 'VA': '51', 'CO': '08',
    'CA': '06', 'AL': '01', 'AR': '05', 'VT': '50', 'IL': '17', 'GA': '13',
    'IN': '18', 'IA': '19', 'MA': '25', 'AZ': '04', 'ID': '16', 'CT': '09',
    'ME': '23', 'MD': '24', 'OK': '40', 'OH': '39', 'UT': '49', 'MO': '29',
    'MN': '27', 'MI': '26', 'RI': '44', 'KS': '20', 'MT': '30', 'MS': '28',
    'SC': '45', 'KY': '21', 'OR': '41', 'SD': '46'
}
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


# In[11]:


remove_extra_space=[]
for i in df['state'].tolist():
    j = i.replace(' ','')
    remove_extra_space.append(j)


# In[12]:


fips=[]
for i in range(len(df)):
    fips.append(state_codes[remove_extra_space[i]])


# In[13]:


full=[]
for i in range(len(df)):
    full.append(states[remove_extra_space[i]])


# In[14]:


df['FIPS']=fips
df['full']=full


# In[15]:


df_clean=df.groupby("full")["high_risk_per_ICU_bed"].mean().reset_index(name='mean')


# In[22]:


icu_bed=dict(zip(df_clean['full'].tolist(),df_clean['mean'].tolist()))
print(icu_bed)


# In[27]:



#fig, ax = plt.subplots(figsize=(10,5))

# Lambert Conformal map of lower 48 states.
#m = Basemap(llcrnrlon=-119,llcrnrlat=20,urcrnrlon=-64,urcrnrlat=49,
           # projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

# Mercator projection, for Alaska and Hawaii
#m_ = Basemap(llcrnrlon=-190,llcrnrlat=20,urcrnrlon=-143,urcrnrlat=46,
            #projection='merc',lat_ts=20)  

#shp_info = m.readshapefile('st99_d00','states',drawbounds=True,
                          # linewidth=0.45,color='gray')
#shp_info_ = m_.readshapefile('st99_d00','states',drawbounds=False)
icu_bed = {'Alabama': 1240.0384159999999,
 'Alaska': 2055.441034,
 'Arizona': 2043.376384,
 'Arkansas': 2090.809104,
 'California': 2191.2162275,
 'Colorado': 2501.0613455000002,
 'Connecticut': 2150.121289,
 'Delaware': 2441.704685,
 'District of Columbia': 2356.378968,
 'Florida': 1760.7124459499998,
 'Georgia': 1537.9472675,
 'Hawaii': 3860.5570000000002,
 'Idaho': 2013.7760269999999,
 'Illinois': 1548.761447,
 'Indiana': 1408.523852175,
 'Iowa': 2526.077444,
 'Kansas': 2399.082127,
 'Kentucky': 1198.2511956499998,
 'Louisiana': 2403.6591725,
 'Maine': 3051.2289530000003,
 'Maryland': 2527.5044172499997,
 'Massachusetts': 2388.92191675,
 'Michigan': 1921.6770276666666,
 'Minnesota': 1410.2821018749999,
 'Mississippi': 1082.387778,
 'Missouri': 1401.0758555,
 'Montana': 1942.9790239999998,
 'Nebraska': 1470.71477894,
 'Nevada': 638.8247432000001,
 'New Hampshire': 2690.925375,
 'New Jersey': 2173.873935,
 'New Mexico': 3091.331014,
 'New York': 2089.4070103999998,
 'North Carolina': 2919.072935,
 'North Dakota': 1276.094062675,
 'Ohio': 1570.6550736,
 'Oklahoma': 1457.7684895,
 'Oregon': 2648.9257039999998,
 'Pennsylvania': 1811.9190317500002,
 'Puerto Rico': 0,
 'Rhode Island': 2110.081467,
 'South Carolina': 2356.472305142857,
 'South Dakota': 1977.9239636666669,
 'Tennessee': 1522.9751190000002,
 'Texas': 2121.046255555555,
 'Utah': 1927.238537,
 'Vermont': 2104.114565,
 'Virginia': 1900.4609500000001,
 'Washington': 2371.5011539999996,
 'West Virginia': 1158.1655238,
 'Wisconsin': 1411.0374160000001,
 'Wyoming':0}

#colors={}
#statenames=[]
#cmap = plt.cm.YlOrRd # use 'reversed hot' colormap
#vmin = 0; vmax = 5000 # set range.
#norm = Normalize(vmin=vmin, vmax=vmax)
#for shapedict in m.states_info:
 #   statename = shapedict['NAME']
    # skip DC and Puerto Rico.
  #  if statename not in ['District of Columbia','Puerto Rico']:
   #     pop = icu_bed[statename]
        # calling colormap with value between 0 and 1 returns
        # rgba value.  Invert color range (hot colors are high
        # population), take sqrt root to spread out colors more.
    #    colors[statename] = cmap(np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
    #statenames.append(statename)

#%% ---------  cycle through state names, color each one.  --------------------
#for nshape,seg in enumerate(m.states):
    # skip DC and Puerto Rico.
 #   if statenames[nshape] not in ['Puerto Rico', 'District of Columbia']:
  #      color = rgb2hex(colors[statenames[nshape]])
   #     poly = Polygon(seg,facecolor=color,edgecolor=color)
    #    ax.add_patch(poly)

#AREA_1 = 0.005  # exclude small Hawaiian islands that are smaller than AREA_1
#AREA_2 = AREA_1 * 30.0  # exclude Alaskan islands that are smaller than AREA_2
#AK_SCALE = 0.19  # scale down Alaska to show as a map inset
#HI_OFFSET_X = -1900000  # X coordinate offset amount to move Hawaii "beneath" Texas
#HI_OFFSET_Y = 250000    # similar to above: Y offset for Hawaii
#AK_OFFSET_X = -250000   # X offset for Alaska (These four values are obtained
#AK_OFFSET_Y = -750000   # via manual trial and error, thus changing them is not recommended.)

#for nshape, shapedict in enumerate(m_.states_info):  # plot Alaska and Hawaii as map insets
#    if shapedict['NAME'] in ['Alaska', 'Hawaii']:
#        seg = m_.states[int(shapedict['SHAPENUM'] - 1)]
#        if shapedict['NAME'] == 'Hawaii' and float(shapedict['AREA']) > AREA_1:
#            seg = [(x + HI_OFFSET_X, y + HI_OFFSET_Y) for x, y in seg]
#            color = rgb2hex(colors[statenames[nshape]])
#        elif shapedict['NAME'] == 'Alaska' and float(shapedict['AREA']) > AREA_2:
#            seg = [(x*AK_SCALE + AK_OFFSET_X, y*AK_SCALE + AK_OFFSET_Y)                   for x, y in seg]
#            color = rgb2hex(colors[statenames[nshape]])
#        poly = Polygon(seg, facecolor=color, edgecolor='gray', linewidth=.45)
#        ax.add_patch(poly)

#ax.set_title('The mean number of high risk individuals per ICU bed by state')


#x1,y1 = m_([-190,-183,-180,-180,-175,-171,-171],[29,29,26,26,26,22,20])
#x2,y2 = m_([-180,-180,-177],[26,23,20])  # these numbers are fine-tuned manually
#m_.plot(x1,y1,linewidth=0.8)  # do not change them drastically
#m_.plot(x2,y2,linewidth=0.8)

#%% ---------   Show color bar  ---------------------------------------
#ax_c = fig.add_axes([0.9, 0.1, 0.03, 0.8])
#cb = ColorbarBase(ax_c,cmap=cmap,norm=norm,orientation='vertical',
                 # label=r'[high risk per ICU bed]')
#plt.show()


# In[28]:


df
st.write("""
    3.  
a.  To find top states/areas that need attention for medical resources
""")
st.write("""
i.  Analyst might want to analysis data for the “reader” such as the authorities trying to support those area with difficulties in terms of medical resources based on the percentage of high-risk population and the number of high-risk individuals per ICU beds and hospitals in the area using a heat geomap and color based on those factors, can be organized by state level or micropolitan area level zoom in the heat geomap, data used is the name and the state of the area, the percent of individuals in that area that are at high risk, the number of high risk individuals per ICU bed and hospital where the target data is looking for extreme/top areas that are mostly likely to have difficulties, name and the state of the area -> the number of high risk individuals per ICU bed-> the percent of individuals in that area that are at high risk ->the number of high risk individuals per hospital.

    """)
st.write("""
    b.  Find correlation between number of ICU beds and hospitals and high-risk population
""")
st.write("""
i.  Audience trying to figure out is there a correlation between number of ICU beds and hospitals and high-risk population, where the visualization can be scatter plots of number of ICU beds vs number of high-risk and plot of number of hospitals vs number of high-risk to discover the relationships using data of the number of ICU beds in the area, the number of hospitals in the area, state of the area and the total number of high risk individuals in the area, can color individual data points by state level,  where number of high risk->number of ICU beds->number of hospitals in the area->state of the area.

    """)
st.write("""
    4.
 a. """)
st.image(
            "https://raw.githubusercontent.com/qisu4484/info/main/Picture1.jpg",
            width=700, 
        )
st.write("""
 the color of individual state can be classified based on the mean value of number of high-risk individuals per ICU beds in that area or the number of high-risk individuals per hospitals, and there can be circle in middle of each state and the size of the circle can be adjusted by other attributes such as the average percent of individuals in the state that are at high risk. Therefore, by visualizing the heat map among with the variable size circle can identify what are some of the states or area that might need medical resources, ideally, the heat map would not only be limited state wise but can be break down to metropolitan area, the tradeoff might be that it is not as easily as state wise to identify key areas, if we break down to metropolitan area, there are way too many small pieces, and the visualization might be hard to gather information, but if we are going to do it state wise by the average of number of high-risk individuals per ICU beds, some extreme area such as Hilton head island metropolitan may not seem obvious.


""")
st.write("""
    b.
    """)
st.image(
            "https://raw.githubusercontent.com/qisu4484/info/main/Picture2.jpg",
            width=700, 
        )
st.write("""
    The correlation heat map can analysis correlation of two features through the color heat base map of each correlation, therefore can analyze if there exist a correlation between the number of high risk and number of ICU bed or hospitals, if there exist such correlation, all we are going to see in the visualization is the correlation number, there is not enough intuitive about how there is a correlation between the two, we might also want to see how two features are correlated for each state, that is, is this correlation exists in every state. Or we can plot the number of high risk vs number of ICU beds or hospitals where each data point is the number of high risk and number of ICU beds for each metropolitan area in this case, 136 data points, where this plot can also break down to state level, that is, data points for metropolitan areas belongs to the same state. 
    """)
st.write("""
    5. 
    a. ![alt text](https://raw.githubusercontent.com/qisu4484/info/main/Picture3.png "1")
    Since MMSA includes the name of the metropolitan area and its state, by splitting the MMSA into two columns of metropolitan area and state, we then can group it by state, first plot the US map then using the mean of number of high risk individuals per ICU beds to determine the color of each state where the colorbar base would be based on the max and min range of the high risk individuals per ICU beds, therefore to achieve the task of find top states that need attention for medical resources using the color assigned to max value. 
    """)
st.write("""
    b. 
    """)
st.image(
            "https://raw.githubusercontent.com/qisu4484/info/main/Picture4.png",
            width=700, 
        )
st.write("""
    ![alt text](https://raw.githubusercontent.com/qisu4484/info/main/Picture5.png "1")
    ![alt text](https://raw.githubusercontent.com/qisu4484/info/main/Picture6.png "1")
    ![alt text](https://raw.githubusercontent.com/qisu4484/info/main/Picture7.png "1")
    Using matplot to plot total at risk VS ICU beds where each data point is total at risk and ICU beds for each metropolitan area, then we can uses altair to create an interactive visualization of the sum of total at risk per state and sum of icu beds in each state to visualize what which states having the highest total at risk and highest ICU beds, by using altair chart, we have the overall plot of total at risk vs ICU beds but we can also visualize the total at risk and icu beds for individual states therefore, we can both analyze whether or not there seems like there is a correlation overall, and there is correlation between total at risk and icu beds state wise, the size of the data point on the left side is determined by sum of total number of high risk individuals in the state, hence to visualize which states have the highest number of high risk individuals. 
    """)
st.write("""
    6.
    a. ![alt text](https://raw.githubusercontent.com/qisu4484/info/main/Picture8.png "1")
    Wyoming is one of the states that don’t have any data where as I mentioned earlier in section 2, that not all metropolitan area in US is included in the dataset, from the heat map above, New Mexico, Hawaii, Oregon , North Carolina, Maine might be top 5 states that need medical attention, however, in the article, the metropolitan area that was suffering from medical shortage which is in South Carolina isn’t so obvious in the visualizations, this is caused by incomplete data, once we group the metropolitan area into state level, those metropolitan area that are seeking for help isn’t going to be obvious. 
    """)

# In[39]:

st.write("""
    b.
    """)
plt.scatter(df['total_at_risk'],df['icu_beds'])
plt.xlabel("total at risk")
plt.ylabel("ICU beds")


# In[37]:


selection = alt.selection(type="multi", fields=['full'])

alt.Chart(df).properties(width=250, height=250).mark_circle().encode(
    x='sum(total_at_risk)',
    y='sum(icu_beds)',
    size='sum(icu_beds)',
    tooltip=['full', 'sum(total_at_risk)'],
    color=alt.condition(selection, 'full', alt.value('lightgray'))
).add_selection(selection)| alt.Chart(df).properties(width=250, height=250).mark_circle().encode(
    x=alt.X('total_at_risk'),
    y=alt.X('icu_beds'),
).transform_filter(selection)

st.write("""
    There do seems like there is correlation between total at risk and number of ICU beds, even if we click on state such as Texas which contains data point for metropolitan area belongs to Texas or metropolitan area belongs to Florida and etc. we still observe that there exits correlation between number of high risk population and number of ICU beds, from there, we also observe that Florida, California, New York, Texas have highest total number high risk individuals which also have the highest total number of ICU beds.
    """)
st.write("""
    7.
    """)
st.write("""
    a.    I think instead of plotting state level heat map, one of the solutions is to plot bar plot for the top five metropolitan area from the data set directly, or to find other dataset that contains all the metropolitan area in US and its number of high-risk per ICU bed and etc. then construct state level graph or to find the FIPS/longitude and latitude for each of the metropolitan area (which is hard to find for each row may requires write a script) and plot for each metropolitan area depending on its longitude and latitude/FIPS. 
    """)
st.write("""
    b.    We can also uses the feature of hospitals and doing comparison between number of high risk population and the number of hospitals, my hypothesis is that since there exist relationship between number of ICU beds and number of high risk, there will also exist some relationship of number of high risk and number of hospitals, maybe the one of the improvement can be that building another plot among with the interactive visualization about the number of hospitals, we can also add a regression line to the graph for better analysis such as hypothesis test.
    """)
st.write("""
    8.  Since most of the high-risk groups are elderly such as 65 or older, and one of the characteristics of the distribution of the elderly may be the cities/states with relatively good economic development in the 1980s and 1990s, and the cities with higher livability, as my visualization shows that New York, Texas, California and Florida where are popular vacation destinations have the highest total number of high-risk individuals and New Mexico and Hawaii that are also popular destinations for vacation requires attention for medical resources. Better economic development means higher taxation, and taxation will bring people’s welfare. Including medical development, so there may be more ICU bed. 
    """)
st.write("""
    9.  In order to design visualizations for audience, we need to identify who our audience are, and decided the precision(such as group metropolitan area into state level or just in the metropolitan area level), and selecting chart types that fits our data and most intuitive for the audience, while not all functionalities in the design stage is achievable, we need to choose the most important idea that we want to present our visualizations to the audience, for the heat map, it is also important to choose the color map, we should choose one that is clear to see and eye-catching for states that most needed medical help. 
    """)

# In[35]:


dft=df.groupby("full").sum()


# In[36]:


dft


# In[ ]:




