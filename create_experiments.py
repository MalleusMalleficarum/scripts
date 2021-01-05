import itertools
import glob
import config
import os

instance_names = glob.glob(config.instance_directory + '/*.hgr')

print(instance_names)
experiments = list(itertools.product(instance_names, config.k, config.epsilon, config.seed, config.time_limit, config.objective, config.mode))


log_directory = config.workpath_directory + config.experiment_name + "/log"
job_directory = config.workpath_directory + config.experiment_name + "/jobs"
os.mkdir(config.workpath_directory + config.experiment_name)
os.mkdir(log_directory)
os.mkdir(job_directory)
f = open(config.workpath_directory + config.experiment_name + "/taskfile", "w+")



for experiment in experiments:
    truncated_graph_name = experiment[0].rsplit('/',1)[1]

    print(truncated_graph_name)
    logfile = log_directory +"/" +  truncated_graph_name+"_"+ str(experiment[1])+"_"+ str(experiment[2]).replace('.','') +"_" + str(experiment[3]) +"_"+ str(experiment[4])+"_"+ str(experiment[5])+"_"+ str(experiment[6])
    print(logfile)

    command = config.launch_script + " " + str(experiment[0])+ " " + str(experiment[1])+ " " + str(experiment[2])+ " " + str(experiment[3])+ " " + str(experiment[4])+ " " + str(experiment[5])+ " " + str(experiment[6]) +" "+ logfile
    print(command)
    f.write("python " + command+"\n")


f.close()
smallfile = None
lines_per_file = 16
with open(config.workpath_directory + config.experiment_name +"/taskfile") as bigfile:
  for lineno, line in enumerate(bigfile):
    if lineno % lines_per_file == 0:
      if smallfile:
        smallfile.close()
      small_filename = job_directory + "/" + str(lineno / lines_per_file)
      print(small_filename)
      smallfile = open(small_filename, "w+")
    smallfile.write(line)
  if smallfile:
    smallfile.close()


