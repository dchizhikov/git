import importlib
import sys

folder = sys.argv[1] #myRepo
module = 'main' #['main', 'sqlite.main', '...']

sys.path.append(f'{folder}')
main_sub = importlib.import_module(module)