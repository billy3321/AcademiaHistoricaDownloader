#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,re,sys
import subprocess


def main(argv):
	#http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//002/08/02/00//00345/023/002-080200-00345-023-001x.jpg
	fn = argv[1]
#	fn = '001-012041-0029'
#	fn = '002-080200-00345-023'
	ndir = argv[2].decode('utf-8')
	if ndir[-1] != '/':
		ndir += '/'
	toks = fn.split('-')
	if len(fn) == 15:
		ln = "%s/%s/%s/%s//%s/%s" % (toks[0], toks[1][:2], toks[1][2:4], toks[1][4:], toks[2][1:], toks[0] + toks[1] + toks[2][1:])
	elif len(fn) == 20:
		ln = "%s/%s/%s/%s//%s/%s/%s" % (toks[0], toks[1][:2], toks[1][2:4], toks[1][4:], toks[2], toks[3], fn)
	tags = ['a', 'm', 'x']

	if not os.path.exists(ndir):
		os.makedirs(ndir)

#	for x in range(1, 500):
	x = 1
	while(1):
#		cmd = "wget 'http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//%s%03dx.jpg' -O %03d.jpg" % (ln, x, x)
		co = 0
		for tag in tags:
			cmd = None
			if len(fn) == 15:
				cmd = "wget 'http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//%s%03d%s.jpg' -O %s%03d.jpg" % (ln, x, tag, ndir.encode('utf-8'), x)
#				cmd = "'http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//%s%03d%s.jpg' -O %s%03d.jpg" % (ln, x, tag, ndir, x)
			elif len(fn) == 20:
				cmd = "wget 'http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//%s-%03d%s.jpg' -O %s%03d.jpg" % (ln, x, tag, ndir.encode('utf-8'), x)
#				cmd = "'http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//%s-%03d%s.jpg' -O %s%03d.jpg" % (ln, x, tag, ndir, x)
			if cmd != None:
#				subprocess.call(['wget', cmd.decode('utf-8')])
				os.system(cmd)
			if os.path.getsize('%s%03d.jpg' % (ndir.encode('utf-8'), x)) >= 10:
				co = 0
				break
			else :
				co += 1
		if co == 3:
			os.system('rm %s%03d.jpg' % (ndir, x))
			break
		x += 1

if __name__=='__main__':
	main(sys.argv)

