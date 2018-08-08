#-*- coding: utf-8 -*-　

import sys
import os

min_chr=19968



go_chr= input('請輸入你的訓練集：')
go_chr=list(go_chr)
n=20
out=[]


def write_file(path, data):
	with open(path, "w", encoding='UTF-8') as f:
		f.writelines(data)


for a in go_chr:

    if ord(a)-int(n/2) <= min_chr:
        for x in range(n):
            out+=chr(ord(a)+x)
    else:
        for x in range(n):
             out+=chr(ord(a)+x-int(n/2))

tmp=["!","?",","]
[tmp.append(i) for i in out if not i in tmp]
out=tmp
tmp=[]
for a in range(len(out)):
        tmp.append(ord(out[a]))
tmp=sorted(tmp)

for a in range(len(tmp)):
        out[a]=chr(tmp[a])

write_file("ch.font.exp0.txt", out)
