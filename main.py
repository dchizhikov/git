import importlib
import os
import sys

repo_up_git = '/content/git'

sys.path.append(repo_up_git)
config = importlib.import_module('config')
sys.path.append(f'{repo_up_git}/modules/')

print("Начало")

folder_modules = 'modules'
folder_modules_path = repo_up_git+'/'+folder_modules
modules_list = [os.path.splitext(file)[0] for file in os.listdir(folder_modules_path) if file.endswith('.py')]
imported_modules = {}

# Импортируем и перезагружаем модули
for module in modules_list:
    # Динамический импорт модуля
    imported_module = importlib.import_module(module)
#    importlib.reload(imported_module)
    imported_modules[module] = imported_module

gc = imported_modules['git_com']
test = imported_modules['test_hello']
test.hello()
'''
if not os.path.exists(f'{config.repo_name}'): 
  gc.git_clone(config.repo_url, config.repo_up)
  gc.git_config(config.user_name)
  gc.git_remote(config.myRepo, config.repo_name, config.branch, config.user_name, config._token)
  gc.git_pull(config.branch, config.remote_branch)
else:
  os.chdir(config.myRepo)
  print(os.getcwd(), config.branch)
  gc.git_add() #!git add .
  message = f'git main_up_abstract commit message'
  gc.git_commit(message)
  gc.git_push(config.branch, config.remote_branch)
'''
print("Конец")