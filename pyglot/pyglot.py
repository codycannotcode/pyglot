import sys
import os
import pathlib
import tokenize
from loadxml import translations_from_xml
import runpy
from core import translate_code
        
def commandline():
    """
    usage: pyglot file.pyg
    """
    if len(sys.argv) != 2:
        print(commandline.__doc__)
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"twpy: file '{file_path}' does not exist")
        sys.exit(1)

    sys.path[0] = os.path.dirname(os.path.join(os.getcwd(), file_path))

    extensions = pathlib.Path(file_path).suffixes[-2:]
    if len(extensions) == 2 and extensions[1] == '.py':
        pass
        


    # source = tokenize.untokenize(
    #         list(translate_code(open(file_path, encoding='utf-8').readline)))

    # code = compile(source, file_path, "exec")

    # runpy._run_module_code(code, mod_name="__main__")

if __name__=="__main__":
    commandline()