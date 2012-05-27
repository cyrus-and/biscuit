#
# biscuit - modular HTTP cookie parser
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

class ServiceWrapper:
    def __init__( self , service ):
        self.service = service
        self.cookies = dict()

    # test and process a given cookie for this service storing it if matches
    def process( self , cookie ):
        for name in self.service.REQUIRED_FIELDS:
            if not name in cookie: return False
        key = self.service.key( cookie )
        self.cookies[ key ] = cookie
        return True

    # dump the cookies stored by this service to a file given a printer module
    def dump( self , printer , file , prefix ):
        for _ , cookie in self.cookies.iteritems():
            domain = self.service.DOMAIN or cookie.host
            fields = dict( ( name , value ) for name , value in cookie
                           if ( not self.service.REQUIRED_FIELDS or
                                name in self.service.REQUIRED_FIELDS ) )
            header = self.service.header( cookie )
            url = self.service.url( cookie )
            entry = printer.print_entry( domain , fields , header , url )
            file.write( prefix + entry + "\n" )
