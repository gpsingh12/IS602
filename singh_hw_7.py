import numpy as np
import pandas as pd
from scipy.optimize import curve_fit





colnames =['Animal', 'Body', 'Brain']
df=pd.read_csv('brainandbody.csv', sep=',',names=colnames)
df = df[1:]



df['Body'] = df['Body'].astype(float)
df['Brain'] = df['Brain'].astype(float)




xdata=df.Brain
ydata=df.Body

df1=df.drop('Animal', 1)



df['brbo'] = df['Body'] * df['Brain']
df['brsq'] = df['Brain']* df['Brain']
sum_br = df['Brain'].sum()
sum_bo = df['Body'].sum()
sum_brbo = df['brbo'].sum()
sum_brsq =df['brsq'].sum()


def linreg(input):

  Y = ((sum_bo*sum_brsq)-(sum_br*sum_brbo))/(62*(sum_brsq)-(sum_br*sum_br))
  X= ((62*sum_brbo)-(sum_br*sum_bo))/((62*sum_brsq)-(sum_br*sum_br))

  r = np.corrcoef(df.Brain,df.Body)

  r_sq = r* r

  print "                       "
  print "The model using least squares is  "
  print "                       "
  model = "body =  %s * brain + (%s)" %(X,Y)

  return model


def curvfit(input):
  
  def func(x, a, b):
    return a*x + b
  popt, pcov = curve_fit(func, xdata, ydata)
  print "                       "
  print "---------------------------"
  print "The model using curve fit is  "
  print "                       "
  model = "body =  %s * brain + (%s)" %(popt[0],popt[1])
  return model


def Gaussfit(input):
  def func1(x,a,b,c):
    return a*np.exp(-(x-b)**2/(2*c**2))
  popt, pcov = curve_fit(func1, xdata, ydata)
  
  print "                       "
  print "---------------------------"
 
  print "                       "
  model= "(%s)*exp(-(x-(%s))**2/(2*(%s)**2))" %(popt[0],popt[1],popt[2])
  values = "a =  %s , b = %s , c = %s " %(popt[0],popt[1],popt[2])
  
  print " the values for a, b and c are :"
  
  print "                       "
  print values
  print "                       "
  print "The model using gaussian is  "
  print "                       "
  return model

  

if __name__ == "__main__":	
  input = df
  print linreg(input)
  print curvfit(input)
  print Gaussfit(input)
 
  
import timeit
setup = '''

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit





colnames =['Animal', 'Body', 'Brain']
df=pd.read_csv('brainandbody.csv', sep=',',names=colnames)
df = df[1:]



df['Body'] = df['Body'].astype(float)
df['Brain'] = df['Brain'].astype(float)

df1=df.drop('Animal', 1)


xdata=df.Brain
ydata=df.Body




df['brbo'] = df['Body'] * df['Brain']
df['brsq'] = df['Brain']* df['Brain']
sum_br = df['Brain'].sum()
sum_bo = df['Body'].sum()
sum_brbo = df['brbo'].sum()
sum_brsq =df['brsq'].sum()


def linreg(input):

  Y = ((sum_bo*sum_brsq)-(sum_br*sum_brbo))/(62*(sum_brsq)-(sum_br*sum_br))
  X= ((62*sum_brbo)-(sum_br*sum_bo))/((62*sum_brsq)-(sum_br*sum_br))

  r = np.corrcoef(df.Brain,df.Body)

  r_sq = r* r
  model = "body =  %s * brain + (%s)" %(X,Y)

  return model


def curvfit(input):
  
  def func(x, a, b):
    return a*x + b
  popt, pcov = curve_fit(func, xdata, ydata)
  model = "body =  %s * brain + (%s)" %(popt[0],popt[1])
  return model

def Gaussfit(input):
  def func1(x,a,b,c):
    return a*np.exp(-(x-b)**2/(2*c**2))
  popt, pcov = curve_fit(func1, xdata, ydata)
  
  
  print "a*exp(-(x-b)**2/(2*c**2))"
  model = "a =  %s , b = %s , c = %s " %(popt[0],popt[1],popt[2])
  return model

'''
print "                       "
print "---------------------------"
print "for n = 100"
print "Runtime for three methods using timeit:"
print "                                     "
n=100
t = timeit.Timer('linreg(input)', setup=setup)
t1 =t.timeit(n)
print " Runtime for least squares is %s secs" %t1 

print "                                     "
n=100
t = timeit.Timer('curvfit(input)', setup=setup)
t2=t.timeit(n)
print" Runtime for curve fit is %s secs " %t2


print "                                     "
n=100
t = timeit.Timer('linreg(input)', setup=setup)
t3 =t.timeit(n)
print " Runtime for gaussian fit is %s secs" %t3 
