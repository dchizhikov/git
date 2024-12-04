import importlib
import sys

repo_up = sys.argv[1]
repo_name = sys.argv[2]
folder = repo_up+repo_name #['git', 'tg_bot', 'databases', '...']
module = 'main' #['main', 'sqlite.main', '...']

sys.path.append(f'{folder}')
main_sub = importlib.import_module(module)