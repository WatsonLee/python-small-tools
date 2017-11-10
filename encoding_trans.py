# -*- coding=utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import codecs

def Ansi_to_utf8(infile_path, outfile_path):
    inf = codecs.open(infile_path, "r", "mbcs")
    outf = codecs.open(outfile_path, "w", "utf8")
    for line in inf:
        outf.write(line)
    outf.close()
    inf.close()

def Gb2312_to_utf8(infile_path, outfile_path):
    inf = codecs.open(infile_path, "r", "gb2312")
    outf = codecs.open(outfile_path, "w", "utf8")
    for line in inf:
        outf.write(line)
    outf.close()
    inf.close()
