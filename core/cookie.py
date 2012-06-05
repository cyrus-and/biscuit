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

from core.exception import ParserError

class Cookie:
    def __init__( self , host , cookie_string ):
        self.host = host

        # create a dictionary form the cookie string
        self.pairs = dict()
        for pair in cookie_string.strip().split( "; " ):
            name , sep , value = pair.partition( "=" )
            if sep == "":
                raise ParserError()
            self.pairs[name] = value

    def __hash__( self ):
        return hash( ( self.host , tuple( self.pairs.items() ) ) )

    def __getitem__( self , name ):
        return self.pairs[name]

    def __contains__( self , name ):
        return name in self.pairs

    def __iter__( self ):
        return self.pairs.iteritems()
