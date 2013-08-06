# -*- coding: utf-8 -*-

from xml.dom import minidom
import csv
import glob
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

class dataset(object):
        time = []
        duration = []
        distance = []
        pace=[]
        colories=[]
        walkEnd=[]
        weight=[]
def saveplot(data,ylabel):
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.plot(dates,data,'o-')
    days=mdates.AutoDateLocator()
    daysFmt=mdates.DateFormatter("%m/%d")
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(daysFmt)
    plt.title("year:"+str(datetime.datetime.now().year))
    plt.xlabel("Days")
    plt.ylabel(ylabel)
    plt.savefig(str(datetime.datetime.now().year)+ylabel)

filedata=glob.glob("./*.xml")
write=csv.writer(file("./walkdata.csv",'w'))
write.writerow(["Time","durationString","Distance","pace","calories","walkEnd","weight"])

for data in filedata:
    tree=minidom.parse(data)
    time=tree.getElementsByTagName("time")[0].firstChild.data
    dataset.time.append(time.split("T")[0])
    durationString=(tree.getElementsByTagName("durationString")[0].firstChild.data)
    dataset.duration.append(durationString)
    distance=(tree.getElementsByTagName("distance")[0].firstChild.data)
    dataset.distance.append(distance)
    pace=(tree.getElementsByTagName("pace")[0].firstChild.data)
    dataset.pace.append(pace)
    colories=(tree.getElementsByTagName("calories")[0].firstChild.data)
    dataset.colories.append(colories)
    walkEnd=(tree.getElementsByTagName("walkEnd")[0].firstChild.data)
    dataset.walkEnd.append(walkEnd)
    weight=(tree.getElementsByTagName("weight")[0].firstChild.data)
    dataset.weight.append(weight)
    write.writerow([time.split("T")[0],durationString,distance,pace,colories,walkEnd,weight])
dates=[]

for i in dataset().time:
    dates.append(datetime.datetime.strptime(i,'%Y-%m-%d'))

saveplot(dataset().distance,"distance")
saveplot(dataset().colories,"colories")
saveplot(dataset().walkEnd,"walkEnd[walk]")
