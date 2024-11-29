import importlib
#import tg_bot.main as tg
folder = 'git' #['git', 'tg_bot', 'databases', '...']
module = 'main' #['main', 'sqlite.main', '...']

main_sub = importlib.import_module(f"{folder}.{module}")
#importlib.reload(main_sub)
