# Based on the Perl implementation of Dave Koelle's Alphanum algorithm
# Beau Gunderson <beau@beaugunderson.com>, 2007
# http://www.bylandandsea.org/
# http://www.beaugunderson.com/

#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#

test_strings = [ "1000X Radonius Maximus", "10X Radonius", "200X Radonius", "20X Radonius", "20X Radonius Prime", "30X Radonius", "40X Radonius", "Allegia 50 Clasteron", "Allegia 500 Clasteron", "Allegia 51 Clasteron", "Allegia 51B Clasteron", "Allegia 52 Clasteron", "Allegia 60 Clasteron", "Alpha 100", "Alpha 2", "Alpha 200", "Alpha 2A", "Alpha 2A-8000", "Alpha 2A-900", "Callisto Morphamax", "Callisto Morphamax 500", "Callisto Morphamax 5000", "Callisto Morphamax 600", "Callisto Morphamax 700", "Callisto Morphamax 7000", "Callisto Morphamax 7000 SE", "Callisto Morphamax 7000 SE2", "QRS-60 Intrinsia Machine", "QRS-60F Intrinsia Machine", "QRS-62 Intrinsia Machine", "QRS-62F Intrinsia Machine", "Xiph Xlater 10000", "Xiph Xlater 2000", "Xiph Xlater 300", "Xiph Xlater 40", "Xiph Xlater 5", "Xiph Xlater 50", "Xiph Xlater 500", "Xiph Xlater 5000", "Xiph Xlater 58" ]

import re

re_chunk = re.compile("([\D]+|[\d]+)")
re_letters = re.compile("\D+")
re_numbers = re.compile("\d+")

def getchunk(item):
	itemchunk = re_chunk.match(item)

	# Subtract the matched portion from the original string
	# if there was a match, otherwise set it to ""
	item = (item[itemchunk.end():] if itemchunk else "")
	# Don't return the match object, just the text
	itemchunk = (itemchunk.group() if itemchunk else "")

	return (itemchunk, item)

def alphanum(a, b):
	n = 0

	while (n == 0):
		# Get a chunk and the original string with the chunk subtracted
		(ac, a) = getchunk(a)
		(bc, b) = getchunk(b)

		# Both items contain only letters
		if (re_letters.match(ac) and re_letters.match(bc)):
			n = cmp(ac, bc)
		else:
			# Both items contain only numbers
			if (re_numbers.match(ac) and re_numbers.match(bc)):
				n = cmp(int(ac), int(bc))
			# One item has letters and one item has numbers, or one item is empty
			else:
				n = cmp(ac, bc)

				# Prevent deadlocks
				if (n == 0):
					n = 1

	return n

test_strings.sort(cmp=alphanum)

for (v) in test_strings:
	print v

