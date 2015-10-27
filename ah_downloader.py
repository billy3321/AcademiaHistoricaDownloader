#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re, sys
from random import randint
from time import sleep
from PIL import Image, ImageDraw
import argparse


def main():
  parser = argparse.ArgumentParser(description='Academia Historica Data Downloader')
  parser.add_argument("-d", "--dir", dest="dir", required=True,
                  help="save result to which directory", nargs='?')
  parser.add_argument("-i", "--identifier", dest="identifier", required=True,
                  help="identifier number", nargs='?')
  args = parser.parse_args()
  # usage: ./ah_downloader.py -i 001-012041-0029 -d 黨務人員從事政治工作考試法（一）
  identifier = args.identifier
  # identifier example:
  # '001-012041-0029'
  # '002-080200-00345-023'
  directory = args.dir
  if directory[-1] != '/':
    directory += '/'
  tokens = identifier.split('-')
  if len(identifier) == 15:
    url_path = "%s/%s/%s/%s//%s/%s" % (tokens[0], tokens[1][:2], tokens[1][2:4], tokens[1][4:], tokens[2][1:], tokens[0] + tokens[1] + tokens[2][1:])
  elif len(identifier) == 20:
    url_path = "%s/%s/%s/%s//%s/%s/%s" % (tokens[0], tokens[1][:2], tokens[1][2:4], tokens[1][4:], tokens[2], tokens[3], identifier)
  tags = ['a', 'm', 'x']

  if not os.path.exists(directory):
    os.makedirs(directory)

  num = 1
  while(1):
    retry = 0
    for tag in tags:
      sleep(randint(1,5))
      cmd = None
      output = '%s%03d.jpg' % (directory, num)
      if len(identifier) == 15:
        cmd = "wget 'http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//%s%03d%s.jpg' -O %s" % (url_path, num, tag, output)
      elif len(identifier) == 20:
        cmd = "wget 'http://weba.drnh.gov.tw/resource/images/pic.jsp?downloadPic=/picture/WaterMark?url=http://172.16.1.111:8081//%s-%03d%s.jpg' -O %s" % (url_path, num, tag, output)
      if cmd != None:
        os.system(cmd)

      if os.path.getsize(output) >= 10:
        retry = 0
        image = Image.open(output)
        draw = ImageDraw.Draw(image)
        draw.rectangle(((0, (image.size[1] - 57)),(363, image.size[1])), fill="white")
        image.save(output)
        break
      else :
        retry += 1
    if retry == 3:
      os.system('rm %s' % output)
      break
    num += 1

if __name__ == '__main__':
  main()

