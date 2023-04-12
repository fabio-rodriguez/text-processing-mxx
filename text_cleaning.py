import re

def substitute_re_in_text(text, re_str, new_str=''):
    return re.sub(re_str, new_str, text)

def remove_links_in_text(text):
    link_re = 'http[s]?://\S+'
    return substitute_re_in_text(text, link_re)

def remove_breaklines_in_text(text):
    return text.replace('\r\n','').replace('\n','')

def remove_quotes_in_text(text):
    return text.replace('"','').replace("'",'')

