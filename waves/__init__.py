import pkgutil
import importlib
from . import _wave_base
from .wave_1 import Wave1
from .wave_2 import Wave2
from .wave_3 import Wave3
from .wave_4 import Wave4
from .wave_5 import Wave5
from .wave_6 import Wave6
from .wave_7 import Wave7
from .wave_8 import Wave8

# Dynamically import all modules in this package
# for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
#     importlib.import_module(f"{__name__}.{module_name}")
