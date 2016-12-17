
import pandas as pd
import numpy as np
import re
import csv


with open('epa-http.txt', 'r') as f_in, open('epa-http_new.txt', 'w') as f_out:
    reader=f_in.readlines()
    pattern=r'="\s[A-Z]'
    for line in reader:
        line = re.sub(pattern, '=\s[A-Z]', line)
        f_out.write(line)

f_in.close()
f_out.close()



df = pd.read_csv('epa-http_new.txt', sep = '\s+',header=None)
df.columns = ['Host', 'Timestamp','Request','Reply', 'Bytes']
df= df.replace("-", "0")

#1 Which hostname or IP address made the most requests?


max_req = df['Host'].value_counts()
M_rq= max_req.head(1).index[0]


print '1. Hostname or IP address made the most requests is : %s' %M_rq



#2 Which hostname or IP address received the most total bytes from the server?
#How many bytes did it receive?

df['Bytes'] = df['Bytes'].astype(int)
m_bytes=df[['Host', 'Bytes']]
m_bytes = m_bytes.groupby(['Host']).sum()
m_bytes=m_bytes.sort('Bytes')
m_bytes_host= m_bytes.tail(1).index[0]
m_bytes_count =m_bytes.tail(1).values[0]
print "                                                               "
print "---------------------------------------------------------------"

print '2. IP address with most total bytes is : %s' %m_bytes_host
print '                                                       '
print ' Bytes recieved by the host is : %s' %m_bytes_count 

#3 During what hour was the server the busiest in terms of requests?

df['Timestamp'] = pd.to_datetime(df['Timestamp'],format='[%d:%H:%M:%S]')
df['Time_hour'] = df['Timestamp'].dt.hour

b_hour = df['Time_hour'].value_counts()
b_hour =  b_hour.head(1).index[0]
print "                                                               "
print "---------------------------------------------------------------"

print "Busiest hour in terms of requests is : %s" %b_hour  

#4. Which .gif image was downloaded the most during the day?

gif = df[df['Request'].str.contains("gif")]
gif = gif[['Request', 'Reply']]
gif = gif.groupby(['Request']).size()

gif.sort()
print "                                                          "
print "----------------------------------------------------------"
print '4. Most downloded .gif image was : %s' %gif.tail(1).index[0]

#5. What HTTP reply codes were sent other than 200?

codes = df['Reply'].unique().tolist()

codes=codes[1:]
print "                                                           "
print "-----------------------------------------------------------"
print "5. HTTP reply codes other than 200 were %s" %(codes)
df.head()
