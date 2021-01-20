#!/bin/python -B
#
# Colors In Terminal
# {2021-01-20}
#

import sys, re
from sty import *

from urllib.request import urlopen

site = 'https://alexbeals.com/projects/colorize/search.php?q='

try:

	cmd = sys.argv
	if len(cmd) <= 1:
		print('usage: <word>')
		sys.exit()
	elif cmd[1]:
		find = cmd[1]
	else: sys.exit()

	data = urlopen(f'{site}{find}')
	html = data.read().decode('utf-8')

	chex = re.search('hex\'\);">#(.*?)</span>', html).group(1)
	crgb = re.search('rgb\'\);">rgb\((.*?)\)</span>', html).group(1)

	slen = ' '.ljust(16)
	srgb = crgb.split(',')

	bg.cl = Style(RgbBg(srgb[0], srgb[1], srgb[2]))

	print(f'\n HEX: {chex}\n RGB: {crgb}')
	print(f' {bg.cl}{slen}{bg.rs}\n')

except KeyboardInterrupt:
	print('Exited'); sys.exit();

#EOF: ./color.py
