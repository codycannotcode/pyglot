import sys
import importlib.util
import os
import tokenize
from pyglot import gettranslations, translatetoen


class PyglotFinder:

    def find_spec(self, fullname, path, target=None):
        pyglotfile = fullname.split('.')[-1]
        if '_' not in pyglotfile:
            return None

        pyglotlanguage = pyglotfile.split('_')[-1]
        if len(pyglotlanguage) != 2:
            return None

        filename = pyglotfile.split('_')[0] + '.' + pyglotlanguage + '.py'

        if not path:
            path = sys.path
        for entry in path:
            if os.path.exists(filename):
                return importlib.util.spec_from_file_location(fullname, filename, loader=PyglotLoader())
        return None

class PyglotLoader:
    def create_module(self, spec):
        return None  # Use default module creation

    def exec_module(self, module):
        language = module.__spec__.origin.split('.')[-2]
        translations = gettranslations(f'{language}.xml')
    
        code = translatetoen(module.__spec__.origin, translations)
        exec(code, module.__dict__)

sys.meta_path.append(PyglotFinder())