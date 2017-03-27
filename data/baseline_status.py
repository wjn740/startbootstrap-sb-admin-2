#!/usr/bin/env python3

import mysql.connector
from collections import OrderedDict
import collections
import json
import cgi

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
        d['testcase'] = row[1]
        d['testsuite'] = row[2]
        d['Count'] = row[3]
        objects_list.append(d)
    j = json.dumps(objects_list)
    print(j)


form = cgi.FieldStorage()
print("Content-type: text/plain\n")
if "r_run_id" not in form or "r_release" not in form:
    print("<H1>ERROR:No parameters from the request</H1>")
r_release = form.getvalue('r_release')
r_run_id = form.getvalue('r_run_id')


mysqlquery('select `host`,`testcase`,`testsuite`,count(`testsuite`) from performance_view where (`host` = \'apac2-ph022.bej.suse.com\' or `host` = \'apac2-ph027.bej.suse.com\' or `host` = \'apac2-ph023.bej.suse.com\' or `host` = \'apac2-ph026.bej.suse.com\') and `product` = \''+ r_release + '\' and `comment` like \'%' + r_run_id + '%\' group by `host`,`testsuite`,`testcase`;')
