service docker stop
thin_check /home/docker/devicemapper/devicemapper/metadata
thin_check --clear-needs-check-flag  /home/docker/devicemapper/devicemapper/metadata
service docker start
docker run -it --rm --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" -v=$(pwd)/..:$(pwd)/.. -w=$(pwd) apollo bash