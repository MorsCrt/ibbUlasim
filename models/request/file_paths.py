import os
from pathlib import Path

path = Path(os.path.dirname(os.path.abspath(__file__)))
ibb_func_path = str(path.parent.parent.absolute())
    
links_file_path = ibb_func_path + '\\Links\\datasets_links.txt'
link_file_open = open(links_file_path, 'r')
links_file = link_file_open.read()
x=links_file.split('\n')
x.remove('')
print(x)