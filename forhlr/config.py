#[Account Information]
instance_directory           = "/work/workspace/scratch/re9207-wallshaw-instances-0/wallshaw_hgr"
application_file             = "/home/kit/iti/re9207/kahypar/release/kahypar/application/KaHyPar"
configuration_file           = "/home/kit/iti/re9207/kahypar/config/wallshaw.ini"
#[Experiment Information]
workpath_directory = "/work/workspace/scratch/re9207-wallshaw-0/"
experiment_name =  "wallshaw_2"
#[Experiment Configuration]
launch_script = "evolutionary.py"
k             = [2,4,8,16,32,64]
epsilon       = [0.01,0.03,0.05]
seed          = [1]
time_limit    = [86400]
objective     = ["km1"]
mode          = ["direct"]
#[MPI Experiment Configuration]
quick_ip      = [0]
mpi_pop_size  = ["as_usual"]

