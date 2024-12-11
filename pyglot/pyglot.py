import sys
import os
import pathlib
import tokenize
from loadxml import translations_from_xml
import runpy
from core import translate_code
import traceback
        
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

    #sys.path[0] = os.path.dirname(os.path.join(os.getcwd(), file_path))

    # Get language based off of the file extension. For example, script.fr.py will look for fr.xml
    extensions = pathlib.Path(file_path).suffixes[-2:]
    language = None
    translations = None

    if len(extensions) == 2 and extensions[1] == '.py':
        language = extensions[0][1:]
    
    # Get the path of the expected xml file, and see if it exists. 
    
    xml_file_path = locatexml(f'{language}.xml', os.getcwd())
    if xml_file_path:
        translations = translations_from_xml(xml_file_path)
    else:
        print(f'Could not locate {os.path.join('localizations', f'{language}.xml')}')
        # print("Attempted to search " + xml_file_path)
        exit(1)

    
    # Convert the source code back into valid python

    with open(file_path, encoding='utf-8') as f:
        source = tokenize.untokenize(list(translate_code(f.readline, translations)))

    try:
        code = compile(source, file_path, "exec")
    except Exception as e:
        traceback.print_exception(sys.exception(), limit= -len(traceback.extract_tb(e.__traceback__)) + 1, file=None, chain=True)
        sys.exit()

    sys.argv = sys.argv[1:]
    try:
        with runpy._TempModule("__main__") as temp_module:
            mod_globals = temp_module.module.__dict__
            runpy._run_code(code, mod_globals, mod_name="__main__")
    except Exception as e:
        traceback.print_exception(sys.exception(), limit= -len(traceback.extract_tb(e.__traceback__)) + 3, file=None, chain=True)
        sys.exit()

def locatexml(filename, searchpath):
    for root, dirs, files in os.walk(searchpath):
        if filename in files and root.endswith("\\localizations"): # this only works on windows, fix later
            return os.path.join(root, filename)
    return None

if __name__=="__main__":
    commandline()