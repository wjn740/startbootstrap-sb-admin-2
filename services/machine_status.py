#!/usr/bin/env python3

from paramiko import SSHClient
import paramiko
import sys
import socket
import collections
import json

hosts = ['209', '210', '226', '227']

ssh = SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

objects_list = []
for host in hosts:
    hostname="".join(['147.2.207.',host])
    try:
        ssh.connect(hostname, username='root', password='susetesting')
    except TimeoutError:
        continue;

    try:
        stdin, stdout, stderr = ssh.exec_command('screen -ls')
    except socket.timeout:
        continue


    msg = "".join(stdout.readlines())

    d = collections.OrderedDict()
    d['hostname'] = hostname
    d['msg'] = msg
    objects_list.append(d)


j = json.dumps(objects_list)

print("Content-type: text/plain\n")
print(j)
    #for line in stdout.readlines():
    #    print("{0:s}".format(line))


