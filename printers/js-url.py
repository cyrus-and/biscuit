import urllib
from core.printer_helper import join_fields

HELP = """\
Javascript code to set the cookie and load the service directly in the URL bar
of the browser. Steps:

 1. point the browser to the service url;

 2. copy the generated Javascript code (the line starting with "javascript:") in
    the URL bar of the browser and hit enter.

NOTES:

 - some browsers will remove the initial "javascript:" from the pasted string;
   add that by hand.

 - since it's not easy to know exactly in which upper level domain to set the
   cookie (or simply *what* is the upper level domain) the generated code just
   tries to set the cookies in every domains until the TLD.

 - it's advised to use an "incognito" browser session to avoid any interferences
   with the current cookies.\
"""

ENTRY_TEMPLATE = "{0}\njavascript:"
PAIR_TEMPLATE = "document.cookie='{0}={1};domain=.'+d+';path=/';"
REDIR_TEMPLATE = "window.location='http://{0}';"

def print_entry( domain , fields , header , url ):
    out = "d=document.domain;while(1){"
    out += join_fields( fields , PAIR_TEMPLATE , "" )
    out += "if((dd=d.indexOf('.'))==-1)break;d=d.slice(dd+1);}"
    out += REDIR_TEMPLATE.format( url )
    out = urllib.quote( out )
    return ENTRY_TEMPLATE.format( header ) + out
