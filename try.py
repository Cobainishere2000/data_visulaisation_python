import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
fandango = pd.read_csv("fandango_scrape.csv")
fandango.head()
plt.figure(figsize=(10,4),dpi=150)
sns.scatterplot(data=fandango,x='RATING',y='VOTES')
fandango['YEAR'] = fandango['FILM'].apply(lambda title:title.split('(')[-1])
fandango['YEAR']=fandango['YEAR'].apply(lambda title:title.replace(')',' '))
#creating a new column in the dataframe year is included in the
#name of the film as FILM (year) , so we split by '(' and then take the last element
#and replace the closing bracket with space
print("THE DATAFRAME :   ")
display(fandango)
plt.title("RATING VS VOTES")
plt.xlabel("RATING")
plt.ylabel("VOTES")
plt.show()
frequencies=fandango['YEAR'].value_counts();
print("Number of Movies Released in a given year ")
display(frequencies)
sns.countplot(data=fandango,x='YEAR')
plt.title("MOVIES EACH YEAR")
plt.xlabel("YEAR")
plt.ylabel("NO. Of Movies")
plt.show();
list=fandango.nlargest(10,"VOTES")
print("TOP 10 Movies with most votes as per FANDANGO:")
display(list)
zero=fandango['VOTES']==0
s=zero.sum()
print("Movies with no votes :",s)
#new dataframe after removing movies with no VOTES
fan_reviewed=fandango[fandango['VOTES']>0]
display(fan_reviewed)
#display kde plot with to show stars displayed vs actual ratings
plt.figure(figsize=(8,5),dpi=150)
sns.kdeplot(data=fan_reviewed,x='RATING',clip=[0,5],fill=True,label='True Rating')
sns.kdeplot(data=fan_reviewed,x='STARS',clip=[0,5],fill=True,label='Stars Displayed')
plt.legend(loc=(0.0,1.01))
plt.show()
#create a new plot  to find difference in ratings and STARS
fan_reviewed["Difference(Stars & Ratings)"]=fan_reviewed["STARS"]-fan_reviewed["RATING"];
fan_reviewed["Difference(Stars & Ratings)"]=fan_reviewed["Difference(Stars & Ratings)"].round(2)
display(fan_reviewed)
#show it graphically
plt.figure(figsize=(8,5),dpi=150)
sns.countplot(data=fan_reviewed,x="Difference(Stars & Ratings)")
plt.show()
