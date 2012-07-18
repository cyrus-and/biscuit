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

import os
import glob
import imp

# load all the python modules in the given directory returning a dictionary:
# module name -> module object
def load_module_dir( path ):
    root_path = os.path.join( os.path.dirname( __file__ ) , ".." )
    modules = dict()
    pattern = glob.glob( os.path.join( root_path , path , "*[!_].py" ) )
    for file in pattern:
        name , _ = os.path.splitext( os.path.basename( file ) )
        modules[ name ] = imp.load_source( name , file )
    return modules
