#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-

# Copyright (C) 2013 Neil McNab <neil@nabber.org>

# This file is part of GGet for Windows.  It fakes pyinotify calls as that is not supported on Windows.

# GGet is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# GGet is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GGet; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA

class Notification:
    def __init__(self, title, text):
        pass
        
    def set_icon_from_pixbuf(self, pixbuf):
        pass
    
    
def init(name):
    pass