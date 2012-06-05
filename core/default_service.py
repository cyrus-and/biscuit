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

# hosts that match this domain will be processed by this service (None is a
# special case of this default service only)
DOMAIN = None

# a list of field names, a cookie must contain them all to be valid, also only
# these fields will be sent in output (the empty list means that every cookie is
# valid and that every field will be sent in output)
REQUIRED_FIELDS = []

# cookies equality check, given a number of cookies with the same key only the
# last is stored
def key( cookie ):
    return hash( cookie )

# provide a description for this cookie, usually the name or the url of the
# service; this fields is for human only
def header( cookie ):
    return "http://" + url( cookie )

# should return the personal url associated to this cookie (profile) or the url
# of the service without the protocol
def url( cookie ):
    return cookie.host
