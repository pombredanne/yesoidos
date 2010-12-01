# Yesoidos
# chapter2.rpy
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

label chapter2:
    scene black
    with dissolve
    
    show text chapterText(2, "The Training") with dissolve
    pause
    scene black with dissolve
    show text bookText("The candle of God is the soul of Man, searching the chambers of the depths.", "Proverbs 20:27") with dissolve
    pause
    scene black with dissolve   
    
    me "hullo!"


    # $ BookQuote("Why should it bother you? He who decreed that oil should burn will decree that the vinegar should burn, too.",
    # "Gemoro, Ta'ainis 25a")
    #s = BookStr("The Almighty saw that the tsadikim were few so He planted them in every generation.",
    #"Gemoro, Yoima 38b")
    
    return