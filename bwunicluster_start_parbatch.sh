#!/bin/bash
MAXQUEUEVALUE=50
while getopts 'e:d:' OPTION ; do
    case "$OPTION" in
        e)
            printf "Experiment:\t\t $OPTARG \n"
            experiment=$OPTARG;;

        d)
            printf "Workspace path:\t\t $OPTARG \n"
            workpath=$OPTARG;;
    esac
done
if [ "x" == "x$experiment" ]; then
  echo "-e [option] experiment name is required"
  exit
fi

if [ "x" == "x$workpath" ]; then
  echo "-d [option] workspace path is required"
  exit
fi


mkdir "$workpath$experiment/scripts"
cp * "$workpath$experiment/scripts"
cd "$workpath$experiment/scripts"

INSTANCE_DIR="$workpath$experiment/jobs/"



    for instance in $INSTANCE_DIR/*;
    do
        COUNTER=`showq | egrep "Running|Idle|Deferred" | wc -l`
        echo "queue has $COUNTER $MAXQUEUEVALUE"
        while [ $COUNTER -ge $MAXQUEUEVALUE ]
        do
            echo "waiting to submit"
            sleep 30s
            COUNTER=`showq | egrep "Running|Idle|Deferred" | wc -l`
            echo queue has $COUNTER
        done
        ###################################
        # singlenode
        ###################################
        msub -q singlenode -l nodes=1:ppn=16,pmem=3800mb,walltime=1:12:00:00,naccesspolicy=singlejob ./bwclusterwrapper.sh "./parbatch_from_file.sh -i$instance"
        ###################################
        ###################################
        # develop
        ###################################
        #msub -q develop -l nodes=1:ppn=16,pmem=100mb,walltime=00:00:02:00,naccesspolicy=singlejob ./bwclusterwrapper.sh "./parbatch_from_file.sh -i $instance"
        ###################################
    done



