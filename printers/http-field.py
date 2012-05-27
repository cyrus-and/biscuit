from core.printer_helper import join_fields

HELP = """\
HTTP 'Cookie:' field format.\
"""

ENTRY_TEMPLATE = "{0}\nCookie: "

def print_entry( domain , fields , header , url ):
    return ( ENTRY_TEMPLATE.format( header ) + join_fields( fields ) )
