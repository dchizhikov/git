# -*- coding: utf-8 -*-
"""gitRepos.ipynb
Automatically generated by Colab.
Original file is located at
https://colab.research.google.com/drive/19pC1RxsoaD3FIIWAgEQvW5mdMMZWUdFK
"""

#!pip freeze

import os
#import random
import requests

#from google.colab import userdata
#userdata.get('test')

#os.chdir('/')
user_name = "dchizhikov"
repo_name_git = "databases"

url = "https://raw.githubusercontent.com/"+user_name+"/"+repo_name_git+"/main/git_commands.py"
response = requests.get(url)

with open('git_com.py', 'w') as f:
  f.write(response.text)

repo_up="/home/runner/gitHubConnect/"
repo_name = "databases" #UML #databases
myRepo = repo_up+repo_name
repo_url = "https://github.com/"+user_name+"/"+repo_name
os.system(f"rm -rf {myRepo}") #!rm -rf $myRepo

import git_com as gc
import importlib
importlib.reload(gc)

gc.git_clone(repo_url, repo_up)
branch = "origin_471F"
remote_branch = "main"
gc.git_pull(branch, remote_branch)

# Commented out IPython magic to ensure Python compatibility.
workFile = repo_up+repo_name+"/display_view.py" #"/git_commands.py"
#workFile = "/content/"+repo_name+"/orders_examples/links.puml"
# %cat $workFile

#%%writefile $workFile
a='''файл'''
with open(workFile, 'w') as f:
  f.write(a)

os.chdir(myRepo)
gc.git_config(user_name)
gc.git_remote(myRepo, repo_name, branch, user_name,
             os.environ['public_token'])

os.chdir(myRepo)
gc.git_add() #!git add .

message = '1 commit message'
gc.git_commit(message)

gc.git_remove("origin")
#!git remote -v

gc.git_push(branch, remote_branch)
#!git log -p