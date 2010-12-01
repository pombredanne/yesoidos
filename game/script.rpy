# Yesoidos v0.4a2
# script.rpy
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

init -1:
    # replace the default black to match the theme
    image black = blackColor
    
    # slowDissolves are used at section breaks
    define slowDissolve = Dissolve(1)    
    
    # some functions to format the book quotes and chapter titles
    $ from sections import bookText, chapterText
    
    # set a nicer italic font
    $ config.font_replacement_map["DejaVuSans.ttf", False, True] = ("DejaVuSans-Oblique.ttf", False, False)

label start:
    call chapter1 from _call_chapter1
    call chapter2 from _call_chapter2
