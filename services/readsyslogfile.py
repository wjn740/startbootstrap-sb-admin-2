#!/usr/bin/env python

from dateutil.parser import parse
from datetime import datetime
from collections import OrderedDict
import collections
import json



objects_list = []

with open('youlogfile.log', 'rU') as f:
  for line in f:
    line = line.split("#")
    item=parse(line[0])
    now=datetime.now()
    diff=now-item
    if diff.seconds < 60:
        t = str(diff.seconds) + " seconds ago" 
        line=line[2].split(": ")
        m = line[1]
    elif diff.seconds < 120:
        t = "a minute ago" 
        line=line[2].split(": ")
        m = line[1]
    elif diff.seconds < 3600:
        t = str(diff.seconds/60) + " minutes ago"
        line=line[2].split(": ")
        m = line[1]
    elif diff.seconds < 7200:
        t = "an hour ago"
        line=line[2].split(": ")
        m = line[1]
    elif diff.seconds < 86400 and diff.days == 0:
        t = str(diff.seconds/60/60) + " hours ago"
        line=line[2].split(": ")
        m = line[1]
    elif diff.days == 1:
        t = "a day ago"
        line=line[2].split(": ")
        m = line[1]
    elif diff.days > 1:
        line=line[2].split(": ")
        t = str(diff.days) + " days ago"
        m = line[1]
    d = collections.OrderedDict()
    d['msg'] = m
    d['time'] = t
    objects_list.append(d)


j = json.dumps(objects_list)

print "Content-type: text/plain\n"
print j
