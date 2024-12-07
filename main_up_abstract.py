import importlib
import os
import sys

folder = sys.argv[1] #myRepo
module = 'main' #['main', 'sqlite.main', '...']
sys.path.append(f'{folder}')

try:
    main_sub = importlib.import_module(module)
    main_sub = importlib.reload(main_sub)  # Перезагрузка модуля
except ImportError as e:
    print(f"Ошибка импорта модуля '{module}': {e}")