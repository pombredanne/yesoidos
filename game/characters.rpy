# Yesoidos
# chapter1.rpy
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
	
init:    
    # Set up Chapter 1 characters
    $ me = Character('Binyomin', color="#6688ff")
    $ zu = Character('Zusha', color="#ff7777")
    $ ch = Character('Children', color="#ccffcc")
    $ pn = Character('Pinchus', color="#bb55ff")
    
    # Characters from the past, like in the Baal Shem Tov story, are in grey
    define storyChar = Character("", color = "#888888")

    # Set up Baal Shem Tov story characters
    $ hs = storyChar.copy("Hashem")
    $ st = storyChar.copy("Satan")
    $ mc = storyChar.copy("Michoel")
    $ el = storyChar.copy("Eliezer")
    $ sr = storyChar.copy("Sara")
    $ yb = storyChar.copy("Yisroel")
    $ sz = storyChar.copy("Shlomo Zalmen")
