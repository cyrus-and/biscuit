from core.printer_helper import join_fields

HELP = """\
Command to reach the service by using the --header option of Wget to set the
cookie.\
"""

ENTRY_TEMPLATE = "{0}\nwget {1} --header='Cookie: {2}'"

def print_entry( domain , fields , header , url ):
    return ENTRY_TEMPLATE.format( header , url , join_fields( fields ) )
