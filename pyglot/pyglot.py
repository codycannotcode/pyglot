import sys
import os
import pathlib
import tokenize
from loadxml import translations_from_xml
import runpy
from core import translate_code
        
def commandline():
    """
    usage: pyglot file.{language}.py
    """
    if len(sys.argv) != 2:
        print(commandline.__doc__)
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"twpy: file '{file_path}' does not exist")
        sys.exit(1)

    sys.path[0] = os.path.dirname(os.path.join(os.getcwd(), file_path))

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
        print("Could not locate " + language + ".xml")
        print("Attempted to search " + xml_file_path)
        exit(1)
    
    source = tokenize.untokenize(
            list(translate_code(open(file_path, encoding='utf-8').readline, translations)))

    code = compile(source, file_path, "exec")

def locatexml(filename, searchpath):
    for root, dirs, files in os.walk(searchpath):
        if filename in files and root.endswith("\\localizations"):
            return os.path.join(root, filename)
    return None

if __name__=="__main__":
    commandline()