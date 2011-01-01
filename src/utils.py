import re
from htmlentitydefs import name2codepoint

from errors import DownloaderError

def get_input(message):
    input = raw_input(message)
    return input

def write_file(file_path, data):
    try:
        out_file = open(file_path, 'w')
        out_file.write(data)
        out_file.close()
    except IOError as error:
        if '13' in error:
            raise DownloaderError('Need higher permissions to write' +
              'settings')
        else:
            raise DownloaderError('File error')

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def remove_entities(word):
	word = word.replace("&#039;", "'")
	return word
