from loadxml import translations_from_xml
import tokenize
import re

lang_re = re.compile(r'lang[=:]\s*([-\w.]+)')

def translate_code(readline, translations):
    # Specify which language using a magic comment
    # Searches up to 3 consecutive comments at the top of the file
    # Use the same style of magic commment for python's encoding
    # https://docs.python.org/3/reference/lexical_analysis.html#encoding-declarations

    # lang_name = ''
    # translations = {}
    # m = 3

    # for tok, name, _,_,_ in tokenize.generate_tokens(readline):
    #     if tok == tokenize.NL:
    #         m -= 1
    #     if tokenize.COMMENT:
    #         match: re.Match = lang_re.search(name)
    #         if match:
    #             lang_name = f'{match.group(1)}.xml'
    #     if m <= 0 or not (tok == tokenize.COMMENT or tok == tokenize.NL):
    #         break

    for tok, name, _,_,_ in tokenize.generate_tokens(readline):
        if tok == tokenize.NAME and name in translations:
            yield tokenize.NAME, translations[name]
        else:
            yield tok, name
            
