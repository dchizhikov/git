import importlib
import sys

folder = '/content/git' #['git', 'tg_bot', 'databases', '...']
module = 'main' #['main', 'sqlite.main', '...']

sys.path.append(f'{folder}')


#main_sub = importlib.import_module(f"{folder}.{module}")
#importlib.reload(main_sub)
tg = importlib.import_module(module)

#tg.test()