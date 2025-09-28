#!/bin/bash
apt-get update
apt-get install vim -y
apt-get remove zip -y
echo "My external script" > /home/vagrant/testing.txt
free -g /home/vagrant/memory.txt