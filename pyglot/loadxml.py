import xml.etree.ElementTree as ET

def translations_from_xml(file):
    # Load the XML tree
    root = ET.parse(file)

    # Create the dictionary
    keyword = {}
    for term in root.findall('term'):
        value = term.text  # Foreign Language Keyword
        key = term.get('key')  # English keyword
        if value and key:
            keyword[value] = key

    return keyword