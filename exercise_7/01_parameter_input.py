import sys

num_param = len(sys.argv) - 1   # -1 because the script itself is also contained in the argument list.
if num_param == 0:
    print("No parameters given on command line. Please specify at least one.")

for i in range(1, len(sys.argv)):
    print("parameter " + str(i) + ":", sys.argv[i]) 
