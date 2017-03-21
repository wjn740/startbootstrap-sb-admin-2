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
        objects_list.append(d)
    j = json.dumps(objects_list)
    print(j)

print("Content-type: text/plain\n")
mysqlquery('select distinct `release` from distro_run_view order by `release` desc;')
