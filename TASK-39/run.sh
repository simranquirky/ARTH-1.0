#!/bin/bash


yum install httpd -y
yum install python3 -y
yum install docker -y
cd Docker-Arth_Task-39/
mv index.html /var/www/html
mv style.css /var/www/html
mv main.js /var/www/html
mv Docker-logo.png /var/www/html
mv background.gif /var/www/html
mv docker.py /var/www/cgi-bin
cd 
cd /var/www/cgi-bin
chmod +x docker.py
systemctl start docker
systemctl start httpd

