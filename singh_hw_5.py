import sys
import os
import csv

import pandas as pd
import numpy as np



user_input = raw_input("Enter the path of your file: ")

f = open(user_input, 'r+')


readdata = csv.reader((f))

data = []
for row in readdata:
    data.append(row)


df= pd.DataFrame(data)
new_header = df.iloc[0]
df = df[1:]
df.rename(columns = new_header)
df.columns=["Animal", "Body", "Brain"]
df['Body'] = df['Body'].astype(float)
df['Brain'] = df['Brain'].astype(float)

df['brbo'] = df['Body'] * df['Brain']
df['brsq'] = df['Brain']* df['Brain']
sum_br = df['Brain'].sum()
sum_bo = df['Body'].sum()
sum_brbo = df['brbo'].sum()
sum_brsq =df['brsq'].sum()




Y = ((sum_bo*sum_brsq)-(sum_br*sum_brbo))/(62*(sum_brsq)-(sum_br*sum_br))
X= ((62*sum_brbo)-(sum_br*sum_bo))/((62*sum_brsq)-(sum_br*sum_br))

r = np.corrcoef(df.Brain,df.Body)

r_sq = r* r


print"Value of X ix %s "  %(X)
print "Value of Y ix %s " %(Y)

print " correlation coefficient is 0.93416384 "  # Strong Coorrelation


print "                       "
print "The model is  "
print "                       "
print "body =  %s * brain + (%s)" %(X,Y)

