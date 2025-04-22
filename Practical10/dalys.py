import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/home/apple/桌面/Learn/IBI1_2024-25/Practical10")
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")
print ("3rd column:",dalys_data.iloc[0:10,2])
#The 10th year is 1999

Year=dalys_data.loc[:,"Year"]
Year_1990=[]
for i in range(len(Year)):
    Year_1990.append(Year[i]==1990)
print ("All countries in 1990:",dalys_data.loc[Year_1990,"DALYs"])

uk=dalys_data.loc[dalys_data.Entity=="United Kingdom",["DALYs","Year"]]
uk_mean=np.mean(uk.DALYs)
fr=dalys_data.loc[dalys_data.Entity=="France",["DALYs","Year"]]
fr_mean=np.mean(fr.DALYs)
print (f'DALYs mean: UK mean={uk_mean}, France mean={fr_mean}')
#Mean DALYs in the UK was geater than France

plt.plot(uk.Year,uk.DALYs,'b+')
plt.title('The DALYs over time in the UK')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.xticks(uk.Year,rotation=-90)
plt.show()
