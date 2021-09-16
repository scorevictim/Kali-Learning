#!/bin/bash
if [ $1 == "" ]
then
echo "Please at least type a range"
echo "Example: ./ping.sh 192.168.1"


else
for ip in 'seq 1 254'; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" $
done
fi
