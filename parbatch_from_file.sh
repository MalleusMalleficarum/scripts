#!/bin/bash

while getopts 'i:' OPTION ; do
    case "$OPTION" in

        i)
            printf "Instance:\t $OPTARG \n"
            INSTANCE=$OPTARG
    esac
done



if [ "x" == "x$INSTANCE" ]; then
  echo "-i [option] is required: hypergraph instance"
  exit
fi
module load system/parbatch

parbatch $INSTANCE


