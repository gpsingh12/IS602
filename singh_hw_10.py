import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
import scipy.ndimage as ndimage
import scipy.misc as misc
import scipy 
from scipy import ndimage

#1. Carsdata Graphs
cars_df= pd.read_csv('cars.data.csv', header=None)
cars_df.columns=['buying', 'maint', 'doors', 'persons', 'lug_boot','safety', 'rating']

freq_buy = cars_df.groupby(['buying']).size()
freq_maint =cars_df.groupby(['maint']).size()
freq_sfty = cars_df.groupby(['safety']).size()
freq_doors = cars_df.groupby(['doors']).size()

plt.figure()
plt.subplot(221)
freq_buy.plot(kind='bar', color='red')
plt.xlabel('Buying')
plt.ylabel('Frequency')
plt.xticks(rotation='horizontal')

plt.subplot(222)
freq_maint.plot(kind='bar', color='skyblue')
plt.xlabel('Maintenance')
plt.xticks(rotation='horizontal')

plt.subplot(223)
freq_sfty.plot(kind='bar', color='grey')
plt.xlabel('Safety')
plt.ylabel('Frequency')
plt.xticks(rotation='horizontal')

plt.subplot(224)
freq_doors.plot(kind='bar', color='orange')
plt.xlabel('No. of Doors')
plt.xticks(rotation='horizontal')
plt.show()



# 2. Brain and Body Weight (Linear Regression)
df = pd.read_csv('brainandbody.csv')
body = df.body.astype(float)
brain=df.brain.astype(float)

#from assignment 5 the values calculated
a= 0.902912947729
b= -56.8555454286
body_lr =  0.902912947729 * brain + (-56.8555454286)

plt.scatter(brain,body)
plt.plot(brain, a*(brain) + b,color='red')
plt.xlabel('Brain Wt.')
plt.ylabel('Body Wt.')
plt.title('ScatterPlot of Body vs Brain Wt & Regression Line')
plt.ylim(ymax=4000)
plt.xlim(xmax=3000)
plt.ylim(ymin=-100)
plt.xlim(xmin=-100)
plt.show()


#3. Center points for Objects  



objects = misc.imread('objects.png')
obj_fil = ndimage.gaussian_filter(objects, 3)
obj_fil = obj_fil[:,:,0]
thres = obj_fil > obj_fil.mean()
labeled, n_objects = ndimage.label(thres)
c_mass= scipy.ndimage.measurements.center_of_mass(thres, labeled, range(1,n_objects+1))

plt.scatter([pt[1] for pt in c_mass], [pt[0] for pt in c_mass],color='red')
plt.imshow(objects)
plt.show()

    




#4. Variation of Requests vs Time(in hours)
#modified file from hw 9
df = pd.read_csv('epa-http_new.txt', sep = '\s+',header=None)
df.columns = ['Host', 'Timestamp','Request','Reply', 'Bytes']
df= df.replace("-", "0")

df.Bytes=df.Bytes.astype(int)
#df=df[['Timestamp', 'Bytes']]

df['Timestamp'] = pd.to_datetime(df['Timestamp'],format='[%d:%H:%M:%S]')
df['Time_hour'] = df['Timestamp'].dt.hour


hr = df.groupby(['Time_hour']).size()

plt.plot(hr,'o-',color='red')
plt.xlabel('Hours')
plt.ylabel('Number of Requests')
plt.show()


#References:
#https://plot.ly/matplotlib/subplots/
