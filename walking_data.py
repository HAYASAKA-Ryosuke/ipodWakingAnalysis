from xml.dom import minidom
import csv
import glob

filedata=glob.glob("./*.xml")

write=csv.writer(file("./walkdata.csv",'w'))
write.writerow(["Time","durationString","Distance","pace","calories","walkEnd","weight"])
for data in filedata:
    tree=minidom.parse(data)
    time=tree.getElementsByTagName("time")[0].firstChild.data
    durationString=(tree.getElementsByTagName("durationString")[0].firstChild.data)
    distance=(tree.getElementsByTagName("distance")[0].firstChild.data)
    pace=(tree.getElementsByTagName("pace")[0].firstChild.data)
    colories=(tree.getElementsByTagName("calories")[0].firstChild.data)
    walkEnd=(tree.getElementsByTagName("walkEnd")[0].firstChild.data)
    weight=(tree.getElementsByTagName("weight")[0].firstChild.data)
    write.writerow([time.split("T")[0],durationString,distance,pace,colories,walkEnd,weight])
