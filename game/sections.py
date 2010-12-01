# Yesoidos
# sections.rpy
#
# All rights reserved.
# Literary content Copyright (c) 2010 by Musashi <astrochess@gmail.com>
#
# This file is part of Yesoidos.
#
# The non-literary content of Yesoidos is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public License as 
# published by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import renpy.exports as renpy

def bookText(text, author = None, title = None):        
    if author and title:
        return "{i}%s{/i}\n\n- {i}%s{/i}, %s" % (text, author, title)
    elif title:
        return "{i}%s{/i}\n\n- %s" % (text, title)
    elif title:
        return "{i}%s{/i}\n\n- {i}%s{/i}" % (text, author)
    else:
        return "{i}%s{/i}" % text


def chapterText(number = None, title = None):
    if not title and not number:
        raise Exception("chapterText() requires at least one argument")
    if not title:
        return "{size=+20}{i}Chapter %d{/i}{/size}" % number
    elif not number:
        return "{size=+20}{i}%s{/i}{/size}" % title
    else: # have both a number and a title
        return "{size=+10}{i}Chapter %d{/size}{size=+20}\n\n%s{/i}{/size}" % (number, title)
    
