import xmlschema

schema = xmlschema.XMLSchema("pyglot.xsd")
schema.validate('es.xml')
print(schema.is_valid('es.xml'))