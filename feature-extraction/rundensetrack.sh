echo  "./release/DenseTrack $1 >$2"
./release/DenseTrack $1 >$2
# use find . -name '*.avi' -exec bash script.sh {} {}.traj \; on Dataset.
