import pandas as pd

df = pd.read_csv("summer.csv")

# # 1. In how many cities Summer Olympics is held so far?
# print(df['City'].unique())
# total_city = len(df['City'].unique())
# print("Olympics is held in {} city".format(total_city))
#
# # 2. Which sport is having most number of Gold Medals so far? (Top 5)
# sportInOlympics = df[(df.Medal == 'Gold')]
# sportInOlympics.head()
#
# data = []
# for sport in sportInOlympics['Sport'].unique():
#     data.append([sport, len(sportInOlympics[sportInOlympics['Sport'] == sport])])
# data = pd.DataFrame(data, columns=['Sport', 'No. of gold medals'])
# data = data.sort_values(by='No. of gold medals', ascending=False).head()
# print(data)
#
# data.plot(x='Sport', y='No. of gold medals', kind='bar')

# 3. Which sport is having most number of medals so far? (Top 5)
data = []
for sport in df['Athlete'].unique():
    data.append([sport, len(df[df['Athlete'] == sport])])
data = pd.DataFrame(data, columns=['Athlete', 'No. of medals'])
data = data.sort_values(by='No. of medals', ascending=False).head()

print(data)
# data1.plot(x='Sport', y='No. of medals', kind='bar')

# # 4. Which player has won most number of medals? (Top 5)
# data4 = []
# for sport in df['Athlete'].unique():
#     data4.append([sport, len(df[df['Athlete'] == sport])])
# data4 = pd.DataFrame(data4, columns=['Athlete', 'No. of medals'])
# data4 = data4.sort_values(by='No. of medals', ascending=False).head()
#
# print(data)
# data.plot(x='Athlete', y='No. of medals', kind='bar')
#
# # 5. Which player has won most number Gold Medals of medals? (Top 5)
# playerInOlympics = df[(df.Medal == 'Gold')]
# playerInOlympics.head()
#
# data5 = []
# for sport in playerInOlympics['Athlete'].unique():
#     data5.append([sport, len(playerInOlympics[playerInOlympics['Athlete'] == sport])])
# data5 = pd.DataFrame(data5, columns=['Athlete', 'No. of gold medals'])
# data5 = data5.sort_values(by='No. of gold medals', ascending=False).head()
#
# data.plot(x='Athlete', y='No. of gold medals', kind='bar')
#
# # 6. In which year India won first Gold Medal in Summer Olympics?
# IndiaInOlympics = df[(df.Country == "IND") & (df.Medal == 'Gold')]
# IndiaInOlympics.head(1)
#
# # 7. Which event is most popular in terms on number of players? (Top 5)
# data7=[]
# for sport in df['Event'].unique():
#     data7.append([sport,len(df[df['Event']==sport])])
# data7=pd.DataFrame(data7, columns=['Event','No. of players'])
# data7=data7.sort_values(by='No. of players', ascending=False).head()
# print(data7)
#
# data.plot(x='Event',y='No. of players',kind='bar')
#
#
# # 8. Which sport is having most female Gold Medalists? (Top 5)
# womenInOlympics = df[(df.Gender == 'Women') & (df.Medal == 'Gold')]
# data8=[]
# for sport in womenInOlympics['Sport'].unique():
#     data8.append([sport,len(womenInOlympics[womenInOlympics['Sport']==sport])])
# data8=pd.DataFrame(data8, columns=['Sport','No. of female gold medalists'])
# data8=data8.sort_values(by='No. of female gold medalists', ascending=False).head()
# print(data8)
#
# data.plot(x='Sport',y='No. of female gold medalists',kind='bar')
#
#
