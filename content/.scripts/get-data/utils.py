import re

def sanitize_filename(text):
    no_punc = re.sub(r'[^\w\s]', ' ', text)
    remove_extra_space = ' '.join(no_punc.split())
    return remove_extra_space