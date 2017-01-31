from os.path import dirname, basename, isfile
import glob

excepts = ['__init__', 'widget']
# Find all *.py files and add them to import
modules = [basename(f)[:-3] for f in glob.glob(dirname(__file__)+"/*.py") if
        isfile(f)]
__all__ = [f for f in modules if f not in excepts]
