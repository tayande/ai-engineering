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


## The tool interface
The tool interface is what makes it possible for a model to ask a program to do an action that it cannot do by itself. so there are two players in the picture here:
- the model (the llm): this is basically the chatbot you are communicating to. It is also the brain that decides what to do, and what should happen.
- the host: The regular program around the model, if a model decides for an action, then the host is what actually does that action. it can be a python script or anything but connected to the model.
### the tool has three parts(plus the code)
- name: a fixed id the program can match always instead of guessing
- description: tell the model when to use and how to use it.
- input schema: the exact shape of the inputs of the tool, and also its outputs.

### The four step loop
All ai models or tool system works this way:
- describe(host): The host gives the model a list of tools
- decide(model): The model reads the user's message and picks one of three options:
    1. answer directly in text
    2. call a tool by producing a structured request, or
    3. refuse.

- execute(host): The host first checks the arguments match the schema.
- Observe(model): the host gives the result back to the model, the model either writes the result as final answer or asks for another tool

### pure vs. consequential tools(safety)
pure tools only read, and they are safe to user all the time while consequential tools change something, they must be gated.


## Apis and keys: 
An api is how my source code talks to another program over the internet. so for ai, it means my python program will make a call to claude, chatgpt or gemini. 
All api calls have four parts:
- endpoints: the web address you send to.
- api key: a secret password that proves who you are and who to bill.
- request body: what you are asking, in json
- response body: the reply that the external program sends back as answer to your request


## Jupyter notebooks
A notebook is a document made of cells. There are two kinds of cells:
- code cells: run python
- markdown cells: hold notes and headlings that explain what you're doing
