#!/bin/bash
node_proc=`ps -ef | grep node | grep -v grep | wc -l`
if [[ ${node_proc}  -lt 2 ]] ; then
  echo "to start node"
  cd /data/django_vue/web ; /usr/local/bin/npm run serve >/dev/null 2>&1 &
else
  echo "node_proc is running..."
fi
