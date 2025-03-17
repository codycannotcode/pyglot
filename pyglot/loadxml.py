import xml.etree.ElementTree as ET
import xmlschema
from os import path

schema = xmlschema.XMLSchema(path.join('localizations', 'schema.xsd'))

def translations_from_xml(file_path):
    schema.validate(file_path)

    root = ET.parse(file_path)
    # keywords = tree.getroot().find('keywords')
    # functions = tree.getroot().find('functions')
    print(root.getroot().attrib)

    translation_map = {}

    # for element in functions.findall('function'):
    #     translation = element.text
    #     native = element.get('name')
    #     if translation and native:
    #         translation_map[translation] = native
    
    # for element in keywords.findall('keywords'):
    #     translation = element.text
    #     native = element.get('key')
    #     if translation and native:
    #         translation_map[translation] = native

    return translation_map
    