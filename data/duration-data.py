#!/usr/bin/env python3

import mysql.connector
from collections import OrderedDict
import collections
import json

config = {
        'user' : 'qadb',
        'password' : '',
        'host' : '147.2.207.30',
        'database' : 'qadb',
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
        d['host'] = row[0]
        d['testsuite'] = row[1]
        d['testcase'] = row[2]
        d['product'] = row[3]
        d['test_time'] = str(row[4])
        objects_list.append(d)
    j = json.dumps(objects_list)
    print(j)

print("Content-type: text/plain\n")
mysqlquery('select distinct `host`,`testsuite`,`testcase`,`product`,avg(`test_time`)  from performance_view where `host` = \'apac2-ph022.bej.suse.com\' or `host` = \'apac2-ph027.bej.suse.com\' or `host` = \'apac2-ph023.bej.suse.com\' or `host` = \'apac2-ph026.bej.suse.com\' group by `testsuite`,`testcase`,`host` order by `host`,`product`;')

