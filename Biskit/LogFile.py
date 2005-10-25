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
## $Revision$
## last $Date$
## last $Author$

import Biskit.tools as T
import sys

class LogFile:
    """
    Simple log file that can be passed between objects.
    It is flushed after each writing and should hence always be
    up2date.
    """

    def __init__(self, fname, mode='w'):
        self.fname = T.absfile( fname )
        self.mode  = mode
        self._f  = None

    def f( self ):
        """
        Open file only when needed for first time.
        -> file object
        """
        if self._f is None:
            self._f = open( self.fname, self.mode )

        return self._f

    def add(self, s):
        self.f().writelines(s+"\n")
        self.f().flush()

    def add_nobreak(self, s):
        self.f().writelines(s)
        self.f().flush()

    def __del__(self):
        if self._f is not None:
            self.f().close()
            self._f = None


class ErrLog( LogFile ):
    """
    Print to stderr instead.
    """

    def __init__(self):
        self.fname = None
        self.mode  = None
        self._f   = sys.stderr

    def __del__(self):
        pass


class StdLog( LogFile ):
    """
    Print to std out.
    """
    def __init__(self):
        self.fname = None
        self.mode  = None
        self._f   = sys.stdout

    def __del__(self):
        pass