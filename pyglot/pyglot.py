import sys
import os
import pathlib
import tokenize
import loadxml
import runpy
from core import translate_code
import traceback
import pyglotimport
        
def commandline():
    """
    usage: pyglot file.{language}.py {args}
    """
    if len(sys.argv) == 1:
        print(commandline.__doc__)
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"{os.getcwd()}: can't open file '{os.getcwd()}\\{file_path}': No such file or directory")
        sys.exit(1)

    # Get language based off of the file extension. For example, script.fr.py will look for fr.xml
    extensions = pathlib.Path(file_path).suffixes[-2:]
    language = None
    translations = None

    if len(extensions) == 2 and extensions[1] == '.py':
        language = extensions[0][1:]
    
    # Get the path of the expected xml file, and see if it exists. 
    translations = gettranslations(f'{language}.xml')
    
    # Convert the source code back into valid python
    source = translatetoen(file_path, translations)

    try:
        code = compile(source, file_path, "exec")
    except Exception as e:
        traceback.print_exception(sys.exception(), limit= -len(traceback.extract_tb(e.__traceback__)) + 1, file=None, chain=True)
        sys.exit(1)

    sys.argv = sys.argv[1:]
    try:
        with runpy._TempModule("__main__") as temp_module:
            mod_globals = temp_module.module.__dict__
            runpy._run_code(code, mod_globals, mod_name="__main__")
    except Exception as e:
        traceback.print_exception(sys.exception(), limit= -len(traceback.extract_tb(e.__traceback__)) + 3, file=None, chain=True)
        sys.exit(1)

def gettranslations(filename):
    xml_file_path = loadxml.locatexml(filename)
    if xml_file_path:
        translations = loadxml.translations_from_xml(xml_file_path)
    else:
        print(f'Could not locate {os.path.join('localizations', f'{filename.split('.')[-2]}.xml')}')
        sys.exit(1)
    return translations

def translatetoen(file_path, translations):
    with open(file_path, encoding='utf-8') as f:
        source = tokenize.untokenize(list(translate_code(f.readline, translations)))
    return source

if __name__=="__main__":
    sys.path.append(os.getcwd())
    commandline()