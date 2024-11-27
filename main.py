import git.config as config
import importlib
import os

modules_list = ['gitHub', 'git_com']
imported_modules = {}

# Импортируем и перезагружаем модули
for module in modules_list:
    # Динамический импорт модуля
    imported_module = importlib.import_module(f"{config.folder_name}.modules.{module}")
    importlib.reload(imported_module)

    # Сохраняем модуль в словаре
    imported_modules[module] = imported_module

# Выводим все загруженные модули
print("Импортированные модули:", imported_modules)
print("user_name:", config.user_name)
print("folder_name:", config.folder_name)

gc = imported_modules['git_com']

if not os.path.exists(f'{config.repo_name}'): 
  gc.git_clone(config.repo_url, config.repo_up)
  gc.git_config(config.user_name)
  print("Имя myRepo:", config.myRepo)
  print("текущ0:", os.getcwd())
  gc.git_remote(config.myRepo, config.repo_name, config.branch, config.user_name, config._token)
  gc.git_pull(config.branch, config.remote_branch)
else:
  os.chdir(config.myRepo)
  gc.git_add() #!git add .
  message = f'git 12 commit message'
  gc.git_commit(message)
  gc.git_push(config.branch, config.remote_branch)

print("Конец")