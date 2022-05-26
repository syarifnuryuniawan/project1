import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('C:\\Users\\PC\\Downloads\\united10years.csv')

dataManager1 = data[data.Club=='United']
perform1 = ['Season','Expenditure']
dataperform1 = dataManager1[perform1]

plt.rcParams['figure.figsize'] = [12, 8]
plt.plot(dataperform1.Season, dataperform1.Expenditure, label = 'Transfer Expenditure', marker='o')
plt.grid(which='major', axis='both', linestyle='-.', linewidth=0.75)
plt.xticks(rotation=60, fontsize=14)
plt.yticks(fontsize=14)
plt.legend(fontsize=14)
plt.ylim(50, 250)
plt.title('Man United Transfer Expenditure each Season', fontsize = 20)
plt.text('2012-2013',240,'*In Million Euro', horizontalalignment='left', verticalalignment='top', fontsize =16, bbox=dict(facecolor='blue', alpha=0.5)) 
x = dataperform1.Season
y = dataperform1.Expenditure
for i, j in zip(x, y):
   if j == 195.35 or j == 198.4 or j == 234.8:
      plt.text(i, j+3, '{}'.format(j), fontsize = 15)
   else :
      plt.text(i, j-5, '{}'.format(j), fontsize = 15)
plt.ylabel("Expenditure", fontsize = 14)
plt.xlabel("Season", fontsize = 14)
plt.tight_layout()
plt.show()