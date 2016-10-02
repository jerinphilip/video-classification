#! /bin/sh

folder_path="/Neutron9/jerin/datasets/$1"
ls $folder_path
echo class,filename > "$1.csv"
find $folder_path -name '*.avi.traj'|awk  -F '/' '{printf("%s,%s\n",$7,$0)}' >> ucf_sports.csv
find $folder_path -name '*.avi.traj'|awk  -F '/' '{printf("%s,%s\n",$7,$0)}' 


