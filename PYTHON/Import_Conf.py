def main():

import pandas as pd
import win32com.client
import matplotlib
import unicodedata
import codecs
import sqlite3
import sys

conf = pd.read_csv("PYTHON/PEP0000903846_Conf2019 - Copy.TXT", sep = "|", skiprows = 3, encoding = "ISO-8859-1", usecols=lambda x: x not in ['Unnamed: 0','Unnamed: 25'])
test0 = pd.read_csv("PYTHON/PEP0000903846_Conf2019 - Copy.TXT", sep = "|", skiprows = 3, encoding = "ISO-8859-1")

conf2 = conf[conf['  Ordem     ']!='  Ordem     ']
conf_obj = Conf.select_dtypes(['object'])
Conf[conf_obj.columns] = conf_obj.apply(lambda x: x.str.strip())

conf2 = conf[conf['  Ordem     ']!='Ordem']
'''print(open('PYTHON/PEP0000903846_Conf2019 - Copy.TXT').read())'''

main()


'help links'
'How to open a file'
'https://stackoverflow.com/questions/22137613/python-open-and-read-a-file-containing-germanic-umlaut-as-unicode'

'File Formats'
'https://docs.python.org/3/library/codecs.html#text-encodings'
