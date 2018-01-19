# -*- coding:utf-8 -*-
import codecs

num = 0
wf1 = codecs.open("badoo_part1.txt", "a", "utf8")
wf2 = codecs.open("badoo_part2.txt", "a", "utf8")
with codecs.open("badoo.txt", "r", "utf8") as f:
    for line in f:
        num += 1
        if num > 60000000:
            wf2.write(line + "\n")
        else:
            wf1.write(line + "\n")
wf1.close()
wf2.close()
