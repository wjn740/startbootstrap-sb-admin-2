#!/usr/bin/env python3

import mysql.connector
from collections import OrderedDict
import collections
import json

config = {
        'user' : 'jnwang',
        'password' : 'susetesting',
        'host' : '147.2.207.100',
        'database' : 'reportdb',
        'raise_on_warnings': True,
        }


def mysqlquery(query):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = cnx.cursor()
    if query:
        cursor.execute(query)
    rows = cursor.fetchall()
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d['project'] = row[0]
        d['baselines'] = []
        #start cursor1 query
        query1=('select distinct `r_release`,`r_run_id` from distro_plan_pair_view where `q_release` = \'' + d['project'] + '\' and `q_release` <> `r_release`;');
        cursor.execute(query1)
        rows1 = cursor.fetchall()
        for row1 in rows1:
            d1 = collections.OrderedDict()
            d1['r_release'] = row1[0]
            d1['r_run_id'] = row1[1]
            d['baselines'].append(d1)
        objects_list.append(d)
    j = json.dumps(objects_list)
    print(j)

print("Content-type: text/plain\n")
mysqlquery('select distinct `release` from distro_run_view order by `release` desc;')
