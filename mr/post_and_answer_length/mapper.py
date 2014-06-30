#!/usr/bin/env python

import sys
import csv

def mapper(f):
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	for line in reader:
	
		if len(line)!=19:
			continue
		if line[0]=='id':
			continue
		
		author_id=line[3]
		added_at =line[8]
	
		hour = added_at[11:13]
	
		print author_id+" "+hour

mapper()
