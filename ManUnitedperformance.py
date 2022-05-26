import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('C:\\Users\\PC\\Downloads\\united10years.csv')
dataManager = data[data.Club=='United']
perform = ['Season','SeasonIndex']
dataperform = dataManager[perform]
plt.rcParams['figure.figsize'] = [15, 10]
plt.ylim(2.7,5)
plt.plot(dataperform.Season, dataperform.SeasonIndex, label = 'Performance', marker='o')
plt.grid(which='major', axis='both', linestyle='-.', linewidth=0.75)
plt.xticks(rotation=60, fontsize=12)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.title('Man United Season Performance Last 10 Years', fontsize = 20)
plt.annotate('Sir Alex Last Season', xy=('2012-2013',3.51), xytext=('2012-2013', 3.7), arrowprops=dict(facecolor='red', shrink=0.05),fontsize =15)
plt.annotate('David Moyes in', xy=('2013-2014',3.25), xytext=('2013-2014', 3.5), arrowprops=dict(facecolor='red', shrink=0.05),fontsize =15)
plt.annotate('Van Gaal in', xy=('2014-2015',3.27), xytext=('2015-2016', 3.3), arrowprops=dict(facecolor='red', shrink=0.05),fontsize =15)
plt.annotate('Jose Mourinho in', xy=('2016-2017',4.4), xytext=('2014-2015', 4.45), arrowprops=dict(facecolor='red', shrink=0.05), fontsize =15)
plt.annotate('Mourinho Fired at Mid Season\n*Solskjaer as Caretaker', xy=('2018-2019',3.21), xytext=('2016-2017', 3.0),arrowprops=dict(facecolor='red', shrink=0.05), fontsize =15)
plt.annotate('Solskjaer as \npermanent manager', xy=('2019-2020',4.29), xytext=('2017-2018', 4.5), arrowprops=dict(facecolor='red', shrink=0.05),fontsize =15)
plt.annotate('Solskjaer Fired at Mid Season\n*Rangnick as Caretaker', xy=('2021-2022',2.9), xytext=('2019-2020', 2.72), arrowprops=dict(facecolor='red', shrink=0.05),fontsize =15)
plt.ylabel("Performance Index", fontsize = 14)
plt.xlabel("Season", fontsize = 14)
plt.tight_layout()

x = dataperform.Season
y = round(dataperform.SeasonIndex,2)
for i, j in zip(x, y):
    if j == 4.42 or j == 4.41 or j == 3.64:
       plt.text(i, j+0.05, '{}'.format(j), fontsize = 13)
    elif j == 3.23 or 3.26 or 3.5:
        plt.text(i, j-0.08, '{}'.format(j), fontsize = 13)

plt.show()