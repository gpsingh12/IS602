import Tkinter
import tkFileDialog
import re
import csv
import operator




root = Tkinter.Tk()
root.withdraw()

filename = tkFileDialog.askopenfilename(parent=root)
fo = open(filename)



print "output for 2a"

data = csv.reader(fo,delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(5))
try:
    for row in sortedlist:
        if row[0] == 'vlow' or row[1]=='vlow' or row[2]=='1' \
           or row[3]=='1' or row[4]=='vbig' or row[5]=='vhigh':
            raise IOError
except:
    pass
sort_list =sortedlist[0:10]
for row in sort_list:
    print row
fo.close()




print "output for 2b"
fo = open(filename)
data1 = csv.reader(fo,delimiter=',')
sortedlist1 = sorted(data1, key=operator.itemgetter(1), reverse = False) 

for row in sortedlist:
    sort_list1 =sortedlist1[-15:]
for line in sort_list1:
    print line
fo.close()




print "output for 2c"
fo = open(filename)
data = csv.reader(fo,delimiter=',')
for row in fo:
    sortedlist = sorted(data, key=operator.itemgetter(2))
    pattern = '^v{0,1}high'
    nlist = []
    for row in sortedlist:
        if re.match(pattern, row[0]) and re.match(pattern, row[1]) and re.match(pattern, row[5]):
            nlist.append(row)
    for row in nlist:
        print row
fo.close()






print "output for 2d"
fo = open(filename)
data = csv.reader(fo,delimiter=',')
nlist2= []
for row in data:
    if row[0] == 'vhigh' and row[1] == 'med' and row[2] == '4' and\
        (row[3] == '4' or row[3] == 'more'):
        nlist2.append(row)
with open("output.csv", 'wb') as f:
    fileWriter = csv.writer(f, delimiter=',')
    for row in nlist2:
        fileWriter.writerow(row)
f.close()



