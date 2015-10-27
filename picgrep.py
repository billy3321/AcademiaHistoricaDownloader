#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re, sys
from random import randint
from time import sleep
from PIL import Image, ImageDraw


def main(argv):
  # usage: ./picgrep.py 001-012041-0029 黨務人員從事政治工作考試法（一）
  fn = argv[1]
  # fn = '001-012041-0029'
  # fn = '002-080200-00345-023'
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

  x = 1
  while(1):
    co = 0
    for tag in tags:
      sleep(randint(1,5))
      cmd = None
      output = '%s%03d.jpg' % (ndir.encode('utf-8'), x)
      if len(fn) == 15:
        cmd = "wget 'http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//%s%03d%s.jpg' -O %s" % (ln, x, tag, output)
      elif len(fn) == 20:
        cmd = "wget 'http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//%s-%03d%s.jpg' -O %s" % (ln, x, tag, output)
      if cmd != None:
        os.system(cmd)

      if os.path.getsize(output) >= 10:
        co = 0
        im = Image.open(output)
        dr = ImageDraw.Draw(im)
        dr.rectangle(((0, (im.size[1] - 57)),(363, im.size[1])), fill="white")
        im.save(output)
        break
      else :
        co += 1
    if co == 3:
      os.system('rm %s' % output)
      break
    x += 1

if __name__ == '__main__':
  main(sys.argv)

