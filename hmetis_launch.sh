#!/bin/bash

while getopts 's:l:d:h:k:e:t:' OPTION ; do
    case "$OPTION" in
        s)
            printf "Seed:\t\t $OPTARG \n"
            seed=$OPTARG;;
        l)
            printf "Tag:\t\t $OPTARG \n"
            LOG_FILE=$OPTARG;;
        d)
            printf "Tag:\t\t $OPTARG \n"
            LOG_FILE_DETAILED=$OPTARG;;
        h)
            printf "Tag:\t\t $OPTARG \n"
            instance=$OPTARG;;
        k)
            printf "Tag:\t\t $OPTARG \n"
            k=$OPTARG;;
        e)
            printf "Tag:\t\t $OPTARG \n"
            epsilon=$OPTARG;;            
        t)
            printf "Tag:\t\t $OPTARG \n"
            timeLimitSeconds=$OPTARG;;        
            
            
            esac

done



end=$((SECONDS+$timeLimitSeconds))
i=0
num1=9999999999999999999 #arbitrarily high
startTime=$(date +%s%N)
while [ $SECONDS -lt $end ]; do


	curSeed=$((seed + i * 5))
	test=$(python start_soed_hmetis-k.py $instance $k $epsilon $curSeed --nruns=1 | grep "RESULT") # >> /home/andre/server-home/scripts/test.txt
	#echo $test
  curTime=$(($(date +%s%N)-$startTime))
  fin=$(echo "scale=9; $curTime/1000000000" | bc)
  
	tes=$(echo $test | cut -d' ' -f 8)
  testo=$(echo $tes | cut -d'=' -f 2)
  bool=$(echo $num1'>'$testo | bc -l)
  if [ $bool -eq 1 ]; then 
    #echo $fin
    echo $test totalTime=$fin >> $LOG_FILE
    echo $test totalTime=$fin >> $LOG_FILE_DETAILED
    num1=$testo
  else
    #echo $fin
    echo $test totalTime=$fin >> $LOG_FILE_DETAILED
  fi
  #sed 's/*initialSOED0=[0-9]*\.[0-9].*/initialSOED0=[0-9]*\.[0-9]/g' test
  	i=$((i + 1))
done
