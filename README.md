## Introduction
This is a port of the MCMC code from the original ESM repo. The only change is we
add a `setup.py` file to allow for installing this as a repo.

## Installation
You can install the repo by first installing esmfold and openfold, then installing
this repo itself.  This can be done by doing

```
pip install "fair-esm[esmfold]"
# OpenFold and its remaining dependency
pip install 'dllogger @ git+https://github.com/NVIDIA/dllogger.git'
pip install 'openfold @ git+https://github.com/aqlaboratory/openfold.git@4b41059694619831a7db195b7e0988fc4ff3a307'
```

Finally, run 

```
pip install -e .
```
