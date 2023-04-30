#!/bin/bash

# To check the name sof the disks associated
echo Disks available in GCP VM:
gcloud compute disks list

# Make sure to create asnpashot before any disk paritions
echo "Open this link and Follow instructions to create a snap shot of disk"
echo "https://cloud.google.com/compute/docs/disks/create-snapshots"

# Get the parition names and note them
echo Disk partitons names/links
echo Root disk must be "sda"
echo Other miunted disks must from "sdb"
lsblk

# Unmounting the extra disks
umount_sdb=$(sudo umount /dev/sdb)
var_umount="umount: /mnt/disks/diss_dir: target is busy."
if [ "$umount_sdb" ==  "$var_umount" ]; then
    echo if it says target is busy, run "kill_process.sh"
fi



