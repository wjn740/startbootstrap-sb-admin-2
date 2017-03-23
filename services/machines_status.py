#!/usr/bin/env python

from paramiko import SSHClient
import paramiko
import sys
import socket
import collections
import json
import re

hosts = ['209', '210', '226', '227']

ssh = SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

objects_list = []
for host in hosts:
    hostname="".join(['147.2.207.',host])
    try:
        ssh.connect(hostname, username='root', password='susetesting', timeout=5, banner_timeout=3)
    except socket.error:
        continue;

    try:
        stdin, stdout, stderr = ssh.exec_command('screen -ls')
    except socket.timeout:
        continue


    msg = "".join(stdout.readlines())
    s="The current ration is (\d+)\.?(\d+)?" 
    for l in msg.splitlines():
        m=re.search(s,l)
        if m:
            progress=(m.group(1)+"."+m.group(2))
        
        
         
    d = collections.OrderedDict()
    d['hostname'] = hostname
    d['msg'] = msg
    d['progress'] = progress
    objects_list.append(d)


j = json.dumps(objects_list)

print("Content-type: text/plain\n")
print(j)
    #for line in stdout.readlines():
    #    print("{0:s}".format(line))


