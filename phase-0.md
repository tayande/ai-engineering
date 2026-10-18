# ai engineering from scratch: phase 0
## Dev Environment.
This is defined as a platform designed and configured specifically for writing, testing and debugging software programs.

## layers of ai engineering environment
there are four layers in an ai dev environment, one builds on the previous one in that order.
- ai/ml libraries which build on
- programming language runtime which build on 
- package managers which build on
- system foundations and operating system.

## Git and collaboration
A repository is a collection of files and their complete creation and change history, all managed by version control. It is a folder that contains files which in turn contain source codes for running programs.

## python Environments
A vitual environment is an independent platform that contains all the packages a program requires at runtime to run, that is seperate from the system.
- The main essence of a venv is to make sure you more than one program can exist on a device, with each of them running independently and having all the dependencies the programs need to run.
- A Lockfile: This is a file listing every package and its exact version, guaranteeing identical installs across machines
- Transitive dependency: This is like a dependency of a dependency, if you have three packages, A, B and C, with A depending on B, and B depending on C. Then package C is a transitive of package A.

## Docker for AI
A docker file is said to be a file that contains the step by step procedure for a program to install and run a container.
- A container: This is sometimes referred to as a lightweight virtual environment, and it is an isolated process using the host kernel, with its own filesystem and network.

## Data management
