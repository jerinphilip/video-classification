#! /bin/sh

folder_path="$1$2"
#ls $folder_path
echo class,filename > "$2.csv"
#find $folder_path -name '*.avi.traj'|awk  -F '/' '{printf("%s,%s\n",$7,$0)}' >> ucf_sports.csv
find $folder_path -name '*.avi.traj'| grep -e ".*small.*" | awk  -F '/' '{printf("%s,%s\n",$8,$0)}' 
find $folder_path -name '*.avi.traj'| grep -e ".*small.*" | awk  -F '/' '{printf("%s,%s\n",$8,$0)}' >> "$2.csv"
