import xml.etree.ElementTree as ET

def translations_from_xml(file_path):
    # Load the XML tree
    root = ET.parse(file_path)

    keyword = {}
    for term in root.findall('term'):
        value = term.text  # Foreign language keyword
        key = term.get('key')  # English keyword equivalent
        if value and key:
            keyword[value] = key

    return keyword
    