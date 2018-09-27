# Shell script for loading docker images 
# from tarballs or tgz's

# NOTE: not necessary anymore, but keeping it around

tartype=$1

if [[ $tartype = *".tar"* ]]; then
  exec docker load < $tartype
fi

if [[ $tartype = *".tgz"* ]]; then
  exec gunzip -c $tartype | docker load
fi

