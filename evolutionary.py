from subprocess import Popen, PIPE
import ntpath
import argparse
import time
import re
import math
import os
import sys
import config

###################################
# SETUP ENV
###################################

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

for line in iter(p.stdout.readline, b''):
    s = str(line).strip()
    #print(s)
    if("RESULT" in s):
      temp = s.split("connectivity=")[1]
      #print(temp)
      conn = int(temp.split(" ")[0])
      if (conn < best):
        file = open(logfile, "a")
        print(s)
        file.write(s)
        file.close()
        best = conn


