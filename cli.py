#!/usr/local/bin/python3
#!/usr/bin/python3

import IPython
from traitlets.config import Config

conf=Config()
conf.InteractiveShell.banner1=""" Bienvenu dans Sky """
conf.InteractiveShell.editor = 'nano'
conf.InteractiveShellApp.exec_lines = [
    '#get_ipython().prompts=TXlQcm9tcHQK(get_ipython())',
    '#from fonctions import search',
    'from interative import (view_vuln,view_info,search_peer_kinds,banner_1,start)',
    ]


IPython.start_ipython(config=conf)
