#!/bin/sh
# Literary content Copyright (c) 2010 by Musashi <astrochess@gmail.com>
# All rights reserved.
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

function incMinor() {
	if [ ${1} ]; then
		amount=${1}
	else
		amount=1
	fi
	version=`grep -ho 'Yesoidos v[0-9]\+.[0-9abd.]\+' script.rpy | grep -ho '[0-9]\+.[0-9abd.]\+'`
	major=`echo $version | grep -ho '^[^abd]\+[abd]\|\([0-9]\+\.\)\+'`
	minor=`echo $version | grep -ho '[0-9]*$'`
	newminor=$(($minor + $amount))
	setVersion ${major}${newminor}
}
function setVersion() {
	if [ "`echo "${1}" | grep -ho '^[0-9]\+.[0-9abd.]\+$'`" ] ; then
		echo "Setting Yesoidos version to ${1}"
		sed -e "s/Yesoidos v[0-9]\{1,\}.[0-9abd.]\{1,\}/Yesoidos v${1}/" -i '' `ls *.rpy *.py`
		exit 0
	fi
	echo "ERROR: Invalid version number provided as argument." 1>&2
	exit -1
}

cd `dirname "$0"`/game
case $1 in
+[0-9]*) incMinor $1;;
-[0-9]*) incMinor $1;;
[0-9]*) setVersion $1;;
*) cat << EOF
    usage: ${0} [ [+-]increment | new_version ]

This script finds all .rpy and .py files in the yesoidos/game folder 
and changes the version numbers found therein.

The version number on line 1 of yesoidos/game/script.py is considered 
authoritative, and is used to the determine the version number of the 
entire project. This is important when decrementing or incrementing
the minor version number, and when packaging the project source files
using yesoidos/package-source.sh.

EOF
;;
esac
