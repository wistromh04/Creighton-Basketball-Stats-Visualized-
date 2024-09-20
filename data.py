import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name': ['Baylor Scheierman F', 'Trey Alexander G', 'Ryan Kalkbrenner C', 'Steven Ashworth G',
             'Mason Miller F', 'Francisco Farabello G', 'Isaac Traudt F', 'Fredrick King C', 
             'Jasen Green F', 'Josiah Dotzler G', 'Johnathan Lawson G'],
    'MIN': [1288, 1302, 1211, 1111, 718, 766, 275, 191, 178, 77, 58],
    'FGM': [219, 232, 241, 121, 61, 49, 30, 32, 17, 10, 4],
    'FGA': [489, 520, 373, 307, 125, 99, 69, 56, 26, 23, 14],
    'FTM': [99, 89, 106, 68, 13, 7, 5, 13, 3, 3, 2],
    'FTA': [113, 108, 149, 75, 18, 10, 6, 25, 6, 5, 3],
    '3PM': [110, 62, 16, 80, 49, 29, 24, 0, 2, 2, 1],
    '3PA': [289, 183, 54, 229, 108, 69, 57, 2, 7, 11, 9],
    'PTS': [647, 615, 604, 390, 184, 134, 89, 77, 39, 25, 11],
    'OR': [26, 18, 88, 12, 29, 9, 15, 25, 23, 1, 4],
    'DR': [289, 183, 178, 104, 79, 64, 23, 40, 20, 6, 8],
    'REB': [315, 201, 266, 116, 108, 73, 38, 65, 43, 7, 12],
    'AST': [138, 165, 44, 148, 13, 51, 11, 3, 7, 3, 5],
    'TO': [78, 86, 52, 54, 13, 31, 4, 9, 8, 7, 3],
    'STL': [32, 38, 13, 17, 7, 19, 2, 2, 1, 3, 0],
    'BLK': [5, 15, 107, 0, 2, 3, 1, 8, 1, 0, 1],
    'FOULS': [58, 61, 66, 68, 34, 50, 16, 29, 7, 9, 5 ,]
}


df = pd.DataFrame(data)

df['FG%'] = (df['FGM'] / df['FGA']) * 100
df['FT%'] = (df['FTM'] / df['FTA']) * 100
df['per32'] = (df['PTS'] / df['MIN']) * 32


plt.figure(figsize=(10, 6))
sns.barplot(x='PTS', y='Name', data=df, palette="Blues_d")
plt.title('Points Scored by Each Player')
plt.xlabel('Points')
plt.ylabel('Player')
plt.show()


plt.figure(figsize=(10, 6))
sns.barplot(x='FG%', y='Name', data=df, palette="Greens_d")
plt.title('Field Goal Percentage by Player')
plt.xlabel('Field Goal Percentage (%)')
plt.ylabel('Player')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='MIN', y='PTS', data=df, hue='Name', palette="deep")
plt.title('Minutes Played vs Points Scored')
plt.xlabel('Minutes Played')
plt.ylabel('Points Scored')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='per32', y='Name', data = df, palette="Blues_d")
plt.title('Points per 32 Min by each Player')
plt.xlabel('Points per 32 Min')
plt.ylabel('Player')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='MIN', y='TO', data=df, hue='Name', palette="deep")
plt.title('Minutes Played vs Turnovers Commited')
plt.xlabel('Minutes Played')
plt.ylabel('Turnovers Comitted')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='MIN', y='FOULS', data=df, hue='Name', palette="deep")
plt.title('Minutes Played vs Personal Fouls Commited')
plt.xlabel('Minutes Played')
plt.ylabel('Fouls Comitted')
plt.show()


