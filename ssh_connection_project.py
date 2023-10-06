#!/usr/bin/python3

import paramiko
import subprocess
import csv

filename = 'hosts.csv'
output = 'output.txt'
csv = csv.reader(open(filename))
f = open(output, "a")
x = slice (2,-3)

def ssh_connection(ip, user, passwd, command):
    client = paramiko.SSHClient()
    # if you wanted to use ssh keys instead, uncomment the line below
    #client.load_host_keys('/home/user/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if (ssh_session.active) & (command == 'cat /etc/hostname'):
        global hostname
        ssh_session.exec_command(command)
        hostname = str(ssh_session.recv(1024))[x]
    else:
        global result
        ssh_session.exec_command(command)
        result = str(ssh_session.recv(1024))[x]
    return

for line in csv:
    ip = line[0]
    user = line[1]
    password = line[2]
    
    command = 'cat /etc/hostname'
    ssh_connection(ip, user, password, command)
    
    command = 'ls /var/www/'
    ssh_connection(ip, user, password, command)
    
    if result:
        f.write("IP: {}, Hostname: {}, Web Server: {}\n".format(ip, hostname, result))
    else:
        f.write("IP: {}, Hostname: {}\n".format(ip, hostname))
        
f.close()