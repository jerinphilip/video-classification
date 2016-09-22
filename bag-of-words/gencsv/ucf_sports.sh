#! /bin/sh

echo "File will be saved as ucf_sports.csv from the calling directory"
echo "It is assumed that you are in the folder containing ucf_sports directory"

echo class,filename >ucf_sports.csv
find ucf_sports -name '*.avi.traj'|awk  -F '/' '{printf("%s,%s\n",$2,$0)}' >>ucf_sports.csv

