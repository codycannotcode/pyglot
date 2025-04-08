import xml.etree.ElementTree as ET
import xmlschema
from os import path

schema = xmlschema.XMLSchema(path.join('localizations', 'schema.xsd'))
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
    