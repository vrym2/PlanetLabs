#!/bin/bash

# Run this script to kil any processes running in a disk
# In order to unmount that disk
echo Storing the running processes details of disk 'sdb' in a text file
sudo lsof /dev/sdb | tr '' ',' > .docs/bash_scripts/process.txt

# Reading each PID of the porcess and killing it
while read -r _ PID _ _ _ _ _ _ _; do
    if [ "$PID" != "PID" ]; then
        echo "Killing the process ID: $PID from /dev/sdb"
        sudo kill -9 "$PID"
    fi
done < ".docs/bash_scripts/process.txt"