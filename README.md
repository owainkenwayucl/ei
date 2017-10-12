# Environment Inspector

This repository contains a Python 3 script to help with setting up packages which at some point in the install process source a shell script to set a lot of variables.

This allows you to:

1. Save the current environment state to a file.

2. Source the shell script (or whatever).

3. Compare the current environment with the file.

## Saving the environment

```none
$ python3 ei.py -a save -f old.env
```

## Comparing old and new environments

```none
$ python3 ei.py -a compare -f old.env
```

This will print out a python dictionary with the differences.  More usefully you can use the `-m` flag to get more usable outputs.

| mode         | function                                                                                                             |
|--------------|----------------------------------------------------------------------------------------------------------------------|
| `dict`       | prints a python dict (default)                                                                                       |
| `bash`       | prints a script that will change from the old to new environment.                                                    |                     
| `bash_smart` | as `bash` but attempts to base modified enviroment variables on the orginal ones (`export PATH=/usr/bin:$PATH` etc.) |