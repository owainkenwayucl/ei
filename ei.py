'''
   This program is a set of tools for inspecting the user's environment for changes.
   The goal is to ease the generation of module files for packages which use a .sh
   file to set a massive list of environment variables.

   Owain Kenway, 2017
'''

# os.environ is weird, so convert into a dictionary.
def extract_environment():
    import os

    r = {}

    for a in os.environ:
        r[a] = os.environ[a]

    return r

# Function to record the current environment into a file.
def record_environment(filename, overwrite=False):
    import os
    import sys
    import pickle

# check to see if the file exists.
    if (os.path.exists(filename) and (overwrite==False)):
        print("The file " + filename + " already exists - exiting.")
        sys.exit(0)
    
# open our file
    f = open(filename, 'wb')

# pickle our environment to the file
    pickle.dump(extract_environment(), f)

# close our file
    f.close()

# Function to compare the current environment with a file.
# This should return a dict of dicts with the keys:
# new - variables that are new
# modified - variables that are modified
# deleted - variables that are removed
def compare_environment(old_environment, new_environment):
    new_vars = {}
    modified_vars = {}
    deleted_vars = {}
    r = {}

    old_keys = old_environment.keys()
    new_keys = new_environment.keys()

# new keys
    for a in new_keys:
        if (not (a in old_keys)):
            new_vars[a] = new_environment[a]
# key in both
        else:
            if (new_environment[a] != old_environment[a]):
                modified_vars[a] = new_environment[a]

# deleted keys
    for a in old_keys:
        if (not (a in new_keys)):
            deleted_vars[a] = old_environment[a]


# construct our return dictionary
    r['new'] = new_vars
    r['modified'] = modified_vars
    r['deleted'] = deleted_vars

    return r



# Load and return an environment from a file
def load_environ(filename):
    import os
    import sys
    import pickle

# check to see if the file exists.
    if (not os.path.exists(filename)):
        print("The file " + filename + " doesn't exit - exiting.")
        sys.exit(0)

# get old environment
    f = open(filename, 'rb')

# read in the data
    old_environment = pickle.load(f)

# close our file
    f.close()

    return old_environment

# In lieu of a main function in python...
if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Inspect environment.')
    parser.add_argument('-f', metavar='filename', type=str, help='file')
    parser.add_argument('-a', metavar='action', type=str, help='save|compare')
    parser.add_argument('-o', action='store_true', help='overwrite')

    args = parser.parse_args()

    if (args.a == None):
        print('Error - must pick an action')
        sys.exit(2)

    if (args.f == None):
        print('Error - must specify a file')
        sys.exit(1)

    if (args.a.lower() == 'save'):
        record_environment(args.f, args.d)
    elif (args.a.lower() == 'compare'):
        diff = compare_environment(load_environ(args.f), extract_environment())
        print(diff)
    else:
        print('Error - invalid action: ' + args.a.lower())
        sys.exit(3)
