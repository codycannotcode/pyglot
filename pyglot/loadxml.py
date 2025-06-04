import xml.etree.ElementTree as ET
import xmlschema
import sys
import os
from pathlib import Path

currpath = Path(os.path.realpath(__file__))
if currpath.parent / 'localizations' not in [subdir for subdir in currpath.parent.iterdir() if subdir.is_dir()]:
    print("Could not locate " + str(currpath.parent / 'localizations'))
    exit(1)

localizations = currpath.parent / 'localizations'

if localizations / 'schema.xsd' not in [f for f in localizations.iterdir() if not f.is_dir()]:
    print("Could not locate " + str(localizations / 'schema.xsd'))
    exit(1)

schema = xmlschema.XMLSchema(str(localizations / 'schema.xsd'))
ns = {'': 'http://pyglot.com/schema'}

def translations_from_xml(file_path):
    schema.validate(file_path)

    tree = ET.parse(file_path)
    keywords = tree.find('keywords', ns)
    functions = tree.find('functions', ns)

    translation_map = {}

    for element in functions.findall('function', ns):
        translation = element.text
        native = element.get('name')
        if translation and native:
            translation_map[translation] = native

    for element in keywords.findall('keyword', ns):
        translation = element.text
        native = element.get('key')
        if translation and native:
            translation_map[translation] = native

    return translation_map


# def locatexml(filename, searchpath):
#     for root, dirs, files in os.walk(searchpath):
#         if filename in files and root.endswith("\\localizations"): # this only works on windows, fix later
#             return os.path.join(root, filename)
#     return None

# def gettranslations(filename):
#     xml_file_path = locatexml(filename, os.getcwd())
#     if xml_file_path:
#         translations = translations_from_xml(xml_file_path)
#     else:
#         print(f'Could not locate {os.path.join('localizations', f'{filename.split('.')[-2]}.xml')}')
#         sys.exit(1)
#     return translations