from subprocess import Popen, PIPE
import ntpath
import argparse
import time
import re
import math
import os
import sys
import config


KaHyPar = config.application_file
Context = config.configuration_file
###################################

parser = argparse.ArgumentParser()
parser.add_argument("h", type=str)#Hypergraph File
parser.add_argument("k", type=int)#K
parser.add_argument("epsilon", type=float)#epsilon
parser.add_argument("seed", type=int)#Seed
parser.add_argument("timelimit", type=int)#time limit
parser.add_argument("objective", type=str)#objective
parser.add_argument("mode", type=str)#mode
parser.add_argument("logfile", type=str)#the log file

args = parser.parse_args()


graph = args.h
k = args.k
seed = args.seed
epsilon = args.epsilon
objective = args.objective
mode = args.mode
timelimit = args.timelimit
logfile = args.logfile


start = time.time()
p = Popen([KaHyPar,
           '-h'+str(graph),
           '-k'+str(k),
           '-e'+str(epsilon),
           '-o'+str(objective),
           '-m'+str(mode),
           '-p'+Context,
           '--seed='+str(seed),
           '--time-limit='+str(timelimit)
           ], stdout=PIPE, bufsize=1)

best = sys.maxsize
connectivity = sys.maxsize
for line in iter(p.stdout.readline, b''):
    s = str(line).strip()
    #print(s)

    if("Hyperedge Cut  (minimize) = " in s):
      #print(s)
      cut = s.split('Hyperedge Cut  (minimize) = ')[1]
      #print(temp)

    string = "SOED           (minimize) = "
    if(string in s):
      soed = s.split(string)[1]
      #print(temp)
    string = "(k-1)          (minimize) = "
    if(string in s):
      connectivity = int(s.split(string)[1])
      #print(temp)
    string = "Absorption     (maximize) = "
    if(string in s):
      absorption = s.split(string)[1]
      #print(temp)
    string ="Imbalance                 = "
    if(string in s):
      imbalance = s.split(string)[1]
      #print(temp)
    string = "Partition time                     = "
    if(string in s):
      time = s.split(string)[1]
      #print(connectivity)
     # print(best)
      #print(connectivity < best)
      print("Cut=" +cut + " SOED=" + soed + " Connectivity=" + str(connectivity) + " Absorption=" + absorption + " Imbalance=" + imbalance + " Time=" +time + " Graph=" + graph + " seed=" + str(seed) + " k=" + str(k))

      if( connectivity < best ):
         f = open(logfile, "a")
         print("Cut=" +cut + " SOED=" + soed + " Connectivity=" + str(connectivity) + " Absorption=" + absorption + " Imbalance=" + imbalance + " Time=" +time + " Graph=" + graph + " seed=" + str(seed) + " k=" + str(k))
         f.write("Cut=" +cut + " SOED=" + soed + " Connectivity=" + str(connectivity) + " Absorption=" + absorption + " Imbalance=" + imbalance + " Time=" +time + " Graph=" + graph + " seed=" + str(seed) + " k=" + str(k) +"\n")

         best = connectivity
         f.close()
