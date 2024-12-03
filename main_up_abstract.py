import importlib
import sys

folder = '/content/tg_bot' #['git', 'tg_bot', 'databases', '...']
module = 'main' #['main', 'sqlite.main', '...']

sys.path.append(f'{folder}')
main_sub = importlib.import_module(module)