#
# biscuit - Modular HTTP cookie parser
# Copyright (C) 2012 Andrea Cardaci <cyrus.and@gmail.com>
#
# This file is part of biscuit.
#
# biscuit is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# biscuit is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# biscuit. If not, see <http://www.gnu.org/licenses/>.
#

from core.printer_helper import join_fields

# describe this printer
HELP = """\
Use the same format expected in input, just add the header.\
"""

# print a cookie, this function should usually produce a two line output (a
# header and the payload) using some or all of the argument passed:
#
# domain: domain of the cookie
# fields: fields of the cookie in a dictionary
# header: header content produced by the service module
# url: service or user profile url  produced by the service module
def print_entry( domain , fields , header , url ):
    return ( "{0}\n{1} ".format( header , domain ) + join_fields( fields ) )
