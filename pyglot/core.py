import tokenize

def translate_code(readline, translations=None):
    for tok, name, _,_,_ in tokenize.generate_tokens(readline):
        if translations and tok == tokenize.NAME and name in translations:
            yield tokenize.NAME, translations[name]
        else:
            yield tok, name
            
