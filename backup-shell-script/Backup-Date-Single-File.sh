#!/bin/sh


backup_file=$(date +%Y%m%d-%H%M)_$1
backup_dir=.backups

cp "$1" "$backup_dir/$backup_file" &&\
chmod 600 "$backup_dir/$backup_file" &&\
echo "[+]: file backed up as  --->  $backup_dir/$backup_file" ||\
echo "[-]: backup failed"
