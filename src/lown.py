#!/usr/local/bin/python3

'''
Parser for the lown markup language
'''

import csv
import os
import re
import sys

import markdown

# Tags

cwd = os.getcwd()
os.chdir('/usr/local/Lown/src')

with open('tags.csv') as file:
	tags = list(csv.reader(file))

with open('emojis.csv') as file:
	emojis = list(csv.reader(file))

with open('header.html', 'r') as file:
	header = file.read()

os.chdir(cwd)

# Parser


def parse(text):
	# Escaped characters
	for ch, es in [('\[', '&#91;'), ('\]', '&#93;'),
				   ('<', '&lt;'), ('>', '&gt;')]:
		text = text.replace(ch, es)
	# Maths
	text = re.sub('\[\$\s([^\[\]]*)\]', r'\\(\1\\)', text)
	text = re.sub('\[\$\$\]([^\[\]]*)\[/\$\$\]', r'$$\1$$', text)
	# Selft closing tags
	text = text.replace('[/hr]', '</hr>')
	text = text.replace('[/br]', '</br>')
	# Links and images
	text = re.sub('\[url\s([^ ]*)(.*)\]', r'<a href="\1">\2</a>', text)
	text = re.sub('\[img\s([^ ]*)(.*)\]', r'</img src="\1" alt="\2">', text)
	# Emojis
	for src, tgt in emojis:
		text = text.replace(src, tgt)
	# Standard tags
	for i in range(text.count('[')):
		for tag in tags:
			if tag[1] == 'inline':
				pattern = '\[' + tag[0] + '\s([^\[\]]*)\]'
			elif tag[1] == 'block':
				pattern = '\[%s\]' % tag[0] + '([^\[\]]*)' + '\[/%s\]' % tag[0]
			if tag[3] != '':
				subst = '<%s class="%s">' % (tag[2], tag[3])
				subst += r'\1</' + tag[2] + '>'
			else:
				subst = '<' + tag[2] + r'>\1</' + tag[2] + '>'
			text = re.sub(pattern, subst, text)
	# Paragraphs
	text = re.sub('[\r\n]+', '\n', text)
	lines = text.split('\n')
	text = ''
	for line in lines:
		if len(line) < 4 or (line[:1] != '<h' and line[3] != '>'):
			text += '<p>' + line + '</p>\n'
		else:
			text += line
	return text


if __name__ == '__main__':
	path = sys.argv[1]
	with open(path, 'r') as file:
		content = file.read()
	
	if len(sys.argv) > 2 and sys.argv[2] == '-s':
		# Standalone
		print('<!DOCTYPE html>\n<html>')
		print(header)
		print(parse(content))
		print('</body></html>')
	else:
		print(parse(content))
	
# TODO: links and images
