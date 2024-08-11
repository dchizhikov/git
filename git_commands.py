import os
def git_test():
  print("test mir")
def git_clone(repo):
#  !git clone $repo #{repo}
  os.system(f"git clone {repo}")
