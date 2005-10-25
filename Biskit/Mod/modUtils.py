##
## Biskit, a toolkit for the manipulation of macromolecular structures
## Copyright (C) 2004-2005 Raik Gruenberg & Johan Leckner
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## General Public License for more details.
##
## You find a copy of the GNU General Public License in the file
## license.txt along with this program; if not, write to the Free
## Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
##
##
## last $Author$
## last $Date$
## $Revision$
"""utility funtions for Mod package"""


def parse_tabbed_file( fname ):
    """
    fname - str, file name of key : value mapping
    -> { key : value, }
    """
    f = open( fname )

    result = {}
    for l in f:
        if not l[0] == '#':

            try:
                fname, chain_id = l.split()
                if not len(fname) == 0:
                    result[ fname ] = chain_id
            except:
                fname = l.strip()
                result[ fname ] = ''

    f.close()

    return result