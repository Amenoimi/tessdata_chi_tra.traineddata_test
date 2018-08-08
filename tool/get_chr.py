#-*- coding: utf-8 -*-　

import sys
import os

min_chr=19968

#text_file = open("input.txt", "r", encoding = 'utf-8-sig')
#lines = text_file.readlines()
#print (lines)



go_chr= input('請輸入你的訓練集：')#["我","你","他","是","不","貓","咪","牛","狗","狼","走","廊","班","馬","魚","們","搬","家","啦","媽","爸","哥","獅","子","弟","一","二","三","四","五","六","七","八","九","十","筆","燒","肉","定","食","請","說","方","法","假","張","吃","飯","喝","水"]
go_chr=list(go_chr)
n=6
out=[]


def write_file(path, data):
	with open(path, "w", encoding='UTF-8') as f:
		f.writelines(data)


for a in go_chr:

    if ord(a)-int(n/2) <= min_chr:
        for x in range(n):
            #print (chr(ord(a)+x).encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
            out+=chr(ord(a)+x)
    else:
        for x in range(n):
            #print (chr(ord(a)+x-5).encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
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
