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

import re
from core.cookie import Cookie
from core.service_wrapper import ServiceWrapper
from core.exception import ParserError
from core import default_service

class System:
    # printer: module used to format the output
    # use_default: if True unknown cookies will be sent to the default service
    # services: dictionary of user services
    def __init__( self , printer , use_default = True , services = dict() ):
        self.printer = printer
        self.wrappers = dict()
        self.default_service = use_default and ServiceWrapper( default_service )
        for _ , service in services.iteritems():
            self.wrappers[ service.DOMAIN ] = ServiceWrapper( service )

    # split and process a line: <host><blanks><cookie>
    def process_line( self , line ):
        split = re.split( "\s+", line.strip() , 1 )
        if len( split ) == 1:
            raise ParserError()
        domain , cookie_string = split
        self.process_cookie( Cookie( domain , cookie_string ) )

    def process_cookie( self , cookie ):
        processed = False
        for domain , wrapper in self.wrappers.iteritems():
            if cookie.host.endswith( domain ): # match?
                wrapper.process( cookie )
                processed = True
        if not processed and self.default_service:
            self.default_service.process( cookie )
        return processed

    def dump( self , file , prefix = "" ):
        for domain , wrapper in self.wrappers.iteritems():
            wrapper.dump( self.printer , file , prefix )
        if self.default_service:
            self.default_service.dump( self.printer , file , prefix )
