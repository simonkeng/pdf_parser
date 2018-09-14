tartype=$1

if [[ $tartype = *".tar"* ]]; then
  exec docker load < $tartype
fi

if [[ $tartype = *".tgz"* ]]; then
  exec gunzip -c $tartype | docker load
fi