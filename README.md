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
| `bash_smart` | as `bash` but attempts to base modified enviroment variables on the original ones (`export PATH=/usr/bin:$PATH` etc.) |

## When Python 3 gets in the way

Unfortunately sometimes you want to inspect environmental changes when having one of our Python 3 modules loaded will get in the way.  To fix this, you can save the two environments to two different text files with `env > somefilename` and then use forensic mode to compare them.

e.g.

```none
$ env > old_environment.txt
```
*(source the .sh files that change the environment)*
```none
$ env > new_environment.txt
$ module load python/3.6.3
$ python3 ei.py -a forensic -f old_environment.txt -n new_environment.txt -m bash_smart
```

This will generate a `bash` script that takes the environment from the one in `old_environment.txt` to the one in `new_environment.txt`.
